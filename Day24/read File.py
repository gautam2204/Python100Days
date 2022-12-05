with open("myFile.txt","r") as file:
    #print(file.write("\nHellow from Program"))
    content = file.read()
    print(content)