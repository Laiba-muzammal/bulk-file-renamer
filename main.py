import os

def rename_files(path, extension, suffix):
    if not os.path.exists(path):
        print(f"Error: The path '{path}' does not exist.")
        return

    renamed = False
    for filename in os.listdir(path):
        if filename.endswith(extension):
            name_without_ext = os.path.splitext(filename)[0]
            new_name = name_without_ext + suffix + extension
            src = os.path.join(path, filename)
            dst = os.path.join(path, new_name)
            os.rename(src, dst)
            print(f"Renamed: {filename} ➝ {new_name}")
            renamed = True

    if not renamed:
        print(f"No {extension} files found to rename.")

if __name__ == "__main__":
    folder_path = input("Enter folder path: ").strip()
    extension = input("Enter file extension (like .png, .jpg, .txt): ").strip()
    suffix = input("Enter suffix to add (like _renamed): ").strip()

    rename_files(folder_path, extension, suffix)
