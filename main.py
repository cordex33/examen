from flask import Flask, request, render_template
app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'

usuarios = {
    'juan': 'admin',
    'pepe': 'user'
}

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        edad = int(request.form['edad'])
        pintura = int(request.form['pintura'])
        tarro = 9000
        resultado = ""
        if edad >= 18 and edad <= 30:
            total_sin_descuento = 9000 * pintura
            descuento = f"${(pintura * 9000) * 0.15}"
            resultado = pintura*tarro -((pintura * 9000) * 0.15)
            return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, descuento=descuento, resultado=resultado)

        elif edad >30:
            total_sin_descuento = 9000 * pintura
            descuento = f"${(pintura * 9000) * 0.25}"
            resultado = pintura*tarro - ((pintura * 9000) * 0.25)
            return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, descuento=descuento, resultado=resultado)

        elif edad < 18:
            total_sin_descuento = 9000 * pintura
            descuento = "Su edad no tiene descuento"
            resultado = 9000 * pintura
            return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, descuento=descuento, resultado=resultado)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['password']

        if usuario in usuarios and usuarios[usuario] == contrasena:
            if usuario == 'juan':
                mensaje = 'Bienvenido administrador juan'
            else:
                mensaje = 'Bienvenido usuario pepe'

            return render_template('ejercicio2.html', mensaje=mensaje)
        else:
            return render_template('ejercicio2.html', mensaje='Usuario o  contraseña incorrectos')
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)