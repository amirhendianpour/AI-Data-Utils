# PNG File Finder

[🇮🇷 فارسی](README.fa.md) | [🇬🇧 English](README.md)

This Python script searches for all `.png` files in a specified directory (including subdirectories)  
and displays their file paths along with their sizes.

## Features
✔ Recursively scans all subdirectories.  
✔ Detects both `.png` and `.PNG` file extensions.  
✔ Displays file sizes in a human-readable format (KB).  
✔ Prevents case sensitivity issues with file extensions.  

## Prerequisites
- Python 3.x

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/amirhendianpour/[project-name].git
   ```
2. Navigate to the project directory:
   ```bash
   cd [project-name]
   ```

## Usage
1. Update the `directory` variable in `find_png.py` with the desired folder path:
   ```python
   directory = "D:/your-directory"
   ```
2. Run the script:
   ```bash
   python find_png.py
   ```
3. The script will output a list of all PNG files along with their sizes.

## Example Output
```
🔍 Found 5 PNG files in 'D:/images'

📄 File: D:/images/photo1.png, Size: 120.50 KB
📄 File: D:/images/subfolder/image2.png, Size: 98.75 KB
```

## Project Structure
```
[project-name]/
│
├── find_png.py       # Main script
├── README.md         # Documentation
└── sample_images/    # Example folder (optional)
```

## Developer
- [Your Name] - [Your Email](mailto:amir.hendianpour@gmail.com)

## License
