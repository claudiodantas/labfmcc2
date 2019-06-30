import csv

#arquivo = open(r'C:\Python27\data\raw', 'r')
#linhas = csv.reader(arquivo)

#UFCG - Campina Grande
#Autor: Franciclaudio Dantas da Silva
#Matricula: 118210343
#Disciplina: Fundamentos Matematicos para Ciencia da Computacao II
#Professor: Thiago Emmanuel

#----------------SETUP-------------------
dict1 = {1: [-1,1,1], 2: [1,0,1], 3: [1,1,1], 4:[1,0,1], 5:[-1,-1,-1]}
dict2 = {1: [1, 1, 1], 2: [1,1,1]}
dict3 = {1: [0,-1,0], 2: [0,0,0]}
dict4 = {1: [-1,-1,-1], 2: [1,1,1]}

#Se o produto interno for igual a 1 = concordam
#Se for igual a -1 = discordam
#Se for igual a 0 = abstencao
#Soma positiva indica que eles concordam e uma negativa discordam
#---------------PROBLEMA 1---------------
def compare(congress_id1, congress_id2, votos_dict):
	array1 = []
	array2 = []
	
	for e in votos_dict:
		if e == congress_id1:
			array1 = votos_dict[e];
		if e == congress_id2:
			array2 = votos_dict[e];

	result = 0;
	
	for i in range(len(array1)):
		if (array1[i] == 0 and array2[i] == 0):
			result += 1
		else:
			result += array1[i] * array2[i]

	return result

print(compare(2, 4, dict1))
print(compare(2, 5, dict1))
print(compare(1, 2, dict2))
print(compare(1, 2, dict3))
print(compare(1, 2, dict4))

#---------------PROBLEMA 2---------------
def most_similar(congress_id, votos_dict):
	idMaisSimilar = 0
	similaridade = 0
	
	primeiro = True
	for x in votos_dict:
		if (x == congress_id):
			continue
		elif primeiro:
			similaridade = compare(congress_id, x, votos_dict)
			idMaisSimilar = x
			primeiro = False
		elif compare(congress_id, x, votos_dict) >= similaridade:
			similaridade = compare(congress_id, x, votos_dict)
			idMaisSimilar = x
	
	return idMaisSimilar

print(most_similar(1, dict1))

#---------------PROBLEMA 3---------------
def least_similar(congress_id, votos_dict):
	idMenosSimilar = 0
	similaridade = 0
	
	primeiro = True
	for x in votos_dict:
		if (x == congress_id):
			continue
		if primeiro:
			similaridade = compare(congress_id, 1, votos_dict)
			idMenosSimilar = x
			primeiro = False
		if compare(congress_id, x, votos_dict) <= similaridade:
			idMenosSimilar = x
			similaridade = compare(congress_id, x, votos_dict)
	
	return idMenosSimilar
	
print(least_similar(2, dict1))

#---------------PROBLEMA 4---------------

#---------------PROBLEMA 5---------------
def average_similarity(congress_id, congress_set, votos_dict):
	media = 0.0
	soma = 0.0
	
	for x in congress_set:
		soma += compare(congress_id, x, votos_dict)
	
	media = soma/len(congress_set)
	
	return "%.2f" %media

print (average_similarity(1, {2, 3, 4}, dict1))

def least_similar_partido(congress_set, votos_dict):
	similaridade = 0.0
	diferentao = 0
	primeiro = True
	
	for x in congress_set:
		if primeiro:
			similaridade = average_similarity(x, congress_set, votos_dict)
			diferentao = x
			primeiro = False
		else:
			if average_similarity(x, congress_set, votos_dict) < similaridade:
				similaridade = average_similarity(x, congress_set, votos_dict)
				diferentao = x
	
	return diferentao

print (least_similar_partido({2,3,4},dict1))

#---------------PROBLEMA 6---------------
def pair_seem(votos_dict):
	parecidos = {}
	ids = ""
	
	for x in votos_dict:
		parecidos[x] = most_similar(x, votos_dict)
		
	similaridade = 0
	primeiro = True
	for y in parecidos:
		if primeiro:
			similaridade = compare(y, parecidos[y], votos_dict)
			ids = "%d e %d" %(y, parecidos[y])
			primeiro = False
		else:
			if compare(y, parecidos[y], votos_dict) >= similaridade:
				similaridade = compare(y, parecidos[y], votos_dict)
				ids = "%d e %d" %(y, parecidos[y])

	return ids

print(pair_seem(dict1))

#---------------PROBLEMA 7---------------
def pair_different(votos_dict):
	diferentes = {}
	ids = ""
	
	for x in votos_dict:
		diferentes[x] = least_similar(x, votos_dict)
		
	similaridade = 0
	primeiro = True
	for y in diferentes:
		if primeiro:
			similaridade = compare(y, diferentes[y], votos_dict)
			ids = "%d e %d" %(y, diferentes[y])
			primeiro = False
		else:
			if compare(y, diferentes[y], votos_dict) <= similaridade:
				similaridade = compare(y, diferentes[y], votos_dict)
				ids = "%d e %d" %(y, diferentes[y])

	return ids

print(pair_different(dict1))

#---------------PROBLEMA 8---------------

#---------------PROBLEMA 9---------------
