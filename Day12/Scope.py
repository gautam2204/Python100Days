enemies = ["skeleton", "zombie", "ghost"]
stringVar = "a"
newVariable = "abc"


def getName():
    enemies.append("Happy")
    global stringVar
    stringVar = "Changed to Bar"
    print(enemies)
    global newVariable
    newVariable += "ab"



getName()
print(newVariable)
print(stringVar)
