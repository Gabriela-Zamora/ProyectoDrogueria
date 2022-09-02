class Productos:

    def __init__(self,producto=None,cantidad=None):
        self.producto=producto
        self.cantidad=cantidad

    def __str__(self) -> str:
        datos="\n<<<<<<<<<<<<< DATOS productos >>>>>>>>>>>>>>>\n"
        datos+=f"producto: {self.producto} , cantidad: {self.cantidad}\n"

        return datos
