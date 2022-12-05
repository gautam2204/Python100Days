import pandas

data=pandas.read_csv("weather_data.csv")
print(data)
print(type(data))

print(data["temp"][3])
mean = data["temp"].mean()
print(mean)
dict_obj=data.to_dict()
print(dict_obj)

print(f"max is {data['temp'].max()}")
print(data.condition)
print(data[data.temp==data['temp'].max()])

monday_row = data[data.day=="Monday"]
monday_temp = monday_row.temp
print(monday_temp)