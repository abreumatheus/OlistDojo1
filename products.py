class Product:
    __sku: int
    __name: str
    __price: float
    __description: str

    def set_sku(self, sku: str) -> None:
        self.__sku = sku

    def get_sku(self) -> str:
        return self.__sku

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_price(self, price: float) -> None:
        self.__price = price

    def get_price(self) -> float:
        return self.__price

    def set_description(self, description: str) -> None:
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
