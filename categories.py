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

