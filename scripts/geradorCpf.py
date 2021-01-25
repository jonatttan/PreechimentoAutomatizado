import random
import json

def gera_cpf(arquivo):
    def cpf():
        n = 9
        n1 = random.randint(0,9)
        n2 = random.randint(0,9)
        n3 = random.randint(0,9)
        n4 = random.randint(0,9)
        n5 = random.randint(0,9)
        n6 = random.randint(0,9)
        n7 = random.randint(0,9)
        n8 = random.randint(0,9)
        n9 = random.randint(0,9)
        num1 = n9*2 + n8*3 + n7*4 + n6*5 + n5*6 + n4*7 + n3*8 + n2*9 + n1*10
        num1 = 11 - (num1 % 11)
        if (num1 >= 10):
            num1 = 0
        
        num2 = num1*2 + n9*3 + n8*4 + n7*5 + n6*6 + n5*7 + n4*8 + n3*9 + n2*10 + n1*11
        num2 = 11 - (num2 % 11)
        if (num2 >= 10):
            num2 = 0

        nums = (n1,n2,n3,n4,n5,n6,n7,n8,n9,num1,num2)
        num_cpf = ""
        for i in nums:
            num_cpf += str(i)

        return num_cpf


    with open(arquivo, 'r') as lista_cpf:
        lista = json.load(lista_cpf)

    for cliente in lista:
        cliente["cpf"] = cpf()

    #for cliente in lista:
    #    print(cliente["cpf"])
    #    print(cliente["nome"],"\n")

    with open(arquivo, 'w') as lista_cpf2:
        json.dump(lista, lista_cpf2, indent=4)



