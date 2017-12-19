import math as mt

def bisect(f, a, b, tol, k):
  
    c = (a+b)/2 # c é o ponto  médio do intervalo
  
    # aux é usada na verificação da metade do intervalo
    # que será considerada na próxima iteração
    aux = f(a) * f(c)
    
    ek = (b-a)/a
    
    print ("%.6f" % c ,"| %.6f" % (ek), " | ", k)
    
    if abs(ek) < tol: #condição de parada: E(k) é menor que a tolerância
        print ("Método da Bissecção finalizado!")
        return c
    elif aux < 0: # se entre os pontos a e c há diferenca de sinal das imagens
        return bisect(f, a, c, tol, k+1) # o novo intervalo é [a,c]
    else: # se f(a) e f(c) tem o mesmo sinal 
        return bisect(f, c, b, tol, k+1) # o novo intervalo é [c,b]
def fun(x):
# f(x) = 2 + x/2 + sen(x)
	return 2 + x/2 + mt.sin(x)
def g(x):
#𝑓(𝑥) = 1 + ln(𝑥 − 2)sqrt(x)
	return 1 + mt.log(x-2) * mt.sqrt(x)
def h(x):
#𝑓(𝑥) = 2 − cos(𝑥)e^x
	return 2 - mt.cos(x) * (mt.e**x)
def n(x):
    return x**2 - 3
    
ret = True
while(ret):
  a = float(input("Início do intervalo: "))
  b = float(input("Fim do intervalo: "))
  aux = fun(a)*fun(b)
  if (aux < 0):
    ret = False
    print ("    X(k)  |    E(k)    |  k")
    print("Raiz aproximada: ", bisect(fun, a, b, 10**-5, 0))
  else:
    print ("Intervalo inválido, tente novamente")






