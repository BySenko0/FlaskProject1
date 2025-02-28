from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    conn = mysql.connector.connect(
        host="mysql",  # ⬅ Cambiado 'localhost' por 'db'
        user="root",
        password="root",  # ⬅ Corregido 'passwd' a 'password'
        database="db"
    )
    cursor = conn.cursor(dictionary=True)  # ⬅ Permite que los resultados sean diccionarios
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()  # ⬅ Eliminada la doble llamada a conn.close()

    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
