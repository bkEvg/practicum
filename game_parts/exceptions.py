
class FieldIndexError(Exception):
    def __str__(self) -> str:
        return "Введено значение за границами игрового поля"
