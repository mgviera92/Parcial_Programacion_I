# 3
from random import randint
lista = []

for i in range (0,78):
    num1 = randint(1,600)
    lista.append(num1)

lista.sort()

print ("El menor es ",lista[0])
print ("El mayor es ",lista[77])

print(lista)
for lista in range (0,78):
    if (lista % 2==0):
        print(lista)