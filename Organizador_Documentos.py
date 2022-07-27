lista = list()
ord = int(input('Numero da caixa [0 para]: '))
lista.append(ord)
while ord != 0:
	ord
	lista.append(ord)
lista.sort()
lista.remove(0)
print(lista)
print(f' Totalizando {len(lista)} caixas')