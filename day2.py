
# ==============================================================================================================

#Este programa farao calculo de uma mesa com gorjeta e o valor para cada pessoa que pagara
print("")
print("")
print("")
print("Bem vindo !!\nEste é um programa feito para calcular a conta da mesa ...")
print("")
#Colecionamos os valores de entrada atribuindo a melhora forma para que não seja armazanada como string 
total = float(input("Qual foi o total na conta da mesa ? "))
gorjeta = int(input("Qual a porcentagem de gorjeta gostaria de dar ? 10, 15 ou 30 ... ?  "))
print(f"Você deixara o total de {gorjeta}% de gorjeta ...")
raxar = int(input("Quantas pessoas  irão dividir essa conta ?"))
gorjeta_porct = gorjeta / 100
valor_cash = total * gorjeta_porct
totalconta = float(valor_cash) + total
conta_final = totalconta / raxar
one = round(conta_final,2)
one = "{:.2f}".format(one)
#finish = round(one,2)
print("")
print(f"Cada pessoa pagará o valor de : ${one} ")

print("")
print("")
print("")




