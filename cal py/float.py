nota1 = print ("qual sua nota1")
nota2 = print ("qual sua nota2")
nota3 = print ("qual sua nota3")

nota1 = float(input("nota 1:"))
nota2 = float(input("nota 2:"))
nota3 = float(input("nota 3:"))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print ("Recuperação")
else:
    print("Reprovado")