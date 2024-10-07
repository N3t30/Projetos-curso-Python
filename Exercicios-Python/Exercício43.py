print('valor do produto')
valorp = float(input())

valor10 = valorp - (valorp * 0.10)
valor3x = valorp / 3
comissão =  valor10 * 0.05
comissão2 = valorp * 0.05

print(f'O valor total com o desconto de 10% é {valor10}')
print(f' O valor parcelado em três vezes sem juros é de {round(valor3x)}')
print(f' A comissão do vendedor se o pagamento for a vista é {comissão}')
print(f' E se o pagamento for parcelado a comissão é {comissão2}')