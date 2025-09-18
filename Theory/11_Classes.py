### Clases ###
# Una clase es una plantilla para crear objetos. Los objetos son instancias de una clase.
# Las clases encapsulan datos y funcionalidades relacionadas.
# Se usan para modelar entidades del mundo real y organizar el código de manera modular.

class Persona:
    def __init__(self,nombre,apellido,alias = "Sin alias"): #Método constructor. Lo que hace falta para crear una instancia de la clase
        self.nombre = nombre
        self.apellido = apellido
        self.alias = alias
    
    def walk(self): #Método de la clase
        return f"{self.nombre} está caminando"

my_person = Persona("Juan","Pérez") #Instancia de la clase Persona
print(my_person.nombre)
print(my_person.walk())
print(my_person.alias) #Si no se pasa el alias, toma el valor por defecto "Sin alias"
my_person.alias = "Juancho" #Puedo cambiar el valor. Sin embargo, no es una buena práctica cambiar atributos directamente. La mejor práctica es usar métodos.
print(my_person.alias)

class Vehiculo:
    def __init__(self,marca,modelo,año,encendido = False):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = encendido
    
    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            return "El vehículo ha arrancado"
        else:
            return "El vehículo ya está encendido"
    
    def apagar(self):
        if self.encendido:
            self.encendido = False
            return "El vehículo se ha apagado"
        else:
            return "El vehículo ya está apagado"
    
    def estado(self):
        estado = "encendido" if self.encendido else "apagado" #estado es una variable temporal
        return f"El vehículo {self.marca} {self.modelo} del {self.año} está {estado}"

mi_vehiculo = Vehiculo("Toyota","Corolla",2020)
print(mi_vehiculo.estado())
print(mi_vehiculo.arrancar())
print(mi_vehiculo.estado())
print(mi_vehiculo.apagar())

# Herencia. Permite crear una nueva clase basada en una clase existente.
class Coche(Vehiculo): #Coche hereda de Vehiculo
    def __init__(self,marca,modelo,año,encendido = False,puertas = 4):
        super().__init__(marca,modelo,año,encendido) #Llama al constructor de la clase padre
        self.puertas = puertas #Nuevo atributo específico de la clase Coche
    
    def estado(self): #Sobrescribe el método estado de la clase padre
        estado = "encendido" if self.encendido else "apagado"
        return f"El coche {self.marca} {self.modelo} del {self.año} con {self.puertas} puertas está {estado}"
    


mi_coche = Coche("Honda","Civic",2019,puertas=2)
print(mi_coche.estado())
print(mi_coche.arrancar()) #Hereda el método arrancar de la clase Vehiculo
print(mi_coche.estado())

# Polimorfismo. Permite usar una interfaz común para diferentes tipos de datos. Deben tener el mismo método.
print(mi_vehiculo.estado()) #Vehiculo
print(mi_coche.estado()) #Coche 
# Ambos tienen el método estado(), pero se comportan de manera diferente según la clase. 

# Encapsulamiento. Restringe el acceso directo a algunos componentes del objeto.
class CuentaBancaria:
    def __init__(self,titular,saldo=0):
        self.titular = titular
        self.__saldo = saldo #Atributo privado. No se puede acceder directamente desde fuera de la clase   
        # Se deber usar métodos para interactuar con él. Como getters y setters.
# Getter
    def get_saldo(self):
        return self.__saldo
# Setter
    def depositar(self,monto):
        self.__saldo += monto

# __Str__ Método especial para modificar la representación en string del objeto
    def __str__(self):
        return f"Cuenta de {self.titular} con saldo {self.__saldo}"
    #Sin este método, al imprimir el objeto, se mostraría algo como <__main__.CuentaBancaria object at 0x...>
    #Con este método, se muestra una representación más amigable.
mi_cuenta = CuentaBancaria("Ana",1000)
print(mi_cuenta) #Usa el método __str__
print(mi_cuenta.get_saldo()) #Usa el getter para acceder al saldo
mi_cuenta.depositar(500) #Usa el setter para modificar el saldo
print(mi_cuenta.get_saldo())
#print(mi_cuenta.__saldo) #Error. No se puede acceder directamente al atributo privado

#Metodos de clase y estáticos
class Avion:
    contador_aviones = 0 #Atributo de clase. Compartido por todas las instancias de la clase

    def __init__(self,modelo):
        self.modelo = modelo
        Avion.contador_aviones += 1 #Incrementa el contador cada vez que se crea una nueva instancia

    @classmethod
    def cantidad_aviones(cls): #Método de clase. Recibe la clase como primer argumento
        return f"Hay {cls.contador_aviones} aviones"
    
    @classmethod
    def crear_avion(cls,modelo): #Método de clase que actúa como una fábrica para crear aviones
        return cls(modelo) #Otra forma de crear una instancia de la clase

    @staticmethod
    def info(): #Método estático. No recibe ni la instancia ni la clase como primer argumento
        return "Los aviones son vehículos aéreos diseñados para el transporte de personas o carga."
# No es necesario crear una instancia de la clase para usar estos métodos
# Se usan para funciones que tienen relación con la clase pero no necesitan acceder a atributos o métodos de instancia.
# Los metódos estáticos son útiles para agrupar funciones relacionadas con la clase solo por organización.
print(Avion.info()) #Llama al método estático
# Los métodos de clase son útiles para operaciones que afectan a la clase en su conjunto.
print(Avion.cantidad_aviones()) #Llama al método de clase
avion1 = Avion.crear_avion("Boeing 747") #Crea una instancia usando el método de clase
print(Avion.cantidad_aviones())

#@property. Permite usar métodos como si fueran atributos.
class Rectangulo:
    def __init__(self,ancho,alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self): #Método que calcula el área. Se usa como un atributo.
        return self.ancho * self.alto

    @property
    def perimetro(self): #Método que calcula el perímetro. Se usa como un atributo.
        return 2 * (self.ancho + self.alto)
    
mi_rectangulo = Rectangulo(5,10)
print(f"Área: {mi_rectangulo.area}") #No se usan paréntesis.
print(f"Perímetro: {mi_rectangulo.perimetro}") #No se usan paréntesis.

#Se puden usar como getters y setters de atributos privados.
class Circulo:
    def __init__(self,radio):
        self.__radio = radio #Atributo privado

    @property
    def radio(self): #Getter
        return self.__radio

    @radio.setter
    def radio(self,valor): #Setter. Se puede implementar lógica de validación.
        if valor > 0:
            self.__radio = valor
        else:
            print("El radio debe ser positivo")

mi_circulo = Circulo(5)
print(mi_circulo.radio) #Usa el getter
mi_circulo.radio = 10 #Usa el setter
print(mi_circulo.radio)
mi_circulo.radio = -3 #Intenta usar el setter con un valor inválido

#Buenas prácticas:
# Usar nombres descriptivos para clases, métodos y atributos.
# Seguir la convención de nomenclatura (CamelCase para clases, snake_case para métodos y atributos).
# Mantener las clases enfocadas en una sola responsabilidad.
# Usar herencia y composición de manera adecuada.
# Documentar las clases y métodos con docstrings.
# Evitar el uso excesivo de atributos y métodos públicos.
# Usar propiedades para controlar el acceso a atributos privados.

