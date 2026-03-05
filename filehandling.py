import os

path=os.path.join(os.getcwd(),"test")

with open(path,"r") as file:
    data=file.read(5)
    print(data)
    print(file.tell())
    file.seek(0)
    print(file.tell())




