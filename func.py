#coding: utf-8

"""
Construção da primeira função, com trabalho de calcular a similaridade entre dois vetores 
de um dicionario com base em id's que servem como identificador dentro do dicionario.

Forma mais basica da Função Principal, que funciona fazendo algo parecido com o
Produto interno entre vetores.
"""

#Forma que todos os dados se organizam dentro do arquivo: id_proposicao,id_votacao,id_deputado,voto,partido.
#Possibilidade de votos: Não" = -1, "Faltou" = 0, "Sim" = 1, "Obstrução" = 2, "Abstenção" = 3, "Art. 17" = 4

#Extrategia: dicionario que guarda dicionarios que possuem listas.

#função auxiliar para tratar cada dataset para colocalos de forma organizada no dicionario dinal
def aux_build_dic(arq,votos):
	arq = arq.split("\n")
	
	for i in arq:
		i = i.split(",")
	#id_proposicao,id_votacao,id_deputado,voto,partido.
	for i in range(1,len(arq)):
		if votos.has_key(arq[i][0]):
			votos[arq[i][0]][arq[i][2]] = []
			for j in range(1,len(arq[i])):
				if arq[i][j] != arq[i][2]:
					votos[arq[i][0]][arq[i][2]].append(arq[i][j])
		else:
			votos[arq[i][0]] = {}

	return votos
			
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
	arq2015 = open(path2015,"w")
	arq2016 = open(path2016,"w")
	arq2017 = open(path2017,"w")
	arq2018 = open(path2018,"w")

	#usando função auxiliar para alterar dicionario
	votos = aux_build_dic(arq2015,votos)
	votos = aux_build_dic(arq2016,votos)
	votos = aux_build_dic(arq2017,votos)
	votos = aux_build_dic(arq2018,votos)

	#fechando arquivos
	arq2015.close()
	arq2016.close()
	arq2017.close()
	arq2018.close()

	return votos

votos = build_Dic()