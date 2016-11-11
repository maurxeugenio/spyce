# Ler código do produto, quantidade, mostrar produto e preço total.
produtos = [ 0, 'cachorro quente', 'X-Salada', 'X-Bacon', 'Torrada Simples', 'Refrigerante']
preco = [ 0, 4.00, 4.50, 5.00, 2.00, 1.50]
codigo = int(input("codigo: "))
quant = int(input("quantidade: "))
print ("Produto:  %s  Total:  %s "%(produtos[codigo], (preco[codigo] * quant)))
