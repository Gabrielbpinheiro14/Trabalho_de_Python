pesoLimite = 50
peso = float(input("Digite a quantidade de kgs de peixe: "))
if peso > pesoLimite:
    excesso = peso - pesoLimite
    multa = excesso * 4.00
    print ("Multa foi de " + str(multa) + " reais")