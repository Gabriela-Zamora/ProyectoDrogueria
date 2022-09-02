class OperacionesMatematicas:
    listaProductos=[]
    listaGeneralProductos=[]

    def sumar(self,num1,num2):
        return num1+num2
    
    def registrar_productos(self,producto):
        
        self.listaProductos.append(producto)
        lista=[]
        lista.append(producto.producto)
        lista.append(producto.cantidad)
        print(lista)
        print(producto)
        
        self.listaGeneralProductos.append(lista)

        print(f"producto {producto.producto} registrado con exito!")
        return f"producto {producto.producto} registrado con exito!"

    