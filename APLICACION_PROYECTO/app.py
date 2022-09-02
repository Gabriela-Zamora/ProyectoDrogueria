from re import U
from flask import Flask, render_template, request
from clases.operacionesMatematicas import *
from Procesos import *
from clases.Productos import *


app = Flask(__name__)

titulosTablaUsuarios=("Documento","Nombre","Telefono","Correo","Tipo")

operacionesM=OperacionesMatematicas()
misProcesos=Procesos()
misProcesos.llenarListaEmpleados()

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/inicio")
def inicio():
    return render_template('inicioEmpleado.html', user=Procesos.usuarioGlobal)

@app.route('/pagina')
def pagina():
    return render_template('pagina.html')

@app.route("/inicioJefe")
def inicioJefe():
    return render_template('inicioJefe.html', user=Procesos.usuarioGlobal)

@app.route("/pago")
def pago_empleados():
    return render_template('pagoEmpleados.html', user=Procesos.usuarioGlobal)

@app.route("/documentacion")
def documentacion():
    return render_template('documentacion.html', user=Procesos.usuarioGlobal)


@app.route("/registrar")
def registro():
    return render_template('registro.html', user=Procesos.usuarioGlobal)

@app.route("/consultar")
def consulta():
    informacion=misProcesos.obtenerListaEmpleados()
    return render_template('consulta.html',titulos_tabla=titulosTablaUsuarios,data=informacion,user=Procesos.usuarioGlobal)

@app.route("/gestionar_empleados")
def gestion_usuario():
    return render_template('gestionar_empleados.html',user=Procesos.usuarioGlobal)

@app.route("/pagoTotal", methods=['GET', 'POST'])
def pagoTotal():
    resultado=None
    if request.method == 'POST':
        num1=int(request.form['salario'])
        num2=int(request.form['comiciones'])
        empleado=(request.form['empleado'])

        resultado=operacionesM.sumar(num1,num2)

        res={
            "num1":num1,
            "num2":num2,
            "resultado":resultado,
            "empleado":empleado
            }
        print(resultado)
        
    return render_template('pagoEmpleados.html', data=res)

@app.route("/valida_usuarios", methods=['GET', 'POST'])
def valida_usuarios():
    informacion=misProcesos.obtenerListaEmpleados()
    global datos
    resultado=""
    if request.method == 'POST':


            usuario=None
            datos=None
            documento=request.form['documento']
            nombre=request.form['nombre']
            telefono=request.form['telefono']
            email=request.form['email']
            tipo=int(request.form['tipo'])

            if ('buscar' in request.form):
                usuario=misProcesos.consultarEmpleado(documento)
                if(usuario==None):
                    resultado="El Empleado no se encuentra registrado!"

            elif('registrar' in request.form):
                print("Registrar")
                usuario=misProcesos.consultarEmpleado(documento)
                if usuario==None:
                    usuario=Usuario(documento,nombre,telefono,email,documento,tipo)
                    misProcesos.registrarEmpleado(usuario)
                    resultado=misProcesos.registrarEmpleado(usuario)
                else:
                    resultado=f"El documento ya se encuentra registrado y corresponde a {usuario.nombre}"
            elif('actualizar' in request.form):
                print("actualizar")
                usuario=Usuario(documento,nombre,telefono,email,documento,tipo)
                resultado=misProcesos.actualizarEmpleado(usuario)
            elif('eliminar' in request.form):
                print("eliminar")
                usuario=Usuario(documento,nombre,telefono,email,documento,tipo)
                resultado=misProcesos.eliminarEmpleado(documento)

            print("**********************")
            print("VALOR DE EMPLEADO",usuario)
            if(usuario!=None):
                datos={
                    "documento":usuario.documento,
                    "nombre":usuario.nombre,
                    "telefono":usuario.telefono,
                    "email":usuario.email,
                    "tipo":usuario.tipo,
                    "resultado":resultado
                    }

            
    return render_template('gestionar_empleados.html',titulos_tabla=titulosTablaUsuarios,data=informacion,usuario=datos,user=Procesos.usuarioGlobal)


@app.route('/inicio_sesion', methods=['POST'])
def inicio_sesion():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        Procesos.usuarioGlobal=misProcesos.consultarEmpleado(usuario)
        print(f"usuario Ingresado:{usuario}, pass:{password}")
        print(f"usuario encontrado:{Procesos.usuarioGlobal}")
        if Procesos.usuarioGlobal!=None:
            if(usuario==Procesos.usuarioGlobal.documento and password==Procesos.usuarioGlobal.password):
                return render_template('inicioJefe.html',user=Procesos.usuarioGlobal)
            

        return render_template('login.html',user=None)

@app.route("/registro_usuario", methods=['GET', 'POST'])
def registrarEmpleado():
    resultado=None
    documento,nombre,telefono,email,tipo="","","","",""

    if request.method == 'POST':
        usuario=None
        documento=request.form['documento']
        nombre=request.form['nombre']
        telefono=request.form['Telefono']
        email=request.form['email']
        password=request.form['password']
        tipo=int(request.form['tipo'])

        print("Registrar")
            
        usuario=misProcesos.consultarEmpleado(documento)
        if usuario==None:
            usuario=Usuario(documento,nombre,telefono,email,password,tipo)
            misProcesos.registrarEmpleado(usuario)
            resultado=misProcesos.registrarEmpleado(usuario)
        else:
            resultado=f"El documento ya se encuentra registrado y corresponde a {usuario.nombre}"       
      

        datos={
            "resultado":resultado
        }

    return render_template('registro.html',data=datos)

@app.route("/registrar_producto", methods=['GET', 'POST'])   
def registrar_producto():
    global datos
    resultado=None
    producto,cantidad="",""
    
 
    if request.method == 'POST':
        
        productos=None
        producto=request.form['producto']
        cantidad=int(request.form['cantidad'])

        productos=Productos(producto,cantidad)
        misProcesos.registrarProductos(productos)
        resultado=misProcesos.registrarProductos(productos)

        datos={
            "resultado":resultado
        }

    return render_template('registrar_producto.html')



if (__name__ == '__main__'): 
    app.run(debug=True,port=8080)