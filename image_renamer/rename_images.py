import os

# تنظیم مسیر به دایرکتوری اسکریپت
file_path = os.path.dirname(os.path.realpath(__file__))
if file_path != os.getcwd():
    os.chdir(file_path)

# تنظیم نام پایه برای فایل‌ها
base_name = "orange"  # این مقدار را بر اساس نیاز خود تغییر دهید

# گرفتن فقط فایل‌های JPG
jpg_files = [f for f in os.listdir() if f.lower().endswith('.jpg')]

# تغییر نام فایل‌ها
for count, old_name in enumerate(jpg_files, 1):
    new_name = f'{base_name}{count}.jpg'
    if old_name != new_name:
        os.rename(old_name, new_name)
