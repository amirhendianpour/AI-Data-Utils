# Dataset Splitter

This Python script is designed to split an image dataset into three parts: `train`, `valid`, and `test`. The default split ratio is 70% for training, 20% for validation, and 10% for testing.

## Features
- Splits images into `train`, `valid`, and `test` sets.
- Maintains class names in the output structure.
- Customizable split ratios.
- Supports `jpg`, `jpeg`, and `png` image formats.
- Uses `shutil` for efficient file copying.

## Requirements
- Python 3
- Standard libraries: `os`, `shutil`

## Usage

1. Set the input dataset path in the `dataset_dir` variable.
2. Define the output directory in `output_dir`.
3. Adjust the split ratios using `train_ratio`, `valid_ratio`.
4. Run the script:

```bash
python split_dataset.py
```

## Output Folder Structure

After execution, the output directory will be structured as follows:
```
output_dir/
├── train/
│   ├── class_1/
│   ├── class_2/
│   ├── ...
├── valid/
│   ├── class_1/
│   ├── class_2/
│   ├── ...
└── test/
    ├── class_1/
    ├── class_2/
    ├── ...
```

## Important Notes
- The input folder should contain subdirectories, each representing a class.
- Class names remain unchanged in the output directory.
- If the output directory does not exist, it will be created automatically.

## Contributing
If you have suggestions or improvements for this script, feel free to contribute on [GitHub](https://github.com/amirhendianpour).

