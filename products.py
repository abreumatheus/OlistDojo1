class Product:
    __sku: int
    __name: str
    __price: float
    __description: str

    def set_sku(self) -> None:
        sku = input('Enter the product sku: ')
        self.__sku = sku

    def get_sku(self) -> str:
        return self.__sku

    def set_name(self) -> None:
        name = input('Enter the product name: ')
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_price(self) -> None:
        price = float(input('Enter the product price: '))
        self.__price = price

    def get_price(self) -> float:
        return self.__price

    def set_description(self) -> None:
        description = input('Enter the product description: ')
        self.__description = description

    def get_description(self) -> str:
        return self.__description

    def __str__(self):
        return f'''
                    - SKU: {self.get_sku()} 
                    - Name: {self.get_name()} 
                    - Price: {self.get_price()} 
                    - Description: {self.get_description()}
                '''
