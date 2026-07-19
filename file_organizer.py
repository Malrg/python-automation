from pathlib import Path
import shutil


CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".odt"},
    "Spreadsheets": {".xls", ".xlsx", ".csv", ".ods"},
    "Presentations": {".ppt", ".pptx", ".odp"},
    "Compressed": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Audio": {".mp3", ".wav", ".aac", ".ogg", ".flac"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov", ".webm"},
}


def get_category(extension: str) -> str:
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"


def get_unique_destination(destination: Path) -> Path:
    if not destination.exists():
        return destination

    counter = 1
    while True:
        new_name = f"{destination.stem}_{counter}{destination.suffix}"
        new_destination = destination.with_name(new_name)

        if not new_destination.exists():
            return new_destination

        counter += 1


def organize_files(folder: Path) -> None:
    moved_files = 0

    for item in folder.iterdir():
        if not item.is_file():
            continue

        if item.name == Path(__file__).name:
            continue

        category = get_category(item.suffix.lower())
        category_folder = folder / category
        category_folder.mkdir(exist_ok=True)

        destination = get_unique_destination(category_folder / item.name)
        shutil.move(str(item), str(destination))

        print(f"Moved: {item.name} -> {category}/{destination.name}")
        moved_files += 1

    print(f"\nFinished. Total files moved: {moved_files}")


def main() -> None:
    folder = Path("/storage/emulated/0/Download/OrganizadorPrueba")

    if not folder.exists():
        print("The Download folder was not found.")
        return

    organize_files(folder)


if __name__ == "__main__":
    main()