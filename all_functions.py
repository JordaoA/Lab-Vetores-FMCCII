#coding: utf-8
#Forma que todos os dados se organizam dentro do arquivo: id_proposicao,id_votacao,id_deputado,voto,partido.
#Possibilidade de votos: Não" = -1, "Faltou" = 0, "Sim" = 1, "Obstrução" = 2, "Abstenção" = 3, "Art. 17" = 4
"""
Extrategia: dicionario que guarda uma tupla, onde seu primeiro valor sera outro dicionario (que possui 
como chave o id de cada proposição votada por ele e seu valor como o voto) e no segundo o seu partido.
"""
#função auxiliar para tratar cada dataset para colocalos de forma organizada no dicionario dinal
def aux_build_dic(arq,votos):
	#Tratando arquivos
	arq = arq.split()
	for i in range(len(arq)):
		arq[i] = arq[i].split(",")

	#Trabalhando em cima da matriz para transforma-la em um dicionario
	for i in range(1,len(arq)-1):
		if arq[i][2] in votos:
			#checando se a proposição atual ja esta inclusa no dicionario de proposições do deputado.
			if arq[i][0] not in votos[arq[i][2]][0]:
				votos[arq[i][2]][0][arq[i][0]] = arq[i][3]
		else:
			"""
			guardando tupla que recebe em seu primeiro valor um dicionario que guarda o voto do deputado
			em determinada lei e no segundo, guarda o seu partido 
			"""
			votos[arq[i][2]] = ({arq[i][0]:arq[i][3]},arq[i][4])

#id_proposicao,id_votacao,id_deputado,voto,partido.	
#funcao que cria dicionario a partir dos datasets fornecidos
def build_Dic():
	#dicionario final
	votos = {}

	#definindo caminho para datasets
	path2015 = "data/votacoes_2015.csv"
	path2016 = "data/votacoes_2016.csv"
	path2017 = "data/votacoes_2017.csv"
	path2018 = "data/votacoes_2018.csv"
	
	#abrindo arquivos
	arq2015 = open(path2015,"r")
	arq2016 = open(path2016,"r")
	arq2017 = open(path2017,"r")
	arq2018 = open(path2018,"r")

	#usando função auxiliar para alterar dicionario
	aux_build_dic(arq2015.read(),votos)
	aux_build_dic(arq2016.read(),votos)
	aux_build_dic(arq2017.read(),votos)
	aux_build_dic(arq2018.read(),votos)

	#fechando arquivos
	arq2015.close()
	arq2016.close()
	arq2017.close()
	arq2018.close()

	return votos

votos_dict = build_Dic()

#Coleta votos e agrupa todos em uma unica lista
def coleta_votos(id_deputado,votos_dict):
	vector = []
	for i in votos_dict:
		if i == id_deputado:
			for i in votos_dict[id_deputado][0]:
				vector.append(votos_dict[id_deputado][0][i])
			break
	return vector

#Não" = -1, "Faltou" = 0, "Sim" = 1, "Obstrução" = 2, "Abstenção" = 3, "Art. 17" = 4
#1ra questao
#*Considerando que os dois congressistas tem o mesmo numero de votos.*
def compare(congress_id1, congress_id2, votos_dict):
	#vetores que com os votos dos dois deputados
	vector_congress_1 = coleta_votos(congress_id1,votos_dict)
	vector_congress_2 = coleta_votos(congress_id2,votos_dict)
	#vetor que sera usado para calcular a similaridade entre os dois deputados.
	result_vector = []
	similaridade = 0.0
	for i in range(len(vector_congress_1)):
		"""
		Adicionarei uma condicional para o caso dos elementos em mesmas posições do vetor sejam diferentes.
		Pois com esse tipo de avaliação, teremos uma precisão maior de similaridade, que podera ser 
		representada por numeros positivos e negativos.
		"""
		if vector_congress_1[i] == vector_congress_2[i]:
			result_vector.append(1)
		#Tratando casos em que os votos não são iguais, mas se aproximam (na minha opnião) de alguma forma.
		else:
			if vector_congress_1[i] == "1" and vector_congress_2[i] == "3" or vector_congress_1[i] == "3" and vector_congress_2[i] == "1":
				result_vector.append(0.5)
			elif vector_congress_1[i] == "-1" and vector_congress_2[i] == "2" or vector_congress_1[i] == "2" and vector_congress_2[i] == "-1":
				result_vector.append(0.5)
			else:
				result_vector.append(-1)

	#Somando elementos do vetor resultante
	for i in result_vector:
		similaridade += i

	return similaridade

#2da Questao
def most_similar(congress_id, votos_dict):
	id_deputado = 0
	maior_similaridade = -99999999

	for i in votos_dict:
		similaridade = -99999999
		#Condicional para garantir que o deputado não sera comparado com ele mesmo
		if i != congress_id:
			similaridade = compare(congress_id,i,votos_dict)

		if similaridade > maior_similaridade:
			id_deputado = int(i)
			maior_similaridade = similaridade

	return id_deputado

#3ra questao
def least_similar(congress_id, votos_dict):
	id_deputado = 0
	menor_similaridade = 99999999

	for i in votos_dict:
		similaridade = compare(congress_id,i,votos_dict)
		
		if similaridade < menor_similaridade:
			id_deputado = int(i)
			menor_similaridade = similaridade

	return id_deputado