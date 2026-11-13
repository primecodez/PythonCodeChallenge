import os
import shutil
import logging
from datetime import datetime

# Optional Level Up: Set up logging
log_filename = os.path.expanduser('~/Downloads/organizer_log.txt')
logging.basicConfig(
    filename=log_filename, 
    level=logging.INFO, 
    format='%(asctime)s - %(message)s'
)

def organize_folder(folder_path):
    # 1. Define target folders and their associated extensions
    FILE_TYPES = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.md'],
        'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Code': ['.py', '.html', '.css', '.js', '.json', '.sql', '.sh']
    }

    # 2. Flatten dictionary for quick lookup: {'.jpg': 'Images', '.pdf': 'Documents'}
    extension_map = {ext: folder for folder, exts in FILE_TYPES.items() for ext in exts}

    # 3. Traverse the directory
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # 4. String manipulation: extract the extension
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # Skip files with no extension or the log file itself
        if not extension or filename == 'organizer_log.txt':
            continue

        # 5. Route to correct folder, default to 'Others'
        target_folder_name = extension_map.get(extension, 'Others')
        target_folder_path = os.path.join(folder_path, target_folder_name)

        # Create the destination folder if it doesn't exist
        os.makedirs(target_folder_path, exist_ok=True)

        # 6. Move the file
        target_file_path = os.path.join(target_folder_path, filename)
        try:
            shutil.move(file_path, target_file_path)
            logging.info(f"Moved {filename} -> {target_folder_name}/")
            print(f"Moved: {filename} -> {target_folder_name}/")
        except Exception as e:
            logging.error(f"Failed to move {filename}: {e}")

if __name__ == "__main__":
    # os.path.expanduser('~') dynamically gets your user directory (C:\Users\Name or /home/name)
    downloads_path = os.path.expanduser('~/Downloads')
    
    # Ensure the path exists before running
    if os.path.exists(downloads_path):
        organize_folder(downloads_path)
    else:
        print(f"Path not found: {downloads_path}")