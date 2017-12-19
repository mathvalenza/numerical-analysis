import numpy as np

def calculaErro(x1_old, x2_old, x1, x2):
	return max(abs(x1 - x1_old),abs(x2 - x2_old)) / max(abs(x1),abs(x2)) # erro relativo

def f1(x2):
	return x2**3 / 9.0 # funcao "fi" em relacao a x2

def f2(x1):
	return (x1**2 + 1) / 6.0 # funcao "fi" em relacao a x1

def itPontoFixo(x1, x2):
	print("k\t   x1\t\t   x2\t\t  erro") # printa cabecalho
	k=0
	print(k, "\t", "%.7f"%x1, "\t%.7f"%x2, "\t0.0000000")
	while(True):
		x1_old = x1 # x1(k-1)
		x2_old = x2
		x1 = f1(x2_old) # calcula x1(k)
		x2 = f2(x1_old)
		erro = calculaErro(x1_old, x2_old, x1, x2)

		if (erro < 10**-5): # condicao de parada
			return (x1,x2)

		k+=1 # numero de iteracoes
		print(k, "\t", "%.7f"%x1, "\t%.7f"%x2, "\t%.7f"%erro) # printa os valores de cada iteracao

itPontoFixo(0.5,0.5) #chama a iteração por ponto fixo passando x1=0.5 e x2=0.5 como chutes iniciais
