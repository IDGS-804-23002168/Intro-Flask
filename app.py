from flask import Flask, render_template, request
import math

app = Flask(__name__)
app.secret_key = 'clave_secreta'

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

if __name__ == '__main__':
        app.run(host="127.0.0.1", port=5051,debug=True)
    