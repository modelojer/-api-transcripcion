from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)  # permite solicitudes desde React Native

# Lee la clave desde una variable de entorno en Render
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    file = request.files['file']
    
    response = requests.post(
        'https://api.openai.com/v1/audio/transcriptions',
        headers={
            'Authorization': f'Bearer {OPENAI_API_KEY}'
        },
        files={
            'file': (file.filename, file.stream, file.content_type),
            'model': (None, 'whisper-1')
        }
    )

    return jsonify(response.json())
