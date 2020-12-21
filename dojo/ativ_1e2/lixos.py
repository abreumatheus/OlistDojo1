#concatenação 
'SKU: ' + product.get_sku()
    + ' - Name: ' + product.get_name()
    + ' - Price: ' + str(product.get_price())
    + ' - Description: ' + product.get_description()
#funcao format
'SKU: {} - Name: {} - Price: {:.2f} - Description: {}'.format(
    product.get_sku(),
    product.get_name(),
    product.get_price(),
    product.get_description()
)
#interpolação de strings

nome1 = 'Regina' 
nome2 = 'Derli' 
nome3 = 'Luciana'

nomes = [ nome1, nome2, nome3 ]
# tipo por valor
# tipo por referencia

print(nomes)
nomes2 =  nomes.copy()
print(nomes2)

nomes2[1] = 'Canutto'
print(nomes)
print(nomes2)

from products import Product

p1 = Product()
p1.set_sku()
p1.set_name()
p1.set_price()
p1.set_description()

p2 = Product()
p2.set_sku()
p2.set_name()
p2.set_price()
p2.set_description()
produtos = [p1, p2]

def busca(termo):
    for p in produtos:
        if p.get_sku() == termo:
            return p

t = input('Digite um sku: ')
n = busca(t)
if n is None:
    print('nao achooo')
else:
    print(n)
    n.set_name()
    n.set_price()
    n.set_description()
    for p in produtos:
        print(p)

