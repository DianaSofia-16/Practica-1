class Platillo:
    def __init__(self, id, nombre, descripcion, precio, categoria, ingredientes = []):
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__categoria = categoria
        self.__ingredientes = ingredientes
    def get_id(self):
        return self.__id
    def get_nombre(self):
        return self.__nombre
    def get_descripcion(self):
        return self.__descripcion
    def get_precio(self):
        return self.__precio
    def get_categoria(self):
        return self.__categoria
    def get_ingredientes(self):
        return self.__ingredientes