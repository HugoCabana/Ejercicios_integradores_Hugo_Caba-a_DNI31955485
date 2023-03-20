#1. Escribir una función que calcule el máximo común divisor entre dos números.

def calcular_mcd(a, b):
    """
    Esta función calcula el máximo común divisor (MCD) entre dos números utilizando el algoritmo de Euclides.
    """
    while b != 0:
        a, b = b, a % b
    return a


mcd = calcular_mcd(72, 108) 
print(mcd)
print("") 

#2. Escribir una función que calcule el mínimo común múltiplo entre dos números

def calcular_mcm(a, b): 
    """ Esta función calcula el mínimo común múltiplo (mcm) entre dos números utilizando el algoritmo de Euclides. """ 
    mcd = calcular_mcd(a, b) 
    return (a * b) / mcd

mcm = calcular_mcm(72, 108) 
print(mcm)
print("") 

# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra 
#  que contiene y la cantidad de veces que aparece (frecuencia).

def contar_palabras(cadena):
     """ Esta función recibe una cadena de caracteres y devuelve un diccionario con la frecuencia de cada
        palabra en la cadena. 
    """ 
     palabras = cadena.split() # Separa la cadena en palabras 
     frecuencia = {} 
     for palabra in palabras: 
        if palabra in frecuencia: 
            frecuencia[palabra] += 1 
        else: 
            frecuencia[palabra] = 1 
     return frecuencia

cadena = "Python Codo a Codo Curso Django Python 2023 comision 23316 23316 Python python" 
frecuencia = contar_palabras(cadena) 
print(frecuencia)
print("")


# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada 
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función que
#   reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más 
#  repetida y su frecuencia.

def palabra_mas_repetida(frecuencia):
    """
    Esta función recibe un diccionario con la frecuencia de cada palabra y devuelve una tupla con la 
    palabra más repetida y su frecuencia.
    """
    palabra = max(frecuencia, key=frecuencia.get)
    frecuencia_max = frecuencia[palabra]
    return (palabra, frecuencia_max)

frecuencia = contar_palabras(cadena) 
palabra, frecuencia_max = palabra_mas_repetida(frecuencia)
print(palabra, frecuencia_max)