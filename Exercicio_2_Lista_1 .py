#defini uma variavel para o peso e uma para o peso limite, se o peso fosse maior que o limite ele mostraria a multa, senao informaria a nao necessidade de pagamento de multa

pesoLimite = 50
peso = float(input("Digite a quantidade de kgs de peixe: "))
if peso > pesoLimite:
    excesso = peso - pesoLimite
    multa = excesso * 4.00
    print ("Multa foi de " + str(multa) + " reais")
