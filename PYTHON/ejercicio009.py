# programa que verifica si una palabra es palindromo

palabra = input('Ingrese una palabra para verificar si es palindromo \n')

# print('1 '+palabra)
# print('2 '+palabra[::-1])

if(palabra == palabra[::-1]):
    print('palindromo')
else:
    print('no es palindromo')