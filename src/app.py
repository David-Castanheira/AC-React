from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuração e conexão do banco de dados 
config = {
    'user': 'root', 
    'password': 'impacta2024', 
    'database': 'aulareact',
    'host': 'localhost',
    'raise_on_warnings': True
}

# Rota que captura dados do formulário e insere dados no banco com path definido no arquivo 'Form.js'
@app.route('/api/formulario', methods=['GET', 'POST'])
def formulario():
    json = request.get_json()
    nome = json['txtNome']
    endereco = json['txtEndereco']
    telefone = json['txtTelefone']

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    query = "INSERT INTO formulario (nome, endereco, telefone) VALUES (%s, %s, %s)"
    cursor.execute(query, (nome, endereco, telefone))
    cnx.commit()
    cursor.close()
    cnx.close()
    return f'{nome, endereco, telefone} adicionados com sucesso!', 200

if __name__ == "__main__":
    app.run(debug=True)
