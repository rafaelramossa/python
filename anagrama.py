arq1 = open("input003.txt", "r")
data = arq1.read()
lista =[]

lista = data.split("\n")


nova_lista = []
numeros = ['1','2','3','4','5','6','7','8','0','9']
count = 0

for i in lista:
    for i2 in lista:
        if ''.join(sorted(i)) in ''.join(sorted(i2)): 
            
            if i not in numeros:
                
                    if i == i2 :
                        nova_lista.append(i)                   
                                                        
            break