def calcular_mcd(a, b):
    """
    Esta función calcula el máximo común divisor (MCD) entre dos números utilizando el algoritmo de Euclides.
    """
    while b != 0:
        a, b = b, a % b
    return a


mcd = calcular_mcd(2, 10) 
print(mcd) 

def calcular_mcm(a, b): 
    """ Esta función calcula el mínimo común múltiplo (mcm) entre dos números utilizando el algoritmo de Euclides. """ 
    mcd = calcular_mcd(a, b) 
    return (a * b) / mcd

mcm = calcular_mcm(2, 10) 
print(mcm) 


def contar_palabras(cadena):
     """ Esta función recibe una cadena de caracteres y devuelve un diccionario con la frecuencia de cada palabra en la cadena. """ 
     palabras = cadena.split() # Separa la cadena en palabras 
     frecuencia = {} 
     for palabra in palabras: 
        if palabra in frecuencia: 
            frecuencia[palabra] += 1 
        else: 
            frecuencia[palabra] = 1 
     return frecuencia

cadena = "Codo a Codo - Curso Django 2023 - comision 23316 - 23316" 
frecuencia = contar_palabras(cadena) 
print(frecuencia) # Imprime {'Hola': 1, 'mundo': 3, 'hola': 2, 'HOLA': 1}