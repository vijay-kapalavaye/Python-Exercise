f=open("myfile.txt","r")
print(f.read())
f.close()

with open("myfile.txt","r")as f1:
    print(f1.read())