import os
import shutil

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return

    file_types = {
        "Images": [".jpg", ".png", ".jpeg"],
        "Documents": [".txt", ".docx"],
        "PDFs": [".pdf"]
    }

    files = os.listdir(folder_path)

    if len(files) == 0:
        print("📂 Folder is empty.")
        return

    for file in files:
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            moved = False

            for folder_name, extensions in file_types.items():
                if file.lower().endswith(tuple(extensions)):
                    # "pic.jpg".endswith(".jpg") → True
                    dest_folder = os.path.join(folder_path, folder_name)
                    os.makedirs(dest_folder, exist_ok=True)

                    shutil.move(file_path, os.path.join(dest_folder, file))
                    print(f"Moved {file} → {folder_name}")
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(other_folder, file))
                print(f"Moved {file} → Others")

def main():
    print("=== File Organizer ===")
    folder = input("Enter folder path: ")

    organize_files(folder)

    print("\n✅ Done organizing files!")

if __name__ == "__main__":
    main()