import json
import os
import re
import subprocess
import sys
import tempfile
import time
import calendar
from datetime import datetime
import requests
import feedparser

# --- IMPORTS DE SISTEMA ---
try:
    import notify2
    from gi.repository import GLib
    import dbus.mainloop.glib 
except ImportError:
    print("❌ Error: Faltan librerías. Instala: python3-notify2 python3-dbus python3-gi")
    sys.exit(1)

# --- CONFIGURACIÓN ---
ARCHIVO_CONFIG = "config.json"
# Usamos /tmp para que no moleste, pero se borra al reiniciar
ARCHIVO_HISTORIAL = os.path.join(tempfile.gettempdir(), "x_notifier_vistos.txt")

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

HTML_TEMPLATE = """<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>Novedades X</title><style>body{{font-family:sans-serif;background:#f7f9f9;padding:20px;max-width:600px;margin:0 auto}}.card{{background:white;border-radius:12px;padding:15px;margin-bottom:15px;border:1px solid #eff3f4}}.user{{font-weight:bold;color:#0f1419}}.date{{color:#536471;font-size:0.9em;float:right}}.text{{margin:10px 0;white-space:pre-wrap}}.btn{{display:inline-block;background:#1d9bf0;color:white;padding:5px 15px;border-radius:20px;text-decoration:none;font-size:0.9em}}</style></head><body><h2>🔔 {cantidad} Novedades</h2>{contenido}</body></html>"""

NOTIFICACIONES_ACTIVAS = []

# --- UTILIDADES ---

def cargar_json(archivo):
    try:
        with open(archivo, 'r') as f: return json.load(f)
    except: return {}

def guardar_visto(tweet_id):
    with open(ARCHIVO_HISTORIAL, 'a') as f: f.write(f"{tweet_id}\n")

def limpiar_html(texto):
    if not texto: return ""
    texto = re.sub(r'<(br\s*/?|/p)>', '\n', texto, flags=re.IGNORECASE)
    texto = re.sub(r'<[^>]+>', '', texto)
    return re.sub(r'\n\s*\n', '\n', texto).strip()

def normalizar_link(link):
    return link.replace("twitter.com", "x.com")

def generar_html(datos):
    ruta = os.path.join(tempfile.gettempdir(), "x_notifier_resumen.html")
    cards = ""
    for t in datos:
        cards += f"""<div class="card"><div><span class="user">@{t['user']}</span><span class="date">{t['date']}</span></div>
        <div class="text">{t['text']}</div><a href="{t['link']}" class="btn" target="_blank">Ver en X</a></div>"""
    
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE.format(cantidad=len(datos), contenido=cards))
    return ruta

# --- INTERACCIÓN ---

def al_hacer_click(n, action, ruta):
    if action in ["default", "abrir"]:
        subprocess.Popen(['google-chrome', ruta], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    n.close()
    if n in NOTIFICACIONES_ACTIVAS: NOTIFICACIONES_ACTIVAS.remove(n)

def notificar(titulo, mensaje, ruta):
    try:
        n = notify2.Notification(f"X: {titulo}", mensaje, "twitter")
        n.add_action("default", "Ver", lambda n, a: al_hacer_click(n, a, ruta))
        n.set_timeout(25000) 
        n.show()
        NOTIFICACIONES_ACTIVAS.append(n)
    except Exception as e:
        print(f"Error notificación: {e}")

# --- LÓGICA CORE ---

def procesar():
    print(f"--- Escaneando: {time.strftime('%H:%M:%S')} ---")
    config = cargar_json(ARCHIVO_CONFIG)
    if not config: return True

    if os.path.exists(ARCHIVO_HISTORIAL):
        with open(ARCHIVO_HISTORIAL, 'r') as f:
            vistos = set(line.strip() for line in f)
    else:
        vistos = set()
    
    host = config.get("nitter_host", "https://rsshub.pseudoyu.com/twitter").rstrip('/')
    nuevos = []

    for usuario, filtros in config.get("users", {}).items():
        url = f"{host}/user/{usuario}/includeRts=0"
        
        try:
            resp = requests.get(url, headers=HEADERS, timeout=15)
            if resp.status_code != 200:
                print(f"⚠️ {resp.status_code} @{usuario}")
                continue
            
            feed = feedparser.parse(resp.content)
            
            # SIMPLIFICACIÓN: Solo miramos los últimos 3.
            # Si hay algo nuevo aquí, avisamos. Si no, seguimos.
            for entrada in feed.entries[:3]:
                tid = entrada.guid if 'guid' in entrada else entrada.id
                
                # Si ya está visto, pasamos al siguiente tweet
                if tid in vistos: 
                    continue

                # Filtros de palabras
                texto = limpiar_html(entrada.summary)
                if filtros and not any(re.search(r'\b'+re.escape(k.lower())+r'\b', texto.lower()) for k in filtros):
                    # Si no pasa el filtro, lo marcamos visto para no analizarlo siempre
                    vistos.add(tid)
                    guardar_visto(tid)
                    continue

                # Si llegamos aquí, es NUEVO y pasó los filtros
                ts = calendar.timegm(entrada.published_parsed) if hasattr(entrada, 'published_parsed') else 0
                fecha_obj = datetime.fromtimestamp(ts)
                fecha_fmt = f"Hoy {fecha_obj.strftime('%H:%M')}" if fecha_obj.date() == datetime.now().date() else fecha_obj.strftime('%d/%m %H:%M')
                
                link = normalizar_link(entrada.link)
                
                print(f"🔔 @{usuario} ({fecha_fmt}): {texto[:50]}...")
                nuevos.append({'user': usuario, 'date': fecha_fmt, 'text': texto, 'link': link, 'ts': ts})
                
                vistos.add(tid)
                guardar_visto(tid)

        except Exception as e:
            print(f"Error @{usuario}: {e}")

    if nuevos:
        nuevos.sort(key=lambda x: x['ts'], reverse=True)
        ruta = generar_html(nuevos)
        usrs = ", ".join([x['user'] for x in nuevos[:3]]) + ("..." if len(nuevos)>3 else "")
        notificar(f"{len(nuevos)} Novedades", f"De: {usrs}\n(Click para abrir)", ruta)
    else:
        print("✅ Sin novedades.")
    
    return True

def main():
    print("🚀 X-Notifier RSSHub Edition")
    try:
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        notify2.init("X-Notifier")
    except: sys.exit(1)

    procesar()
    
    tiempo = cargar_json(ARCHIVO_CONFIG).get("tiempo_espera", 300)
    print(f"😴 Ciclo: {tiempo/60:.1f}m")
    
    loop = GLib.MainLoop()
    GLib.timeout_add_seconds(tiempo, procesar)
    try: loop.run()
    except KeyboardInterrupt: pass

if __name__ == "__main__":
    main()