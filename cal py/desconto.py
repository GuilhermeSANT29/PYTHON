valor = float(input("digite o valor da compra: "))
vip = input("cliente VIP? (sim/nao)")

if vip == "sim" and valor >= 100:
    desconto = valor * 0.2
elif valor >= 100:
    desconto = valor * 0.1
else:
    desconto = 0

valor_final = valor - desconto

print("desconto:", desconto)
print('valor final: ', valor_final)