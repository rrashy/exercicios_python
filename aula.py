# -*- coding:utf-8 -*-

nome_1 = "Nícolas" #string com aspas armazena caracteres | sem aspas se torna um numeral
nome_2 = "Helena"
idade_1 = 18
idade_2 = 19
endereço = "argentina flores da rosa"

usuario_1 = nome_1 + " e " + nome_2 + "\n" #concatenamçao (mesclagem string ou soma)
tamanho = len(usuario_1) #contagem de caracteres -> print(tamanho ou nome da variavel)
utilidade = endereço.split("a") #tira letra especifica da string inteira
search = endereço.find("flores") #serve para achar posição da substring
endereço = endereço.replace("flores","cravos") #substitui uma string por outra 
#print(endereço[search:]) #serve para mostrar string apenas apartir da substring


#colchetes mostra a letra de acordo com a contagem da string exemplo: 4ª letra da string "Helena" é >n< || OBS: na computação a contagem começa do 0 (zero) 
#print(nome_2[0]) #H
#print(nome_2[1]) #e
#print(nome_2[2]) #l
#print(nome_2[3]) #e
#print(nome_2[4]) #n
#print(nome_2[5]) #a

#print(usuario_1[0:12]) #dessa forma pode ser feita a sequencia da string até o numero determinado | tambem pode ser feito de qualquer forma ex: [4:12] apartir da 4ª letra da string até a 12ª

#print(usuario_1.lower()) # deixa as letras da string em minusculo
#print(usuario_1.upper()) #deixa as letras da string em maiusculo
#print(usuario_1.strip()) #remove a quebra de linhas e espaços


#dessa forma a string adota o valor -> maiusculo ou minusculo
#usuario_1 = usuario_1.upper()
#print(usuario_1)

