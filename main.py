from products import Product

products = []

def valid_number(number: float) -> float:
    try:
        while float(number) <= 0:
            number = float(input('Number must be bigger than 0, try again: '))
    except ValueError:
        number = valid_number(input('Number need to be a number: '))
    return number

def new_product() -> None:
    print('\nCreate new product')
    
    product = Product()
    sku_not_valid = True
    sku = ""
    while sku_not_valid:
        sku = input('Product SKU: ')
        p = search_product(sku)
        if not p:
            sku_not_valid = False
            break
        print('SKU invalid, try again')
    
    product.set_sku(sku)
    name = input('Product name: ')
    product.set_name(name)
    price = input('Product price: ')
    product.set_price(valid_number(price))
    weight = input('Product weight: ')
    product.set_weight(valid_number(weight))
    height = input('Product height: ')
    product.set_height(valid_number(height))
    lenght = input('Product lenght: ')
    product.set_lenght(valid_number(lenght))
    width = input('Product width: ')
    product.set_width(valid_number(width))
    description = input('Product description: ')
    product.set_description(description)

    products.append(product)


def list_products():
    if len(products) > 0:
        print('\nList all products')
        for product in products:
            print(product)
    else:
        print('\nNo products available.')


def input_sku():
    initial_product = input('Enter the product SKU: ')
    return search_product(initial_product)


def search_product(sku: str) -> Product:
    for product in products:
        if product.get_sku() == sku:
            return product


def product_detail():
    p = input_sku()
    if not p:
        print('Product not found.')
    else:
        print(p)


def delete_product():
    p = input_sku()
    if not p:
        print('Product not found.')
    else:
        products.remove(p)
        print('Product deleted successfully')


def edit_product():
    p = input_sku()
    if not p:
        print('Product not found.')
    else:
        print(p)
        
        name = input('Product name: ')
        p.set_name(name)
        price = input('Product price: ')
        p.set_price(valid_number(price))
        weight = input('Product weight: ')
        p.set_weight(valid_number(weight))
        height = input('Product height: ')
        p.set_height(valid_number(height))
        lenght = input('Product lenght: ')
        p.set_lenght(valid_number(lenght))
        width = input('Product width: ')
        p.set_width(valid_number(width))
        description = input('Product description: ')
        p.set_description(description)


def menu():
    options = ['Cadastrar Produto', 'Editar Produto', 'Listar Produtos', 
               'Buscar Produto por SKU', 'Deletar Produtos', 'Sair']

    print('\nMENU: ')

    for i, option in enumerate(options):
        print(f'[{i+1}] - {option}')

    op = int(input('Selecione uma opção: '))
    return op


while True:
    try:
        op = menu()
        if op == 1:
            new_product()
        elif op == 2:
            edit_product()
        elif op == 3:
            list_products()
        elif op == 4:
            product_detail()
        elif op == 5:
            delete_product()
        elif op == 6:
            exit(1)
        else:
            print('Opção indisponível. Tente novamente.')
    except ValueError:
        print('Opção indisponível. Tente novamente.')
