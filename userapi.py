# app.py - Flask API

from flask import Flask, request, jsonify
from rq import Queue
from redis import Redis
import os

app = Flask(__name__)
redis_conn = Redis(host='localhost', port=6379)
queue = Queue(connection=redis_conn)

@app.route('/submit_audio', methods=['POST'])
def submit_audio():
    # Check if audio file is present in the request
    if 'audio_file' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio_file']
    # You can add more validation for audio file type, size, etc. here

    # Save the audio file to disk or cloud storage
    audio_file_path = os.path.join('uploads', audio_file.filename)
    audio_file.save(audio_file_path)

    # Enqueue audio processing task
    j = queue.enqueue(str(process_audio), str(audio_file_path))
    print(j)
    return jsonify({'message': 'Audio submitted for processing'}), 202

def process_audio(audio_file_path):
    # Simulate audio processing (replace with your actual processing logic)
    print(f"Processing audio file: {audio_file_path}")
    return "Audio_Test"
    # Example: Perform transcription, analysis, etc.

if __name__ == '__main__':
    app.run(debug=True)
