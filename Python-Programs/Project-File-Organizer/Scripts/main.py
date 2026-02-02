import os
import shutil

# 🔥 IMPORTANT: Target folder path (CHANGE THIS)
FOLDER_PATH = r"/Users/shraddhamaheshwari/Data/Shraddha/data-analyst-portfolio/Python-Programs/Project-File-Organizer"
# Mac/Linux example:
# FOLDER_PATH = "/Users/yourname/Desktop/PYTHON-PROGRAMS/Project-File-Organizer"

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".odt"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".rb"],
}

# Create folders
for folder in FILE_TYPES:
    os.makedirs(os.path.join(FOLDER_PATH, folder), exist_ok=True)

# Organize files
for file in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, file)

    if os.path.isdir(file_path):
        continue

    file_ext = os.path.splitext(file)[1].lower()

    for folder, extensions in FILE_TYPES.items():
        if file_ext in extensions:
            shutil.move(
                file_path,
                os.path.join(FOLDER_PATH, folder, file)
            )
            break

print("Files organized successfully ✅")
