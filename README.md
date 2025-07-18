# Bulk File Renamer

A simple Python script to batch rename files in a folder by adding a custom suffix to all files of a specific extension.

---

## 🔧 Features

- Rename all files with a given extension in a folder
- Adds a custom suffix before the file extension
- Command-line input for flexibility
- Minimal and beginner-friendly

---

## 🚀 Usage

#### 1. Clone this repository or download the `main.py` file.
#### 2. Run the script:

```bash
python main.py
```

---

#### Provide the following inputs when prompted:

Folder path: Path where your files are stored

Extension: File type (e.g., .png, .jpg, .txt)

Suffix: Text to append before the extension (e.g., _edited)

---

## 🔄 Example
Suppose your folder contains:
```
invoice.txt
notes.txt
photo.jpg
```

#### Input:

```
Folder path: ./documents
Extension: .txt
Suffix: _v2
```

#### After running, renamed files will be:

```
invoice_v2.txt
notes_v2.txt
photo.jpg  # unchanged (not .txt)
```

---

## 📂 Project Structure
```
bulk-file-renamer/
├── main.py
├── README.md
└── .gitignore
```

---

## 📝 License
This project is licensed under the MIT License. See the LICENSE file for details.
