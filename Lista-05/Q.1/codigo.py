from random import sample

lista = sample(range(100), k=10)

listaCrescente = sorted(lista)
listaDecrescente = sorted(lista, reverse=True)

print(f"Lista crescente: {listaCrescente}")
print(f"Lista decrescente: {listaDecrescente}")