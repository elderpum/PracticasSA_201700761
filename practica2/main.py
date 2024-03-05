from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL base de los microservicios de Genderize y Agify
GENDERIZE_BASE_URL = "http://practica2-genderize-1:7000/genderize" # Nombre del contenedor de docker
AGIFY_BASE_URL = "http://practica2-agify-1:6000/agify" # Nombre del contenedor de docker

@app.route('/process_name', methods=['POST'])
def process_name():
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Missing name parameter'}), 400

    # Solicitar datos de género
    gender_response = requests.get(f"{GENDERIZE_BASE_URL}?name={name}")
    gender_data = gender_response.json()

    # Solicitar datos de edad
    age_response = requests.get(f"{AGIFY_BASE_URL}?name={name}")
    age_data = age_response.json()

    response = {
        'name': name,
        'gender': gender_data.get('gender'),
        'gender_probability': gender_data.get('probability'),
        'age': age_data.get('age')
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)