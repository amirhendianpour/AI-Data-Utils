import os

# دریافت مسیر اسکریپت و تغییر دایرکتوری کاری
file_path = os.path.dirname(os.path.realpath(__file__))
if not file_path == os.getcwd():
    os.chdir(file_path)

# دریافت لیست فایل‌ها
a = os.listdir()
count = 1

for i in a:
    if i.lower().endswith(".jpg"):
        new_name = f'cls{count}.jpg'
        
        # بررسی اینکه نام جدید وجود دارد یا نه
        while os.path.exists(new_name):
            count += 1
            new_name = f'cls{count}.jpg'
        
        os.rename(i, new_name)
        count += 1
