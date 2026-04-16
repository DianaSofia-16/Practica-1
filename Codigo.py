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
    def set_id(self, nuevo_id):
        self.__id = nuevo_id
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    def set_descripcion(self, nueva_descripcion):
        self.__descripcion = nueva_descripcion
    def set_precio(self, nuevo_precio):
        self.__precio = nuevo_precio
    def set_categoria(self, nueva_categoria):
        self.__categoria = nueva_categoria
    def set_ingredientes(self, nuevos_ingredientes):
        self.__ingredientes = nuevos_ingredientes
    def info(self):
        print(f"{self.__id} | {self.__nombre} | {self.__descripcion} | $ {self.__precio} | {self.__categoria} | Ingredientes: {self.__ingredientes}")
    def mostrar_ingredientes(self):
        if self.__ingredientes:
            print(self.__ingredientes)
        else:
            print("No hay ingredientes para mostrar")
    def aplicar_descuento(self, porcentaje):
        descuento = self.__precio * (porcentaje/100)
        precio_final = self.__precio - descuento
        return precio_final

platillo1 = Platillo(1, "Flan napolitano", "Flan casero bañado en caramelo", 70, "Postre")
platillo2 = Platillo(2, "Hamburguesa BBQ Bacon", "Hamburguesa de res con tocino y salsa BBQ", 185, "Plato fuerte", ["pan brioche", "carne de res 200g", "tocino", "queso cheddar", "cebolla caramelizada", "salsa BBQ"])

# Método mostrar_ingredientes
platillo1.mostrar_ingredientes()
platillo2.mostrar_ingredientes()
# Método aplicar_descuento
print(f"El precio ya con descuento es: {platillo1.aplicar_descuento(50)}")
print(f"El precio ya con descuento es: {platillo2.aplicar_descuento(20)}")
# Método info
platillo1.info()
platillo2.info()