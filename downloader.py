import os
import requests
from datetime import datetime

def download_media(url, media_type):
    try:
        if media_type not in ['image', 'video', 'story']:
            return {"error": "Tipe media tidak valid. Pilih 'image', 'video', atau 'story'."}

        response = requests.get(url)
        if response.status_code == 200:
            save_dir = './assets/result/'
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            if media_type == 'image':
                file_path = os.path.join(save_dir, f'image_{timestamp}.jpg')
            elif media_type == 'video':
                file_path = os.path.join(save_dir, f'video_{timestamp}.mp4')
            elif media_type == 'story':
                file_path = os.path.join(save_dir, f'story_{timestamp}.mp4')

            with open(file_path, 'wb') as f:
                f.write(response.content)

            log_download_activity(url, media_type, file_path)

            response_data = {
                "status": "success",
                "file_name": os.path.basename(file_path),
                "file_path": file_path,
                "media_type": media_type
            }
            return response_data
        else:
            return {"error": "Gagal mengunduh media"}
    except Exception as e:
        return {"error": str(e)}

def log_download_activity(url, media_type, file_path):
    log_dir = './assets/log/'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file = os.path.join(log_dir, 'download_log.txt')
    log_entry = f"{datetime.now()} - Media type: {media_type}, URL: {url}, File path: {file_path}\n"
    with open(log_file, 'a') as f:
        f.write(log_entry)
