# Image Renamer Script

[🇮🇷 فارسی](README.fa.md) | [🇬🇧 English](README.md)

## Description
This Python script is designed to rename JPG image files in a directory. Its primary purpose is to transform long, unreadable, or hashed filenames into simple, meaningful names suitable for dataset management. For example, it can rename image files in a folder of oranges to `orange1.jpg`, `orange2.jpg`, etc.

## Prerequisites
- Python 3.x
- `os` module (included by default in Python)

## Usage
1. Place the script in the directory containing the JPG files or adjust the directory path in the code.
2. Set your desired base name (prefix) in the code (e.g., replace `cls` with `orange`).
3. Run the script:
   ```bash
   python script.py
   ```

## Features
- Converts complex names to a simple, readable format (e.g., `orange1.jpg`)
- Automatically assigns sequential numbers to files
- Checks for existing files to avoid overwriting
- Case-insensitive handling of the `.jpg` extension

## Example
**Before running:**
```
- abc123hashxyz.jpg
- def456hashuvw.jpg
- ghi789hashrst.jpg
```

**After running (with base_name="orange"):**
```
- orange1.jpg
- orange2.jpg
- orange3.jpg
```

## Notes
- The script only processes files with the `.jpg` extension.
- It won’t overwrite existing files with the new name (due to the `if old_name != new_name` check).
- To use with other extensions (e.g., `.png`), modify the `endswith('.jpg')` condition.

## Development
For suggestions or bug reports, please open an issue or submit a pull request.

## License
This project is licensed under the [License](LICENSE.md).
