from flask import Flask, request, render_template, redirect, url_for, flash
from cliente import guardar_cliente
import os

app = Flask(__name__)
app.secret_key = 'pepino56'

# Ruta para el formulario
@app.route('/', methods=['GET'])
def formulario():
    return render_template('cliente.html')

# Ruta para procesar el formulario
@app.route('/guardar_cliente', methods=['POST'])
def procesar_cliente():
    try:
        # Recibir datos del formulario y archivo
        datos_formulario = request.form
        archivo_img = request.files['imgDocumento']

        # Guardar cliente usando la lógica de cliente.py
        mensaje = guardar_cliente(datos_formulario, archivo_img)
        print(mensaje, 'success')

        return redirect(url_for('formulario'))

    except Exception as e:
        print(f"Error: {str(e)}", 'danger')
        return redirect(url_for('formulario'))

if __name__ == '__main__':
    app.run(debug=True)
