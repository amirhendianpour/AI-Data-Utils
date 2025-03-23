import os

# دریافت مسیر اسکریپت و تغییر دایرکتوری کاری
file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(file_path)

print(f"Base Directory: {file_path}")

# دریافت لیست دایرکتوری‌ها
dirs = [d for d in os.listdir() if os.path.isdir(d)]

p = 0
for d in dirs:
    folder_path = os.path.join(file_path, d)
    os.chdir(folder_path)

    # دریافت لیست فایل‌ها
    images = [f for f in os.listdir() if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    
    count = 1
    for img in images:
        new_name = f'lol{count}.jpg'
        
        # بررسی اینکه فایل جدید از قبل وجود دارد یا نه
        while os.path.exists(new_name):
            count += 1
            new_name = f'lol{count}.jpg'
        
        os.rename(img, new_name)
        count += 1

    print(f"Processed Folder {p}: {d}")
    p += 1

print("Renaming Completed!")
