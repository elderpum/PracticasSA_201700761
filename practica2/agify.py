from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/agify', methods=['GET'])
def agify():
    name = request.args.get('name')

    if not name:
        return jsonify({'error': 'Missing name parameter'}), 400

    url = f'https://api.agify.io/?name={name}'
    response = requests.get(url)
    data = response.json()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=6000)