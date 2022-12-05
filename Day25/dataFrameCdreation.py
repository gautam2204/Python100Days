import pandas
students = {"Name":"Gautam",
            "marks":[21,25,4,19]}

data_frame = pandas.DataFrame(data=students)
print(data_frame)
data_frame.to_csv("created_csv")