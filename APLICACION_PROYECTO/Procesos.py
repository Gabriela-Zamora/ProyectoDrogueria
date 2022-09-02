from Empleado import *
from Usuario import *
from AlmacenamientoEmpleados import *
from clases.operacionesMatematicas import *
from clases.Productos import *

class Procesos:
    productoGlobal=None
    miAlmacenamientoProductos=OperacionesMatematicas()

    usuarioGlobal=None
    miAlmacenamientoUsuarios=AlmacenamientoEmpleados()


    def llenarListaEmpleados(self):
        miUsuarioAdmin = Empleado("admin","admin","3138904567","imperiumdip@gmail.com","1234",1)
        miUsuario1 = Empleado("1096","Santiago Ruiz","3208798551","ruiz08399@gmail.com","1111",1)
        miUsuario2 = Empleado("111","Felipe","321789","felipe@gmail.com","111",1)
        miUsuario3 = Empleado("222","Juan Diego","3132456","juandiego@gmail.com","222",2)
        miUsuario4 = Empleado("333","Gabriela","32094567","gabriela@gmail.com","333",2)
    
        print()
        self.miAlmacenamientoUsuarios.registrarEmpleado(miUsuarioAdmin)
        self.miAlmacenamientoUsuarios.registrarEmpleado(miUsuario1)
        self.miAlmacenamientoUsuarios.registrarEmpleado(miUsuario2)
        self.miAlmacenamientoUsuarios.registrarEmpleado(miUsuario3)
        self.miAlmacenamientoUsuarios.registrarEmpleado(miUsuario4)

    def registrarEmpleado(self,miUsuario):
        print("Empleado a registrar",miUsuario)
        return self.miAlmacenamientoUsuarios.registrarEmpleado(miUsuario)

    def actualizarEmpleado(self,miUsuario):
        return self.miAlmacenamientoUsuarios.actualizarEmpleado(miUsuario)

    def eliminarEmpleado(self,documento):
        return self.miAlmacenamientoUsuarios.eliminarEmpleados(documento)


    def consultarEmpleado(self,documento):
        usuario=self.miAlmacenamientoUsuarios.consultarEmpleadoPorDocumento(documento)

        if(usuario!=None):
            print(usuario)
        else:
            print(f"\nNo existe ningún Empleado con el documento {documento}")
            
        return usuario

    def obtenerListaEmpleados(self):
        lista=self.miAlmacenamientoUsuarios.obtenerListaEmpleados()  
        return lista 
    
    def consultarListaEmpleados(self):
        print("\n<<<<<<<<<<<<<<<<<- LISTA DE ESTUDIANTES ->>>>>>>>>>>>>>>>>>>>")
        self.miAlmacenamientoUsuarios.consultarListaEmpleados()  
        print("\n*************************************************************\n")    
    def registrarProductos(self,producto):
        print("producto a registrar",producto)
        return self.miAlmacenamientoProductos.registrar_productos(producto)
