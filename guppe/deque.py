'''
Modulo collections - deque
podemos dizer que o deque é uma lista de alta perfomace
'''
# inport
from collections import deque
# Criando deques
deq = deque('neto')
print(deq)

deq.append('p') # adiciona ao final
print(deq)

deq.appendleft('josé') #@ adiciona ao começo
print(deq)

deq.pop() # Remove retorna o ultimo elemento
print(deq)

print(deq.popleft()) # Remove e retorna o primero elemneto

print(deq)