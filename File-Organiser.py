import os
import shutil

# Change this to the folder you want to organize
folder_to_organize = "C:/Users/Ben/Downloads"

# File types and their folders
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".sh"],
}

def organize_files(folder):
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            extension = os.path.splitext(filename)[1].lower()
            moved = False
            for folder_name, extensions in file_types.items():
                if extension in extensions:
                    new_folder = os.path.join(folder, folder_name)
                    if not os.path.exists(new_folder):
                        os.makedirs(new_folder)
                    shutil.move(filepath, os.path.join(new_folder, filename))
                    print(f"Moved: {filename} -> {folder_name}")
                    moved = True
                    break
            if not moved:
                print(f"Skipped: {filename} (no matching folder)")

if __name__ == "__main__":
    organize_files(folder_to_organize)
    print("Done organizing!")
