import os
import shutil
import time

# ================== EXTENSION MAPPING ==================
EXTENSION_MAP = {
    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    # Documents
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",       # data.csv
    ".md": "Documents",        # README.md
    ".yaml": "Documents",      # config.yaml
    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    # Code
    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",
    ".java": "Code",
    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    # Music
    ".mp3": "Music",
    # Others (explicit map just for completeness)
    ".xyz": "Others",          # unknown_file.xyz
    "": "Others"               # no_extension_file
}

# ================== HELPER FUNCTIONS ==================
def get_destination(extension):
    return EXTENSION_MAP.get(extension.lower(), "Others")

def log_move(message):
    timestamp = time.ctime()
    with open("organizer.log", "a") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")

# ================== CORE ORGANIZER ==================
def organize_folder():
    folder_path = input("Enter the full path of the folder to organize: ").strip()
    
    # Validate path
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return
    if not os.path.isdir(folder_path):
        print("❌ That is not a directory.")
        return
    
    # List only files (ignore subfolders)
    all_items = os.listdir(folder_path)
    only_files = [item for item in all_items
                  if os.path.isfile(os.path.join(folder_path, item))]
    
    if not only_files:
        print("📭 No files to organize.")
        return

    moved_count = 0
    for filename in only_files:
        file_extension = os.path.splitext(filename)[1]   # e.g., ".txt"
        destination_folder_name = get_destination(file_extension)
        dest_dir = os.path.join(folder_path, destination_folder_name)

        try:
            # Create destination folder if it doesn't exist
            os.makedirs(dest_dir, exist_ok=True)
            
            src_path = os.path.join(folder_path, filename)
            dest_path = os.path.join(dest_dir, filename)
            
            shutil.move(src_path, dest_path)
            moved_count += 1
            
            message = f"Moved: {filename} → {destination_folder_name}/"
            print(message)
            log_move(message)
            
        except Exception as e:
            error_msg = f"Error moving {filename}: {e}"
            print(error_msg)
            log_move(error_msg)

    # Summary AFTER the loop
    print(f"\n✅ Organized {moved_count} file(s)!")
    log_move(f"--- Finished organizing {moved_count} file(s) ---\n")

# ================== MAIN EXECUTION ==================
if __name__ == "__main__":
    # ---- For a single run (test first!) ----
    organize_folder()

    # ---- Uncomment below to run continuously every 30 minutes ----
    # while True:
    #     organize_folder()
    #     wait_minutes = 30
    #     print(f"⏳ Sleeping for {wait_minutes} minutes...")
    #     time.sleep(wait_minutes * 60)