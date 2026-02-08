from flask import Flask, render_template, request, flash
import math
import forms
from formsCinepolis import CinepolisForm
from formsCinepolis import CinepolisForm
from flask_wtf.csrf import CSRFProtect
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
app.secret_key = 'clave_secreta'
app.config['SECRET_KEY'] = 'clave_secreta_123'
csrf = CSRFProtect(app)
csrf=CSRFProtect()



@app.route("/cinepolis", methods=['GET', 'POST'])
def cinepolis():
    form = CinepolisForm(request.form)
    total_pagar = 0.0
    mensaje = ""

    if request.method == 'POST' and form.validate():
        try:
            nombre = form.nombre.data
            compradores = int(form.cant_compradores.data)
            boletas = int(form.cant_boletas.data)
            tarjeta = form.tarjeta.data
            
            max_boletas_permitidas = compradores * 7

            if boletas > max_boletas_permitidas:
                mensaje = f"Error: No se pueden comprar más de 7 boletas por persona."
            else:
                precio_unitario = 12
                total = boletas * precio_unitario

                if boletas > 5:
                    total = total * 0.85 
                elif boletas >= 3:
                    total = total * 0.90 

                if tarjeta == 'Si':
                    total = total * 0.90 
                
                total_pagar = total

        except Exception as e:
            mensaje = "Ocurrió un error en el cálculo"

    return render_template("cinepolis.html", form=form, total=total_pagar, mensaje=mensaje)









@app.route('/')
def index():
    title = "IDGS804 - Intro Flask"
    listado = ['Juan','Ana','Pedro','Mario']
    return render_template('index.html')#,title=title,listado=listado)

@app.route("/saludo1")
def saludo1():
    return render_template('saludo1.html')

@app.route("/saludo2")
def saludo22():
    return render_template('saludo2.html')

@app.route("/distancia", methods=['GET', 'POST'])
def saludo2():
    distancia = None

    if request.method == 'POST':
        x1 = float(request.form['x1'])
        y1 = float(request.form['y1'])
        x2 = float(request.form['x2'])
        y2 = float(request.form['y2'])

        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return render_template('distancia.html', distancia=distancia)

@app.route("/operasBas", methods=['GET','POST'])
def operasbas():
    res=None
    if request.method == 'POST':
        n1=request.form.get('num1')
        n2=request.form.get('num2')
        if request.form.get('operacion') == 'suma':
            res=float(n1)+float(n2)
            
        if request.form.get('operacion') == 'restar':
            res=float(n1)-float(n2)
            
        if request.form.get('operacion') == 'dividir':
            res=float(n1)/float(n2)
            
        if request.form.get('operacion') == 'multiplicar':
            res=float(n1)*float(n2)
            
    return render_template("operasBas.html", res=res)

@app.route("/resultado", methods=['GET', 'POST'])
def result1():
    n1=request.form.get('num1')
    n2=request.form.get('num2')
    return f"<h1>La suma es: {float(n1)+float(n2)}</h1>"

@app.route("/hola")
def func():
        return 'Hola, Nueva Ruta!!'

@app.route("/user/<string:user>")
def user(user):
    return f'Hola, {user}!'

@app.route("/numero/<int:n>")
def numero(n):
    return f'<H1>Number, {n}!</H1>'

@app.route("/username/<int:id>/<string:username>")
def username(id,username):
    return f'<H1>Hola, {username}, tu id es: {id}</H1>'

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return f'<h1>La suma es: {n1 + n2}</h1>'

@app.route('/operas')
def operas():
    return '''
        <form>
        <label for="name"> Nombre: </label>
        <input type="text" id="name" name="name" required>
        </br>
        <label for="name"> Paterno: </label>
        <input type="text" id="name" name="name" required>
        </br>
        <label for="pass"> Password: </label>
        <input type="password" id="pass" name="pass">
        </br>
        <input type="submit" value="Enviar">
        </form>
'''

@app.route("/alumnos", methods=['GET','POST'])
def alumnos():
    mat=0
    nom=''
    ape=''
    email=''
    alumno_clas=forms.UserForm(request.form)
    if request.method=='POST':
        mat = alumno_clas.matricula.data
        nom = alumno_clas.nombre.data
        ape = alumno_clas.apellido.data
        email = alumno_clas.correo.data
    return render_template("alumnos.html",
    form=alumno_clas,
    mat=mat,
    nom=nom,
    ape=ape,
    email=email)
    
    
    




from formsPizzeria import PizzaForm  

@app.route('/pizzeria', methods=['GET', 'POST'])
def pizzeria():

    form = PizzaForm()
    pedido = None

    precios_tamano = {
        'ch': 40,
        'md': 80,
        'gr': 120
    }

    precios_ing = {
        'jam': 10,
        'pin': 10,
        'cha': 10
    }

    if request.method == 'POST':

        if form.validate():

            precio_tamano = precios_tamano[form.tamano.data]
            total_ingredientes = sum(precios_ing[i] for i in form.ingredientes.data)
            num_pizzas = form.cantidad.data

            total_pagar = (precio_tamano + total_ingredientes) * num_pizzas

            pedido = {
                'nombre': form.nombre.data,
                'direccion': form.direccion.data,
                'telefono': form.telefono.data,
                'tamano': dict(form.tamano.choices)[form.tamano.data],
                'ingredientes': ", ".join(
                    dict(form.ingredientes.choices)[i]
                    for i in form.ingredientes.data
                ),
                'cantidad': num_pizzas,
                'total': total_pagar
            }

        else:

             flash("Comprueba que todos los campos esten bien", "error")

    return render_template('pizzeria.html', form=form, pedido=pedido)

    
    

if __name__ == '__main__':
        app.run(host="127.0.0.1", port=5051,debug=True)
    