from products import Product


products = []


def new_product() -> None:
    print('\nCreate new product')
    product = Product()
    product.set_sku()
    product.set_name()
    product.set_price()
    product.set_description()
    products.append(product)


def list_products():
    print('\nList all products')
    for product in products:
        print('SKU: ' + product.get_sku()
              + ' - Name: ' + product.get_name()
              + ' - Price: ' + str(product.get_price())
              + ' - Description: ' + product.get_description())


def search_product(initial_product: str) -> Product:
    for product in products:
        if product.get_sku() == initial_product:
            return product


def edit_product():
    initial_product = input('Enter the product SKU: ')
    p = search_product(initial_product)
    if p is None:
        print('Product not found.')
    else:
        print('SKU: ' + p.get_sku()
              + ' - Name: ' + p.get_name()
              + ' - Price: ' + str(p.get_price())
              + ' - Description: ' + p.get_description())
        p.set_name()
        p.set_price()
        p.set_description()


def menu():
    options = ['Cadastrar Produto', 'Editar Produto',
               'Listar Produtos', 'Deletar Produtos', 'Sair']

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
            delete_product()
        elif op == 5:
            exit(1)
        else:
            print('Opção indisponível. Tente novamente.')
    except ValueError:
        print('Opção indisponível. Tente novamente.')
