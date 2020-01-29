#coding: utf-8
#Forma que todos os dados se organizam dentro do arquivo: id_proposicao,id_votacao,id_deputado,voto,partido.
#Possibilidade de votos: Não" = -1, "Faltou" = 0, "Sim" = 1, "Obstrução" = 2, "Abstenção" = 3, "Art. 17" = 4
"""
Extrategia: dicionario que guarda uma tupla, onde seu primeiro valor sera outro dicionario (que possui 
como chave o id de cada proposição votada por ele e seu valor como o voto) e no segundo o seu partido.
"""
import utils.csvToDict as buildDic

votos_dict = buildDic.build_Dic()
#ids para test ~ 178957 / 141417
#Coleta votos e agrupa todos em uma unica lista
def coleta_votos(id_deputado,votos_dict):
	vector = []
	for i in votos_dict:
		if i == id_deputado:
			
			#formatação do dict votos[idDeputado] = ({leiVotada:tipoDeVoto},partido)
			for i in votos_dict[id_deputado][0]: 
				vector.append((votos_dict[id_deputado][0][i],i))
							   #voto                         #proposição		
			break

	return vector

#1ra questao
def compare(congress_id1, congress_id2, votos_dict):
	#vetores que com os votos dos dois deputados
	vectorCongressMan1 = coleta_votos(str(congress_id1),votos_dict)
	vectorCongressMan2 = coleta_votos(str(congress_id2),votos_dict)
	#vetor que sera usado para calcular a similaridade entre os dois deputados.
	similaridade = 0.0
	
	for i in range(len(vectorCongressMan1)):
		"""
		Adicionarei uma condicional para o caso dos elementos em mesmas posições do vetor sejam diferentes.
		Pois com esse tipo de avaliação, teremos uma precisão maior de similaridade, que podera ser 
		representada por numeros positivos e negativos.
		"""
		for k in range(len(vectorCongressMan2)):

			if vectorCongressMan1[i][1] == vectorCongressMan2[k][1]: 
				
				if vectorCongressMan1[i][0] == vectorCongressMan2[k][0]:
					similaridade += 1
				#Tratando casos em que os votos não são iguais, mas se aproximam (na minha opnião) de alguma forma.
				else:
					if vectorCongressMan1[i][0] == "1" and vectorCongressMan2[k][0] == "3" or vectorCongressMan1[i][0] == "3" and vectorCongressMan2[k][0] == "1":
						similaridade += 0.5
					elif vectorCongressMan1[i][0] == "-1" and vectorCongressMan2[k][0] == "2" or vectorCongressMan1[i][0] == "2" and vectorCongressMan2[k][0] == "-1":
						similaridade += 0.5
					else:
						similaridade -= 1

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
