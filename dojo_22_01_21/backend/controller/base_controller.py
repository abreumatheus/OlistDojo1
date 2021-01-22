class BaseController:
    def __init__(self, dao) -> None:
        self.dao = dao

    def save(self, obj: object) -> None:
        self.dao.save(obj)

    def read_all(self) -> list:
        return self.dao.read_all()

    def read_by_id(self, id: int) -> object:
        return self.dao.read_by_id(id)

    def delete(self, obj: object) -> None:
        self.dao.delete(obj)
