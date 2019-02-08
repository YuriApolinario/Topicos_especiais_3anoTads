#Este é um comentario

'''comentario em bloco

- Três aspas simples ou tres aspas duplas

print("Olá 3º ano do TADS!")

print("Maravilha")

'''

'''
nome = "Yuri"


#Concatenação com +
print("Olá", nome )


#Entrada de dados pelo terminal
nome = input("digite seu nome: ")
print(nome + " bem vindo ao sistema! ")

#quandi trabalhamos com  numeros, temos que converter a variavel
idade = input("digite sua idade: ")
idade = int(idade)
#idade = float(idade)
'''
'''
operadores
+
-
*
/

** é usado para calcular a Potencia. Por exemplo
2**3 = 8
8**2 = 64

A raiz de um numero é ele elevado a (1/x)
16**(1/2) - raiz quadrada de 16
16**(1/3) - raiz quadrada de 16
257**(1/5) - raiz de grau 5

print("A raiz é ", 16**(1/4) )

'''
'''
Condicionais

'''

a = 20

if a > 10:
    print(str(a) , " é maior que 10. ")

elif a < 10:
    print(str(a) , " é menor do que 10. ")

else:
    print(str(a) , " é igual a 10.")

'''
Laços de repetição
'''

x = 1

t = 8

while x <= 10:

    print(x, "x", t, "=", t*x)

    x += 1
