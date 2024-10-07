print('Digite o valor da sua hora de trabalho em Reais')
valor = float(input())

print('Agora o numero de horas trabalhadas no mês')
numero = float(input())

total = (valor * numero) * 1.10
print(f' O valor a ser pago adicionado 10% é {round(total)}')

