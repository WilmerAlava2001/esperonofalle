import math

radio = int(input('Ingrese el radio del circulo : \t'))

area = math.pi * (radio*radio)
perimetro = 2 * math.pi * radio

print(f'El area del circulo es : {area}')
print(f'El perimetro del circulo es : {perimetro}')
