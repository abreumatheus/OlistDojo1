from .base_dao import BaseDao
from aula014.models.seller import Seller


class SellerDao(BaseDao):
    def create(self, model:Seller)-> None:
        query = f"""INSERT INTO SELLERS 
                    (NAME, PHONE, EMAIL) 
                    VALUES 
                    ('{model.name}','{model.phone}','{model.email}');"""
        super().execute(query)

    def read_by_id(self, id:int)-> Seller:
        query = f"""SELECT NAME, PHONE, EMAIL, ID FROM SELLERS WHERE ID={id};"""
        result = super().read(query)[0]
        seller = Seller(result[0], result[1], result[2], result[3])
        return seller

    def read_all(self)-> list:
        sellers = []
        query = f"""SELECT NAME, PHONE, EMAIL, ID FROM SELLERS;"""
        list_result = super().read(query)
        for result in list_result:
            seller = Seller(result[0], result[1], result[2], result[3])
            sellers.append(seller)
        return sellers

    def delete(self, id:int)-> None:
        query = f"DELETE FROM SELLERS WHERE ID={id};""
        super().execute(query)

    def update(self, model:Seller)-> None:
        query = f"""UPDATE SELLERS 
                    SET
                        NAME = '{model.name}', 
                        PHONE = '{model.phone}', 
                        EMAIL = '{model.email}'
                    WHERE ID = {model.id};"""
        super().execute(query)
        