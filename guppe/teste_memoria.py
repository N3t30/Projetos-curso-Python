"""
teste de memoria com generators

sequencia de fibonacci
1, 1, 2, 3, 5, 8, 13...


# teste
for n in fib_lista(50):
    print(n)
"""

# função usando listas 449mb
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Função usando geradores  3mb

def fib_gem(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1


for n in fib_gem(50):
    print(n)