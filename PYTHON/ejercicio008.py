"""
STRING y mas!!!!!
"""

esto_es_una_string = "hola wilmer alava como estas"
esto_es_una_otra_string = "Mundo"

# concatenar
print(esto_es_una_string + ' ' + esto_es_una_otra_string)
# hola mundo
 
 # MAYUS
print(esto_es_una_string.upper())
 # minus
print(esto_es_una_string.lower())
 # Primeraen mayus
print(esto_es_una_string.capitalize())
 # Pone en mayus la primera letra de cada palabra
print(esto_es_una_string.title())
 # me dice la longitud del string
print(len(esto_es_una_string.lower()))

#buscar un caracter y muestra su ubicación en indice
print(esto_es_una_string.find('e'))



# rebanar!!!!!! o slice
print(esto_es_una_string[0:2])  # ho tu le dices que inicie en cero
print(esto_es_una_string[:2])  # ho el asume que inicia en cero
print(esto_es_una_string[5:11])

#radar
variable = 'radar'
print(variable[::])
print(variable[::-1])