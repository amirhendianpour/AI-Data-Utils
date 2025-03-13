import os

file_path = os.path.dirname(os.path.realpath(__file__))

if not file_path == os.getcwd():
    os.chdir(file_path)

a = os.listdir()
count=1
for i in a:
    if i[-3:] =="jpg" or i[-3:] =="JPG":
        os.rename(i,'cls'+ str(count) +'.jpg')
        count =count+1

