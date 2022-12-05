prog_dict = {
    "Bug": "issue",
    "loop":"circle",
    1:"one"
}

print(type(prog_dict))
print(prog_dict["loop"])

prog_dict["Happy"]="Charlie"

print(prog_dict)

prog_dict["Bug"]="New Bug"

print(prog_dict)

for key in prog_dict:
    print(prog_dict[key])