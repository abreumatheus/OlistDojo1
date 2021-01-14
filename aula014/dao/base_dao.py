from .connection import Connection


class BaseDao:
    def execute(self, query:str)-> None:
        with Connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()

    def read(self, query:str)-> tuple:
        with Connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        return result
