from Usuario import *

class AlmacenamientoEmpleados:

    listaEmpleados=[]
    listaGeneralEmpleados=[]

    def registrarEmpleado(self,empleado):
        
        self.listaEmpleados.append(empleado)
        lista=[]
        lista.append(empleado.documento)
        lista.append(empleado.nombre)
        lista.append(empleado.telefono)
        lista.append(empleado.email)
        lista.append(empleado.password)
        lista.append(empleado.tipo)
        print(lista)
        print(empleado)
        print(type(empleado))
        print("Tipo empleado: ",empleado.tipo)
        if (empleado.tipo==1):
            print("Ingresa a tipo 1")

        else:

            print("Ingresa a tipo 2")
        self.listaGeneralEmpleados.append(lista)

        print(f"Empleados {empleado.nombre} registrado con exito!")
        return f"Empleados {empleado.nombre} registrado con exito!"

    def eliminarEmpleados(self,documento):
        global nombre
        print(documento)
        empleado=self.consultarEmpleadoPorDocumento(documento)
        if(empleado!=None):
            nombre=empleado.nombre
            for i in range(len(self.listaGeneralEmpleados)):
                lista=self.listaGeneralEmpleados[i]
                print("-->",lista)
                if(empleado.documento==lista[0]):
                    print("Elimina")
                    self.listaGeneralEmpleados.remove(lista)
                    self.listaEmpleados.remove(empleado)
                    break
                mensaje=f"El Empleado {nombre} Se ha eliminado con exito!"
        
        return mensaje

    def actualizarEmpleado(self,miEmpleado):
        empleado=self.consultarEmpleadoPorDocumento(miEmpleado.documento)
        mensaje=""
        if(empleado!=None):
            empleado.nombre=miEmpleado.nombre
            empleado.telefono=miEmpleado.telefono
            empleado.email=miEmpleado.email
            empleado.password=miEmpleado.password
            empleado.tipo=miEmpleado.tipo
            self.actualizarListaGeneralEmpleados(empleado)
            mensaje="Se ha actualizado el empleado"
        else:
            mensaje="no se pudo actualizar"
        
            
        return mensaje

    def actualizarListaGeneralEmpleados(self,empleado):
        for i in range(len(self.listaGeneralEmpleados)):
            lista=self.listaGeneralEmpleados[i]
            print("-->",lista)
            if(empleado.documento==lista[0]):
                print("Actualiza")
                lista[1]=empleado.nombre
                lista[2]=empleado.telefono
                lista[3]=empleado.email
                lista[4]=empleado.password
                if (empleado.tipo==1):
                    print("Ingresa a tipo 1")
                    lista[5]="Administrador"
                else:
                    lista[5]="Empleado"
                    print("Ingresa a tipo 2")
                
                break


    def obtenerListaEmpleados(self):
        print(self.listaGeneralEmpleados)
        return self.listaGeneralEmpleados

    def consultarListaEmpleados(self):
        if(self.validaTamanioLista()==True):
            for i in range(len(self.listaEmpleados)):
                empleado=self.listaEmpleados[i]
                print(empleado)
        
        return self.listaEmpleados


    def consultarEmpleadoPorDocumento(self,documento):
        empleado=None 
        if(self.validaTamanioLista()==True):
            for est in self.listaEmpleados:
                if(est.documento==documento):
                    empleado=est 
        
        return empleado
        

    def obtenerCantidadEmpleados(self):
        return len(self.listaEmpleados)

    
    def validaTamanioLista(self):
        if(len(self.listaEmpleados)>0):
            return True
        else:
            print("\n<<<< No han registrado empleados >>>")
            return False
