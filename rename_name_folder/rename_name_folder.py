import os

file_path = os.path.dirname(os.path.realpath(__file__))
if not file_path == os.getcwd():
    os.chdir(file_path)

print(file_path)
dir = os.listdir()

p=0
for d in dir:
    if os.path.isdir(d):
        os.rename(d, d.lower())
        print(p)
        p+=1
print("end")

