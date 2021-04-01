#10.Escreva um programa que pergunte o valor inicial de uma dívida e o juros mensal. Pergunte também o valor mensal 
# que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros a pago.
valordivida= float(input("Qual o valor inicial?\n"))
taxajuros = float(input("Qual o juros mensal?\n"))
pagamentomensal= float(input("Quanto será pago por mês?\n"))
parcela=0
juros=0
valorfinal = 0
totaldejuros=0

while valordivida >= pagamentomensal:
    
    juros = (taxajuros/100) * pagamentomensal
    parcela += 1
    
    valordivida = valordivida-pagamentomensal + juros
    valorfinal= parcela*pagamentomensal
    
    if valordivida > 0:
        valordivida2 = valordivida +(valordivida*taxajuros/100)
        parc2 = parcela + 1
if valordivida2 > pagamentomensal:
    parc2 +=1
    residual=valordivida2-parcela
    residual = residual+(residual*taxajuros/100)
    valordivida2 = 0
else:
    residual = 0
    
valorfinal=valorfinal+valordivida+residual

print("A dívida será paga em {} meses.".format(parc2))
print("O total a pagar será R${}".format(valordivida2-valordivida+valorfinal))
print("O valor total de juros será R${}.".format(juros*parcela+valordivida2-valordivida+residual))