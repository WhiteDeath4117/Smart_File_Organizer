# Smart_File_Organizer
# Folder Organizer

A lightweight Python script to automatically organize messy folders by grouping files into categorized subdirectories based on their extensions.

## ✨ Features

- **Automatic categorization** – Moves files into folders like `Images`, `Documents`, `Videos`, etc.
- **Extensible mapping** – Easily add or modify file extension rules.
- **Safe operation** – Only processes files; subdirectories are left untouched.
- **Detailed logging** – Every move (and error) is recorded in `organizer.log` with timestamps.
- **Interactive mode** – Run once manually, or enable continuous background watching every 30 minutes.

## 📁 How It Works

1. You provide a folder path.
2. The script scans all **files** inside (subfolders are ignored).
3. Each file’s extension is checked against a built‑in lookup table.
4. Files are moved into a matching subfolder (e.g., `.jpg` → `Images`).
5. If a subfolder doesn’t exist, it is created automatically.
6. Every action is printed to the console and logged to `organizer.log`.

Files with unmapped extensions go to the `Others/` folder.

## 🚀 Usage

### Prerequisites
- Python 3.6+ (standard libraries only – no external packages required).

### Running the script

```bash
python organizer.py
```

You’ll be prompted to enter the full path of the folder you want to organize, for example:

```
Enter the full path of the folder to organize: C:\Users\Name\Downloads
```

The script will immediately move files and display a summary.

### Example output

```
Moved: photo.jpg → Images/
Moved: report.pdf → Documents/
Moved: movie.mp4 → Videos/

✅ Organized 3 file(s)!
```

### Continuous mode

The script includes a commented‑out loop that re‑runs the organizer every 30 minutes. To enable it, uncomment the `while True:` block at the bottom of `organizer.py`.

```python
if __name__ == "__main__":
    # organize_folder()   # single run
    while True:           # continuous mode
        organize_folder()
        wait_minutes = 30
        print(f"⏳ Sleeping for {wait_minutes} minutes...")
        time.sleep(wait_minutes * 60)
```

## 📋 Default Extension Mapping

| Category   | Extensions                                         |
|------------|---------------------------------------------------|
| Images     | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`           |
| Documents  | `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`, `.csv`, `.md`, `.yaml` |
| Videos     | `.mp4`, `.mkv`, `.avi`, `.mov`                    |
| Code       | `.py`, `.js`, `.html`, `.css`, `.java`            |
| Archives   | `.zip`, `.rar`                                    |
| Music      | `.mp3`                                            |
| Others     | Everything else (including files with no extension) |

## 🛠 Customizing the Mapping

Open `organizer.py` and edit the `EXTENSION_MAP` dictionary. Use lowercase keys, and map each extension to the folder name you prefer.

Example – adding `.iso` to `"Disc Images"`:

```python
EXTENSION_MAP = {
    ...
    ".iso": "Disc Images",
    ...
}
```

## 📄 Logging

All actions are appended to `organizer.log` in the same directory as the script. Each entry includes a UTC timestamp and a description of what was moved or any errors encountered.

Example log lines:

```
[Wed Apr 29 10:15:23 2026] Moved: photo.jpg → Images/
[Wed Apr 29 10:15:23 2026] Error moving important.docx: [Errno 13] Permission denied
[Wed Apr 29 10:15:23 2026] --- Finished organizing 12 file(s) ---
```

## 🤝 Contributing

Feel free to fork the repository and submit pull requests. Ideas for improvements:
- Add a graphical interface
- Support for organizing subfolders recursively
- Custom regex‑based mappings

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
