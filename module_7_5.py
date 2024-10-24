import os
from datetime import datetime

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.stat(file).st_mtime
        formatted_time = datetime.fromtimestamp(filetime).strftime('%Y.%m.%d %H:%M:%S')
        filesize = os.stat(file).st_size
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
