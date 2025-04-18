from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    arquivos = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', arquivos=arquivos)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect('/')
    arquivo = request.files['file']
    if arquivo.filename != '':
        caminho = os.path.join(UPLOAD_FOLDER, arquivo.filename)
        arquivo.save(caminho)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
