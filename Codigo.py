class Platillo:
    def __init__(self, id, nombre, descripcion, precio, categoria, ingredientes = []):
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__categoria = categoria
        self.__ingredientes = ingredientes