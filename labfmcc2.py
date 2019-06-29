#UFCG - Campina Grande
#Autor: Franciclaudio Dantas da Silva
#Matricula: 118210343
#Disciplina: Fundamentos Matematicos para Ciencia da Computacao II
#Professor: Thiago Emmanuel

#----------------SETUP-------------------
dict1 = {1: [-1, -1, 1], 2: [1,0,1], 3: [1,1,1]}
dict2 = {1: [1, 1, 1], 2: [1,1,1]}
dict3 = {1: [0,-1,0], 2: [0,0,0]}
dict4 = {1: [-1,-1,-1], 2: [1,1,1]}

#---------------PROBLEMA 1---------------
def compare(congress_id1, congress_id2, votos_dict):
	array1 = []
	array2 = []
	
	for e in votos_dict:
		if e == congress_id1:
			array1 = votos_dict[e];
		if e == congress_id2:
			array2 = votos_dict[e];
	
	result = 0.0;
	
	for i in range(0, len(array1)):
		if (array1[i]==array2[i]):
			result += 1
		elif (array1[i] == 0 or array2[i] == 0):
			result += 0.333

	return result

print(compare(1, 2, dict1))
print(compare(1, 2, dict2))
print(compare(1, 2, dict3))
print(compare(1, 2, dict4))

#---------------PROBLEMA 2---------------
def most_similar(congress_id, votos_dict):
	idMaisSimilar = 0
	similaridade = 0
	
	for x in votos_dict:
		if compare(votos_dict[congress_id], x, votos_dict) >= similaridade:
			idMaisSimilar = x
			similaridade = compare(votos_dict[congress_id], x, votos_dict)
	
	return idMaisSimilar

print(most_similar(1, dict1))

#---------------PROBLEMA 3---------------
def least_similar(congress_id, votos_dict):
	idMenosSimilar = 0
	similaridade = compare(votos_dict[congress_id], 1, votos_dict)
	
	for x in votos_dict:
		if compare(votos_dict[congress_id], x, votos_dict) <= similaridade:
			idMenosSimilar = x
			similaridade = compare(votos_dict[congress_id], x, votos_dict)
	
	return idMenosSimilar
	
print(least_similar(1, dict1))

#---------------PROBLEMA 4---------------

#---------------PROBLEMA 5---------------

#---------------PROBLEMA 6---------------

#---------------PROBLEMA 7---------------

#---------------PROBLEMA 8---------------

#---------------PROBLEMA 9---------------
