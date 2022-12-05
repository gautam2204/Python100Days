from customError import CustomIndexError
fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError as inderr:
        print(f"Index is out of range {inderr}")





def make_pie2(index):
    if index>len(fruits):
        raise CustomIndexError("This is custom Error")
    else:
        fruit = fruits[index]
        print(fruit + " pie")


make_pie(4)
make_pie2(4)


