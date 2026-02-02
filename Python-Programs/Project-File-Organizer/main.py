import os
import shutil

# Folder path you want to organize
FOLDER_PATH = os.getcwd()  # Change this to your target folder path if needed
# Define file type categories and their corresponding extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".odt"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".rb"],
}
# Create Folders if they don't exist
for folder in FILE_TYPES.keys(): # Create folder for each folder
    folder_path = os.path.join(FOLDER_PATH, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path) # os.path.exists() checks if the folder already exists
# Organize files
for file in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, file)

    # Skip folders
    if os.path .isdir(file_path):
        continue 

# Get file extension
# print(os.path.splitext(file))
file_ext = os.path.splitext(file)[1].lower()



