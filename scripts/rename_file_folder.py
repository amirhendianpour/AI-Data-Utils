import os

file_path = os.path.dirname(os.path.realpath(__file__))
if not file_path == os.getcwd():
    os.chdir(file_path)

print(file_path)
dir = os.listdir()
os.chdir(dir[0])
# print(os.getcwd())
p=0
for d in dir:
    if os.path.isdir("..\\"+d):
        os.chdir(file_path + '\\' + d)
        a = os.listdir()
        count=1
        for i in a:
            if i[-3:] =="jpg" or i[-3:] =="JPG":
                os.rename(i,'lol'+ str(count) +'.jpg')
                count =count+1
        print(p)
        p+=1
print("end")

