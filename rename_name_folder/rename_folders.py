import os

# دریافت مسیر اسکریپت و تنظیم دایرکتوری کاری
file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(file_path)

print(f"Base Directory: {file_path}")

# دریافت لیست پوشه‌ها (فقط دایرکتوری‌ها)
dirs = [d for d in os.listdir() if os.path.isdir(d)]

p = 0
for d in dirs:
    new_name = d.lower()
    
    # جلوگیری از خطای نام تکراری
    if new_name != d and not os.path.exists(new_name):
        os.rename(d, new_name)
        print(f"Renamed Folder {p}: {d} → {new_name}")
    
    p += 1

print("All folder names converted to lowercase.")
