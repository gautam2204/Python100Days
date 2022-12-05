import os
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.chdir("C:\\")
print(os.getcwd())
os.chdir(r"C:\Users\gauta\OneDrive\Desktop")
print(os.listdir(r"C:\Users\gauta\OneDrive\Desktop"))


for file in os.listdir(r"C:\Users\gauta\OneDrive\Desktop"):
    if file.endswith("random.txt"):
        with open(file="random.txt", mode='r') as myFile:
            print(myFile.read())

os.chdir(r"D:\pyhton projects\UdemyLearningPython\Day24")

with open("../../UdemyLearningPython/Scratch.py",mode="r") as file:
    contents = file.read()
    print(contents)