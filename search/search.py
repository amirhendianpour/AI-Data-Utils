import os

def find_png_files(directory):
    png_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".png") or file.endswith(".PNG"):
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)  # سایز فایل به بایت
                png_files.append((file_path, file_size))
    return png_files

# استفاده از تابع
directory = "D:/arman-archive/dataset_all_plant"  # جایگزین کنید با مسیر پوشه‌ی خود
png_files = find_png_files(directory)
for file_path, file_size in png_files:
    print(f"File: {file_path}, Size: {file_size} bytes")
