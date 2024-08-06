from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    data = request.get_json()
    birth_year = int(data['birthYear'])
    current_year = datetime.now().year
    age = current_year - birth_year
    return jsonify({'age': age})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

