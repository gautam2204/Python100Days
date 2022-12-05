import csv
lst_of_data=[]
with open("weather_data.csv","r") as file:

    line = file.readlines()
    lst_of_data.append(line)

print(lst_of_data)
lst_of_temp=[]
with open("weather_data.csv","r") as file:
    data = csv.reader(file)
    print(type(data))
    for line in data:
        print(line)

        if line[1].isdigit():
            lst_of_temp.append(line[1])

print(lst_of_temp)
