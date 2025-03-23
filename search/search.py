import os

def find_png_files(directory):
    png_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".png"):  # چک کردن با حروف کوچک برای جلوگیری از مشکلات
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)  # سایز فایل به بایت
                png_files.append((file_path, file_size))
    return png_files

# استفاده از تابع
directory = "D:/arman-archive/dataset_all_plant"  # جایگزین با مسیر دلخواه
png_files = find_png_files(directory)

# نمایش نتیجه
if png_files:
    print(f"\n🔍 Found {len(png_files)} PNG files in '{directory}'\n")
    for file_path, file_size in png_files:
        size_kb = file_size / 1024  # تبدیل بایت به کیلوبایت
        print(f"📄 File: {file_path}, Size: {size_kb:.2f} KB")
else:
    print("❌ No PNG files found.")
