from flask import Flask, jsonify, make_response
from http import HTTPStatus

app = Flask(__name__)

# Dados fictícios dos resultados dos jogos da NBA
resultados_nba = [
    {"data": "2024-05-10", "time_da_casa": "Los Angeles Lakers", "pontos_da_casa": 177, "time_visitante": "Boston Celtics", "pontos_visitante": 84},
    {"data": "2024-05-9", "time_da_casa": "Phoenix Suns", "pontos_da_casa": 97, "time_visitante": "Golden State Warriors", "pontos_visitante": 120},
    {"data": "2024-05-8", "time_da_casa": "San Antonio Spurs", "pontos_da_casa": 107, "time_visitante": "Miami Heat", "pontos_visitante": 77}
]

@app.route('/resultados_nba', methods=['GET'])
def get_resultados_nba():
    return jsonify(resultados_nba)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)