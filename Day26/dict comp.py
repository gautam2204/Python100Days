sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

#lst_of_words=sentence.split(" ")

result = {i:len(i) for i in sentence.split(" ")}


print(result)