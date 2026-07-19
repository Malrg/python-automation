# Python Automation

A collection of Python scripts focused on file management, organization and productivity.

## Current Project

### File Organizer

A Python script that automatically organizes files into folders based on their file type.

It can classify files into categories such as:

- Images
- Documents
- Spreadsheets
- Presentations
- Compressed files
- Audio
- Videos
- Others

## Features

- Automatically detects file extensions.
- Creates category folders when needed.
- Moves files into the appropriate folder.
- Prevents overwriting files with the same name.
- Displays a summary of all moved files.
- Uses only Python's standard library.

## Technologies

- Python
- `pathlib`
- `shutil`

## How to Use

1. Open `organizador_de_archivos.py`.
2. Edit the folder path inside the `main()` function:

```python
folder = Path("/storage/emulated/0/Download/OrganizadorPrueba").
