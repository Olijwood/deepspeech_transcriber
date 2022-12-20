from flask import Flask, request, render_template, jsonify, after_this_request
from flask_cors import CORS
import os
import deep_speech_transcriber
import glob

app = Flask(__name__)
CORS(app)

APP__ROOT = os.path.dirname(os.path.abspath(__name__))

@app.route('/', methods= ['GET', 'POST'])
def get_message():
    if request.method == "GET":
        print("Got request in main function")
        return render_template("index.html")

@app.route('/upload_static_file', methods=['GET', 'POST'])
def upload_static_file():
    print("Got request in static files")

    target = os.path.join(APP__ROOT, 'audio_files/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("static_file"):
        print(file)
        filename = file.filename
        destination = '/'.join([target, filename])
        file.save(destination)

    deep_speech_transcriber.main()

    dir_path = os.getcwd()
    transcription_path = f"{dir_path}/transcription/"

    for item in os.listdir(transcription_path):
        with open(str(transcription_path + item), 'r') as f:
            text = f.read()
            jsonResp = {"success": True, "transcription": text}
            return jsonify(jsonResp), 200
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)