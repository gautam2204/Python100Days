weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
#(temp_c * 9/5) + 32 = temp_f

weather_f = {k:(v * 9/5) + 32 for (k,v) in weather_c.items()}
print(weather_f)
