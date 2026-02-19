name = input ("digite seu nome")
age = int(input("digite sua idade"))

print ("Hello!,", name)
if age >= 18:
        print ("voce e maior de idade")
else:
    age = 18 - age
    print ("voce e menor de idade, e faltam,", age, " anos para maior idade")