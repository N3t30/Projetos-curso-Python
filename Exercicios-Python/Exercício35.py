import math

print('considerando ''A'' e ''B'' os catetos de um triangulo.')

print(' digite o cateto ''A'' ')
a = float(input())

print('digite o cateto ''B''')
b = float(input())

hip = math.sqrt(a ** 2 + b ** 2)

print(f' a hipotenusa é {round(hip)}')

