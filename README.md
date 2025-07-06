# File Organizer
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white) 
![License](https://img.shields.io/badge/License-MIT-green) 

A simple Python script that organizes files in a folder by moving them into subfolders based on their file types.

## How it works  
The script checks the files in the folder you specify and moves them into folders like `Images`, `Documents`, `Music`, etc., depending on their file extensions.


## Features

- 📂 Automatically sorts files into folders
- ⚡ Fast and easy to set up
- 🧩 Simple to customize and add more file types
- 💻 Works on Windows, Mac, and Linux
  
## How to Use

✅ Follow these simple steps to organize your files with this script:

1. 🔧 **Set your folder path:**  
   Open the `file_organizer.py` file in a text editor (Notepad++, VS Code, etc..).  
   Find the line that says:  
   ```python
   folder_to_organize = "C:/Users/.../Downloads"
   ```
   💾 Change the path inside the quotes to the folder you want to organize and save the file.
   
   Example:
   
   ```bash
   "C:/Users/YourName/Desktop/MyFiles"
   ```
2. ▶️ **Run the script:**  
   Open your terminal or command prompt.  
   Navigate to the folder where your script is saved by typing:  
   ```bash
   cd path/to/your/script/folder
   ```
   Then run the script by typing:
   ```bash
   python file_organizer.py
   ```

   
4. 📂 **Check your folder:**  
   Open the folder you set in the script.  
    Example:
   
     ```bash
     "C:/Users/YourName/Desktop/MyFiles"
     ```
You’ll see your files neatly sorted into new folders like `Images`, `Documents`, `Music`, and more.  
 

## Requirements  
- Python 3  
- No extra libraries needed

## Example Output
```bash
✅ Moved: photo.jpg           -> Images  
✅ Moved: song.mp3            -> Music  
⚠️ Skipped: randomfile.xyz    (no matching folder)  
🎉 Done organizing!
```
## ⭐️ Support

If you like this project, give it a ⭐️! It really helps!

<p align="center"> Made with ❤️ using Python </p> 
