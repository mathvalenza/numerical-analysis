import math as mt

def posicaoFalsa(f, a, b, tol):
	
	ek = abs((b-a)/a)
	fa = f(a)
	fb = f(b)
	c = (fb*a - fa*b)/(fb-fa) # fórmula do Método da Pposição Falsa
	k = 0
	
	print ("    X(k)  |    E(k)   |  k")
	while (ek > tol and c != 0):
	  
		fa = f(a)
		fb = f(b)
		c = (fb*a - fa*b)/(fb-fa) # cálculo do novo ponto
		fc = f(c)
		if(fc * fa < 0):
			b = c
		else:
			a = c
		ek = abs((b-a)/a)
		print ("%.6f" % c ,"| %.6f" % (ek), " | ", k)
		k = k + 1
		
	print ("Método da Posição Falsa finalizado!")
	return c

def fun(x):
# f(x) = 2 + x/2 + sen(x)
	return 2 + x/2 + mt.sin(x)
def g(x):
#𝑓(𝑥) = 1 + ln(𝑥 − 2)sqrt(x)
	return 1 + mt.log(x-2) * mt.sqrt(x)
def h(x):
#𝑓(𝑥) = 2 − cos(𝑥)e^x
	return 2 - mt.cos(x) * (mt.e**x)
	
ret = True
while(ret):
  a = float(input("Digite o início do intervalo: "))
  b = float(input("Digite o fim do intervalo: "))
  aux = fun(a)*fun(b)
  if (aux < 0):
    ret = False
    print("Raiz aproximada: ", posicaoFalsa(fun, a, b, 10**-5))
  else:
    print ("Intervalo inválido, tente novamente")
