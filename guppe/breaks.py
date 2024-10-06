'''
saindo de loops com breaks
funciona da msm forma que as outras linguagens
utilizamos o break para sairmos de loops para sair de maneira froçada
'''
# Exemplo 1
for numero in range(1, 11):
     if numero == 10:
         break
     else:
         print(numero)
print('loop parado')

# Exemplo 2
while True:
    comando = input("Digite 'sair' para sair.")
    if comando == 'sair':
        break


