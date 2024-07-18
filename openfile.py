
try:
    with open("myfile1.txt","r")as f1:
        print(f1.read())
except FileNotFoundError as e:
    print(f"error- {e}")


f=open("myfile.txt","r")
print(f.read())
f.close()