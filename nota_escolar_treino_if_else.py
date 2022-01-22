#-*- coding:utf-8 -*-
nota1 = float(input("Digite a nota do primeiro trimestre:"))
nota2 = float(input("Digite a nota do segundo trimestre:"))
nota3 = float(input("Digite a nota do terceiro trimestre:"))

media = (nota1+nota2+nota3)/2

if media <=7:
    print("Reprovado")
else:
    print("Aprovado")