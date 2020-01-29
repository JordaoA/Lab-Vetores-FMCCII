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
	path2015 = "../data/votacoes_2015.csv"
	path2016 = "../data/votacoes_2016.csv"
	path2017 = "../data/votacoes_2017.csv"
	
	#abrindo arquivos
	arq2015 = open(path2015,"r")
	arq2016 = open(path2016,"r")
	arq2017 = open(path2017,"r")

	#usando função auxiliar para alterar dicionario
	aux_build_dic(arq2015.read(),votos)
	aux_build_dic(arq2016.read(),votos)
	aux_build_dic(arq2017.read(),votos)

	#fechando arquivos
	arq2015.close()
	arq2016.close()
	arq2017.close()

	return votos
