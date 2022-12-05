#try , except , else , finally

try:
    with open("hello.json","r") as file:
        file.read()
    myDict = {"Hello":"World","NotHello":"EveryDay"}
    myVal = myDict["not"]
except FileNotFoundError as fileError:
    print(f"File was not found with error '{fileError}'")
    with open("hello.json", "w") as file:
        file.write("Wrote something")
except KeyError as keyerror:
    print(f"Key not found '{keyerror}'")
else:
    print("If try is successful")
finally:
    print("Got caught")