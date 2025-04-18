from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Diretório onde os vídeos estão armazenados
UPLOAD_FOLDER = 'D:\hard disk drive\andré criações\espaço mundo digital\streaming\categorias\séries\0-grachi 1 2 e 3 temporadas incompletas dubladas e legendadas\1 temporada incompleta-parte 1'  # Substitua pelo caminho onde seus vídeos estão armazenados
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Rota para a página inicial
@app.route('/')
def index():
    # Carregar a lista de vídeos
    videos = []
    for root, dirs, files in os.walk(app.config['UPLOAD_FOLDER']):
        for file in files:
            if file.endswith(('.mp4', '.avi', '.mkv')):  # Supondo que os vídeos sejam nesses formatos
                videos.append(os.path.join(root, file))
    
    return render_template('index.html', videos=videos)

# Rota para exibir vídeos selecionados
@app.route('/play_video', methods=['GET'])
def play_video():
    video_path = request.args.get('video_path')
    if video_path and os.path.exists(video_path):
        return jsonify({"status": "success", "video_path": video_path})
    else:
        return jsonify({"status": "error", "message": "Video not found!"})

# Iniciar o servidor com modo de depuração ativado
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
