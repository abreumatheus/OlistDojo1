class Category:
    __id: int
    __name: str
    __id_mother: int # quando for 0 é mãe e quando for outro é referente a cat mãe

    def set_id(self, id: int) -> None:
        self.__id = int(id)

    def get_id(self) -> int:
        return self.__id

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_id_mother(self, id_mother: int) -> None:
        self.__id_mother = id_mother

    def get_id_mother(self) -> int:
        return self.__id_mother

    def __str__(self):
        pass