from flask import Flask, request, jsonify
from auth import authenticate
from downloader import download_media
from user_info import get_user_info

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    L = authenticate(username, password)
    if L:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "error", "message": "Failed to authenticate"})

@app.route('/user_info', methods=['GET'])
def user_info():
    username = request.args.get('username')
    user_info = get_user_info(username)
    return jsonify(user_info)

@app.route('/download_image', methods=['GET'])
def download_image():
    url = request.args.get('url')
    result = download_media(url, 'image')
    return jsonify(result)

@app.route('/download_video', methods=['GET'])
def download_video():
    url = request.args.get('url')
    result = download_media(url, 'video')
    return jsonify(result)

@app.route('/download_story', methods=['GET'])
def download_story():
    url = request.args.get('url')
    result = download_media(url, 'story')
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
