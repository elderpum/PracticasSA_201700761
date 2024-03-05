from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/genderize', methods=['GET'])
def genderize():
    name = request.args.get('name')

    if not name:
        return jsonify({'error': 'Missing name parameter'}), 400

    url = f'https://api.genderize.io/?name={name}'
    response = requests.get(url)
    data = response.json()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=7000)