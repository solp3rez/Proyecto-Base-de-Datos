from flask import Flask, jsonify, request ,render_template
import mysql.connector
from dotenv import load_dotenv
import os
from pathlib import Path
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"]) ##CORS(app)  # esto permite cualquier origen

# Cargar variables de entorno desde .env
env_path = Path(__file__).parent / "ini.env"
load_dotenv(dotenv_path=env_path)




# Configuración de la base de datos usando .env
db_config = {
    "host": os.getenv("DB_HOST", "10.9.120.5"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER", "proyecto"),
    "password": os.getenv("DB_PASS", "proyecto1234"),
    "database": os.getenv("DB_NAME", "ProyectoUBA")
}

def get_connection():
    return mysql.connector.connect(**db_config)

@app.route("/")
def index():
    return render_template("index.html")

# ----------------------
# VERIFICACIÓN DE CONEXIÓN
# ----------------------
try:
    conn = get_connection()
    conn.close()
    print("Conexión a la base de datos exitosa ✅")
except Exception as e:
    print("Error al conectar a la base de datos ❌:", e)

# ----------------------
# RUTAS PARA INGLES
# ----------------------
@app.route("/ingles", methods=["GET"])
def get_ingles():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Ingles")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/ingles", methods=["POST"])
def insertar_ingles():
    try:
        data = request.json
        apuntes = data.get("Apuntes")
        profesor = data.get("Profesor")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Ingles (Apuntes, Profesor) VALUES (%s, %s)", (apuntes, profesor))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Registro insertado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/ingles/<int:id>", methods=["PUT"])
def modificar_ingles(id):
    try:
        data = request.json
        apuntes = data.get("Apuntes")
        profesor = data.get("Profesor")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Ingles SET Apuntes=%s, Profesor=%s WHERE Ingles_id=%s", (apuntes, profesor, id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Registro modificado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/ingles/<int:id>", methods=["DELETE"])
def eliminar_ingles(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Ingles WHERE Ingles_id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": f"Registro con id {id} eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------
# RUTAS PARA QUIMICA
# ----------------------
@app.route("/quimica", methods=["GET"])
def get_quimica():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Quimica")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/quimica", methods=["POST"])
def insertar_quimica():
    try:
        data = request.json
        apuntes = data.get("Apuntes")
        profesor = data.get("Profesor")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Quimica (Apuntes, Profesor) VALUES (%s, %s)", (apuntes, profesor))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Registro insertado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/quimica/<int:id>", methods=["PUT"])
def modificar_quimica(id):
    try:
        data = request.json
        apuntes = data.get("Apuntes")
        profesor = data.get("Profesor")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Quimica SET Apuntes=%s, Profesor=%s WHERE Quimica_id=%s", (apuntes, profesor, id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Registro modificado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/quimica/<int:id>", methods=["DELETE"])
def eliminar_quimica(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Quimica WHERE Quimica_id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": f"Registro con id {id} eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------
# RUTAS PARA MATEMATICA
# ----------------------
@app.route("/matematica", methods=["GET"])
def get_matematica():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Matematica")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/matematica", methods=["POST"])
def insertar_matematica():
    try:
        data = request.json
        apuntes = data.get("Apuntes")
        profesor = data.get("Profesor")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Matematica (Apuntes, Profesor) VALUES (%s, %s)", (apuntes, profesor))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Registro insertado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/matematica/<int:id>", methods=["PUT"])
def modificar_matematica(id):
    try:
        data = request.json
        apuntes = data.get("Apuntes")
        profesor = data.get("Profesor")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Matematica SET Apuntes=%s, Profesor=%s WHERE Matematica_id=%s", (apuntes, profesor, id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Registro modificado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/matematica/<int:id>", methods=["DELETE"])
def eliminar_matematica(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Matematica WHERE Matematica_id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": f"Registro con id {id} eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------
# RUTAS PARA TAP
# ----------------------
@app.route("/tap", methods=["GET"])
def get_tap():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM TAP")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/tap", methods=["POST"])
def insertar_tap():
    try:
        data = request.json
        apuntes = data.get("Apuntes")
        profesor = data.get("Profesor")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TAP (Apuntes, Profesor) VALUES (%s, %s)", (apuntes, profesor))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Registro insertado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/tap/<int:id>", methods=["PUT"])
def modificar_tap(id):
    try:
        data = request.json
        apuntes = data.get("Apuntes")
        profesor = data.get("Profesor")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE TAP SET Apuntes=%s, Profesor=%s WHERE TAP_id=%s", (apuntes, profesor, id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Registro modificado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/tap/<int:id>", methods=["DELETE"])
def eliminar_tap(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM TAP WHERE TAP_id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": f"Registro con id {id} eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------
# RUTAS PARA AGBD
# ----------------------
@app.route("/agbd", methods=["GET"])
def get_agbd():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM AGBD")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/agbd", methods=["POST"])
def insertar_agbd():
    try:
        data = request.json
        apuntes = data.get("Apuntes")
        profesor = data.get("Profesor")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO AGBD (Apuntes, Profesor) VALUES (%s, %s)", (apuntes, profesor))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Registro insertado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/agbd/<int:id>", methods=["PUT"])
def modificar_agbd(id):
    try:
        data = request.json
        apuntes = data.get("Apuntes")
        profesor = data.get("Profesor")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE AGBD SET Apuntes=%s, Profesor=%s WHERE AGBD_id=%s", (apuntes, profesor, id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Registro modificado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/agbd/<int:id>", methods=["DELETE"])
def eliminar_agbd(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM AGBD WHERE AGBD_id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": f"Registro con id {id} eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------
# RUTAS PARA AED
# ----------------------
@app.route("/aed", methods=["GET"])
def get_aed():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM AED")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/aed", methods=["POST"])
def insertar_aed():
    try:
        data = request.json
        apuntes = data.get("Apuntes")
        profesor = data.get("Profesor")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO AED (Apuntes, Profesor) VALUES (%s, %s)", (apuntes, profesor))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Registro insertado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/aed/<int:id>", methods=["PUT"])
def modificar_aed(id):
    try:
        data = request.json
        apuntes = data.get("Apuntes")
        profesor = data.get("Profesor")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE AED SET Apuntes=%s, Profesor=%s WHERE AED_id=%s", (apuntes, profesor, id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Registro modificado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/aed/<int:id>", methods=["DELETE"])
def eliminar_aed(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM AED WHERE AED_id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": f"Registro con id {id} eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------
# RUTAS PARA PROGRAMACIÓN WEB
# ----------------------
@app.route("/programacionweb", methods=["GET"])
def get_programacionweb():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ProgramacionWeb")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/programacionweb", methods=["POST"])
def insertar_programacionweb():
    try:
        data = request.json
        apuntes = data.get("Apuntes")
        profesor = data.get("Profesor")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ProgramacionWeb (Apuntes, Profesor) VALUES (%s, %s)", (apuntes, profesor))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Registro insertado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/programacionweb/<int:id>", methods=["PUT"])
def modificar_programacionweb(id):
    try:
        data = request.json
        apuntes = data.get("Apuntes")
        profesor = data.get("Profesor")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE ProgramacionWeb SET Apuntes=%s, Profesor=%s WHERE ProgramacionWeb_id=%s", (apuntes, profesor, id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Registro modificado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/programacionweb/<int:id>", methods=["DELETE"])
def eliminar_programacionweb(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ProgramacionWeb WHERE ProgramacionWeb_id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": f"Registro con id {id} eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------
# RUTAS PARA DISEÑO DE SOFTWARE
# ----------------------
@app.route("/diseño_software", methods=["GET"])
def get_diseño_software():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM DiseñoSoftware")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/diseño_software", methods=["POST"])
def insertar_diseño_software():
    try:
        data = request.json
        apuntes = data.get("Apuntes")
        profesor = data.get("Profesor")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO DiseñoSoftware (Apuntes, Profesor) VALUES (%s, %s)", (apuntes, profesor))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Registro insertado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/diseño_software/<int:id>", methods=["PUT"])
def modificar_diseño_software(id):
    try:
        data = request.json
        apuntes = data.get("Apuntes")
        profesor = data.get("Profesor")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE DiseñoSoftware SET Apuntes=%s, Profesor=%s WHERE DiseñoSoftware_id=%s", (apuntes, profesor, id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Registro modificado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/diseño_software/<int:id>", methods=["DELETE"])
def eliminar_diseño_software(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM DiseñoSoftware WHERE DiseñoSoftware_id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": f"Registro con id {id} eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------
# RUTAS PARA APOYOM
# ----------------------
@app.route("/apoyoM", methods=["GET"])
def get_apoyoM():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ApoyoM")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/apoyoM", methods=["POST"])
def insertar_apoyoM():
    try:
        data = request.json
        apuntes = data.get("Apuntes")
        profesor = data.get("Profesor")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ApoyoM (Apuntes, Profesor) VALUES (%s, %s)", (apuntes, profesor))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Registro insertado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/apoyoM/<int:id>", methods=["PUT"])
def modificar_apoyoM(id):
    try:
        data = request.json
        apuntes = data.get("Apuntes")
        profesor = data.get("Profesor")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE ApoyoM SET Apuntes=%s, Profesor=%s WHERE ApoyoM_id=%s", (apuntes, profesor, id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Registro modificado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/apoyoM/<int:id>", methods=["DELETE"])
def eliminar_apoyoM(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ApoyoM WHERE ApoyoM_id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": f"Registro con id {id} eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------
# EJECUTAR APP
# ----------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
