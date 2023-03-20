#6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes 
#métodos para la clase:
#-Un constructor, donde los datos pueden estar vacíos.
#-Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#-mostrar(): Muestra los datos de la persona.
#-Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("La edad debe ser un número positivo")
    
    def get_dni(self):
        return self.dni
    
    def set_dni(self, dni):
        if len(dni) == 8:
            self.dni = dni
        else:
            print("El DNI debe tener 8 caracteres")
    
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)
        
    def es_mayor_de_edad(self):
        return self.edad >= 18
    
p1 = Persona()
p1.set_nombre("Hugo")
p1.set_edad(36)
p1.set_dni("12345678")

p2 = Persona()
p2.set_nombre("Maria")
p2.set_edad(15)
p2.set_dni("87654321")

p1.mostrar() 
print(p1.es_mayor_de_edad()) 
print("")
p2.mostrar() 
print(p2.es_mayor_de_edad())
print("")


#7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
# titular (que es una persona) y cantidad (puede tener decimales). 
# El titular será obligatorio y la cantidad es opcional. 
# Crear los siguientes métodos para la clase: 
# -Un constructor, donde los datos pueden estar vacíos. 
# -Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente,
#  sólo ingresando o retirando dinero. 
# -mostrar(): Muestra los datos de la cuenta. 
# -ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, 
# no se hará nada. 
# -retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad
        
    def get_titular(self):
        return self.titular
    
    def get_cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        print("Titular:", self.titular.get_nombre())
        print("Cantidad:", self.__cantidad)
        
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
        
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad


p = Persona("Hugo", 36, "12345678")
c = Cuenta(p, 10000)
c.ingresar(5000)
c.retirar(4000)
c.mostrar() 


#8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven 
# que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular 
# y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. 
# Crear los siguientes métodos para la clase: 
# -Un constructor. 
# -Los setters y getters para el nuevo atributo. 
# -En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, 
# por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si 
# el titular es mayor de edad pero menor de 25 años y falso en caso contrario. 
# -Además, la retirada de dinero sólo se podrá hacer si el titular es válido. 
# -El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=10):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    # Setter y getter para la bonificación
    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self.__bonificacion
    
    # Método para comprobar si el titular es válido
    def es_titular_valido(self):
        edad = self.get_titular().get_edad()
        return edad >= 18 and edad < 25
    
    # Redefinición del método retirar para comprobar si el titular es válido
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No se puede retirar dinero de una cuenta joven con un titular no válido")
    
    # Redefinición del método mostrar para incluir la bonificación
    def mostrar(self):
        super().mostrar()
        print(f"Cuenta Joven con una bonificación del {self.__bonificacion}%")


print("")
p3 = Persona("Julio", 22, "10101010")
c1 = CuentaJoven(p3, 100000)
c1.ingresar(10000)
c1.retirar(50000)
c1.mostrar() 

print("")
p4 = Persona("Ana", 20, "19876543")
c2 = CuentaJoven(p4, 5000)
c2.ingresar(1000)
c2.retirar(3500)
c2.mostrar() 