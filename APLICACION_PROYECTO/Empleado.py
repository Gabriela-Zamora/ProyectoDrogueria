class Empleado:

    def __init__(self,documento=None,nombre=None,telefono=None,
    email=None, password=None, tipo=None
                    ):
        self.documento=documento
        self.nombre=nombre
        self.email=email
        self.telefono=telefono
        self.password=password
        self.tipo=tipo


    def imprimirDatos(self):
        datos="\n<<<<<<<<<<<<< DATOS ESTUDIANTE >>>>>>>>>>>>>>>\n"
        datos+=f"Documento: {self.documento} , Nombre: {self.nombre}\n"
        datos+=f"Email: {self.email} , Telefono: {self.telefono}\n"
        datos+=f"password: {self.password} , Tipo: {self.tipo}\n"
        print(datos)
