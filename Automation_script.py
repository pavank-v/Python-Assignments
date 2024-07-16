'''This Script will Move the Files in Downloads Folder to Appropriate Destination 
Based on the Extension Name'''

import os
import shutil
import collections

# All possible extensions
PICTURE_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'tif',
                      'webp', 'heif', 'heic', 'svg', 'cr2', 'nef', 'arw'
                      , 'psd', 'ico']
MUSIC_EXTENSIONS = ['mp3', 'wav', 'flac', 'aac', 'ogg', 'wma', 'm4a', 
                    'alac', 'aiff', 'dsd']
VIDEO_EXTENSIONS = ['mp4', 'mkv', 'mov', 'avi', 'wmv', 'flv', 'webm', 
                    'mpg', 'mpeg', '3gp']
DOCUMENT_EXTENSIONS = ['pdf', 'docx', 'doc', 'txt', 'xlsx', 'xls',
                       'pptx', 'ppt', 'odt', 'rtf']
COMPRESSED_EXTENSIONS = ['zip', 'rar', 'tar.gz', '7z', 'bz2', 'gz',
                         'xz', 'deb', 'z', 'pkg', 'rpm']
INSTALLATION_EXTENSIONS = ['exe', 'iso', 'dmg']

# Destination directories
BASE_PATH = os.path.expanduser('~')
DEST_PATH = {
    'Pictures': PICTURE_EXTENSIONS,
    'Music': MUSIC_EXTENSIONS,
    'Videos': VIDEO_EXTENSIONS,
    'Documents': DOCUMENT_EXTENSIONS,
    'Compressed Files': COMPRESSED_EXTENSIONS,
    'Installers': INSTALLATION_EXTENSIONS
}

# Create destination directories if they don't exist
for d in DEST_PATH.keys():
    dir_path = os.path.join(BASE_PATH, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

# Source directory
DOWN_PATH = os.path.join(BASE_PATH, 'Downloads')

# Collect files based on their extension
files = collections.defaultdict(list)#Using Defaultdict instead of dict to prevent key error
files_list = os.listdir(DOWN_PATH)

for file_name in files_list:
    if not file_name.startswith('.'):
        file_ext = file_name.split('.')[-1].lower()
        files[file_ext].append(file_name)

# Move files to respective directories
for ext, file_list in files.items():
    for file_name in file_list:
        source_path = os.path.join(DOWN_PATH, file_name)
        for dest, ext_list in DEST_PATH.items():
            if ext in ext_list:
                dest_path = os.path.join(BASE_PATH, dest, file_name)
                shutil.move(source_path, dest_path)
                print(f"Moved {file_name} to {dest}")

print("Organizing files complete.")
