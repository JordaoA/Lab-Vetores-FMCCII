#coding: utf-8
"""
Construção da primeira função, com trabalho de calcular a similaridade entre dois vetores 
de um dicionario com base em id's que servem como identificador dentro do dicionario.

Forma mais basica da Função Principal, que funciona fazendo algo parecido com o
Produto interno entre vetores.
"""
def similaridade(id1,id2,votes_p_ids):
	vetor1 = votes_p_ids[id1]
	vetor2 = votes_p_ids[id2]
	vetor_resultante = []
	similaridade = 0

	#Simulando "Produto interno" entre os dois vetores.
	for i in range(len(vetor1)):
		"""
		Nenhuma das condicionais trata o caso de voto a favor X abstenção
		por enquanto. 
		"""
		if (vetor1[i] == "1" and vetor2[i] == "1"):
			vetor_resultante.append(1)
		if (vetor1[i] == "0" and vetor2[i] == "0"):
			vetor_resultante.append(1)
		if (vetor1[i] == "-1" and vetor2[i] == "-1"):
			vetor_resultante.append(1)
		else:
			vetor_resultante.append(0)

	for i in vetor_resultante:
		similaridade += i

	return similaridade
