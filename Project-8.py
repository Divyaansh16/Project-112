import os
import shutil
source=r"C:/Users/Secret user/Desktop/Web-Work/Whitehat Junior/Python/Project/Project-8/Document_files"
destination=r"C:/Users/Secret user/Desktop/Web-Work/Whitehat Junior/Python/Project/Project-8/Downloads"
listoffiles=os.listdir(source)
for i in listoffiles:
    name,extension=os.path.splitext(i)
    print(name)
    print(extension)
    if extension=="":
        continue
    if extension in ['.txt','.doc','.docx','.pdf']:
        path1=source+'/'+i
        path2=destination+'/'
        path3=destination+'/'+i
        if os.path.exists(path2):
            print("Moving...",i)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving...",+i)
            shutil.move(path1,path3)
print("Done")