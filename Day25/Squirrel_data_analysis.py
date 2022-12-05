import pandas


squirrel_data_frame = pandas.read_csv("Squirrel_Data.csv")

grey_len =  len(squirrel_data_frame[squirrel_data_frame["Primary Fur Color"]=="Gray"])
red_len =  len(squirrel_data_frame[squirrel_data_frame["Primary Fur Color"]=="Cinnamon"])
black_len =  len(squirrel_data_frame[squirrel_data_frame["Primary Fur Color"]=="Black"])

data_dict = {
    "Primary Colour":["Gray","Red","Black"],
    "Count":[grey_len,red_len,black_len]
}
data_frame = pandas.DataFrame(data=data_dict)
data_frame.to_csv("Sorted squirrel Data.csv")


