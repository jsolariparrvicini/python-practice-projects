X-Notifier (RSSHub Edition)

Un monitor de escritorio ligero y eficiente para X (Twitter) en Ubuntu. Utiliza RSSHub para obtener los datos y el sistema nativo de notificaciones de Linux (D-Bus/GLib) para enviar alertas interactivas.

🚀 Características

Motor RSSHub: Más rápido y estable que Nitter. Filtra Retweets desde el servidor.

Reportes Visuales: Genera automáticamente un HTML amigable y limpio con el resumen de las novedades, evitando leer texto crudo en la consola.

Notificaciones Interactivas: Haz clic en la burbuja de notificación para abrir el reporte HTML directamente en tu navegador.

Cero Basura: Usa /tmp para el historial y los resúmenes, no ensucia tu carpeta de proyecto.

Smart Links: Convierte automáticamente los enlaces para que lleven siempre a x.com.

Filtros de Palabras: Define palabras clave por usuario para recibir solo lo que te interesa.

Bajo Consumo: Utiliza GLib MainLoop para esperar eventos sin saturar la CPU.

📋 Requisitos del Sistema

Este script está diseñado para Ubuntu/Debian y requiere Google Chrome para abrir los enlaces.

Librerías de Sistema (Obligatorias):
Necesitas instalar los bindings de Python para las notificaciones y D-Bus:

sudo apt update
sudo apt install python3-notify2 python3-dbus python3-gi google-chrome-stable



Librerías de Python:
Instala las dependencias del proyecto:

pip3 install -r requirements.txt



⚙️ Configuración (config.json)

Crea o edita el archivo config.json en la misma carpeta:

{
    "nitter_host": "[https://rsshub.pseudoyu.com/twitter](https://rsshub.pseudoyu.com/twitter)",
    "tiempo_espera": 300,
    "users": {
        "HernanSCastillo": [],
        "ElonMusk": ["Mars", "Starship"],
        "Ubuntu": ["LTS", "security"],
        "FabricioRomano": ["Boca", "River"]
    }
}



nitter_host: URL de la instancia RSSHub (se recomienda mantener la del ejemplo).

tiempo_espera: Segundos entre cada ciclo de búsqueda (300s = 5 min).

users:

[] (Lista vacía): Notifica todo (menos Retweets, que se filtran siempre).

["palabra"]: Filtra y solo notifica si el tweet contiene alguna de las palabras.

▶️ Uso

Ejecución básica (Pruebas)

Mantén la terminal abierta para ver los logs:

python3 x-monitor.py



Ejecución en Segundo Plano (Recomendado)

Para dejarlo corriendo "para siempre" aunque cierres la terminal:

nohup python3 x-monitor.py >/dev/null 2>&1 &



Detener el Script ("Matar" el proceso)

Si lo corriste en segundo plano y quieres detenerlo:

pkill -f x-monitor.py



🔧 Solución de Problemas Frecuentes

Error ImportError: Asegúrate de haber ejecutado el comando sudo apt install ... mencionado en los requisitos.

No abre el navegador: El script busca el ejecutable google-chrome. Asegúrate de tenerlo instalado.

Notificaciones no clicables: Asegúrate de estar usando un entorno de escritorio compatible (GNOME, KDE, XFCE) y que el servicio de notificaciones esté activo.

Hecho para correr en segundo plano en tu Ubuntu.