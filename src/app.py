from flask import Flask, request, jsonify
from mysql import connector as con
from flask_cors import CORS

# Configuração e conexão do banco de dados 
config = {
    'user': 'root', 
    'password': 'impacta2024', 
    'database': 'aulareact',
    'host': 'localhost',
    'raise_on_warnings': True
}

app = Flask(__name__)
CORS(app)

db = con.connect(user = 'root', password = 'impacta2024', database = 'aulareact')

@app.route('/api/formulario', methods=['GET', 'POST'])
def formulario():
    json = request.get_json()
    nome = json['txtNome']
    
    cursor = db.cursor()
    query = "INSERT INTO formulario(nome) VALUES ('%s');" %nome
    cursor.execute(query)
    db.commit()
    cursor.close()
    return f'{nome} adicionado com sucesso!', 200

if __name__ == "__main__":
    app.run(debug=True)