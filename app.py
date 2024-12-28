from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
   os.makedirs(UPLOAD_FOLDER)

# Configuring flask to receive 10MB files
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 # 10MB

@app.route('/')
def home():
   return render_template("home.html")

@app.route('/record')
def record():
   return render_template("generate.html")

@app.route('/upload', methods=['POST'])
def upload_audio():
   if 'audio' not in request.files:
      # return jsonify({"error": "No audio file part"}), 400
      return render_template("error.html")
   
   audio_file = request.files['audio']
   if audio_file.filename == '':
      #  return jsonify({"error": "No selected file"}), 400
      return render_template("error.html")
   
   file_path = os.path.join(UPLOAD_FOLDER, audio_file.filename)
   audio_file.save(file_path)

   return jsonify({"message:" f"Audio saved successfully. {file_path}"}), 200

@app.route('/generate')
def generate():
   print("Generating...")

if  __name__ == '__main__':
   app.run(debug=True)
