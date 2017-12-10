from itertools import product

caracteres = [1, 3, 5, 9]
permsList = []
permsListInv = []
genComb = product(caracteres, repeat=2) # conjunto tomado 2 a 2
for subset in genComb:
    #print(subset[0]) # tuple retornado com uma combinacao por loop
    if(subset[0] < subset[1]): # remocao de repeticoes e desordem de elementos
    	permsList.append(subset)

#print(permsList)
permsListInv = permsList[::-1] # recebe lista invertida
#print(permsListInv)

for x in range(0, len(permsList) // 2):
	soma = permsList[x][0] + permsList[x][1] + permsListInv[x][0] + permsListInv[x][1]
	print (permsList[x], permsListInv[x], permsList[x][0] + permsList[x][1], permsListInv[x][0] + permsListInv[x][1])

