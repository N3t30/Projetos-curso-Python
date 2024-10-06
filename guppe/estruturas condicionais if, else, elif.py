'''
estruturas condicionais
 if(se), else(se não), elif
'''
print(' digite sua idade')
idade = float(input())

if idade < 18:
    print('menor de idade')
elif idade == 18:
    print('voce tem 18')
else:
    print('maior de idade')
