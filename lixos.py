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

