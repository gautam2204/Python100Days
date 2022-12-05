travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(county,no_of_visits,cities):
  new_visit_details={"country":county
                     ,"visits":no_of_visits
                     ,"cities":cities}
  travel_log.append(new_visit_details)




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


def totalCountries(travel_log):
  for dictElm in travel_log:
    print(dictElm["country"])


totalCountries(travel_log)


def totalCities(travel_log):
  cityList=[]
  for dictElm in travel_log:
    for city in dictElm["cities"]:
       cityList.append(city)

  print(cityList)


totalCities(travel_log)

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []}
}

print(order["main"][2])
import json

print(json.dumps(order,indent=4))


order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: "[]"}
}
with open("Sample.json","w") as file:
  file.write(json.dumps(order))
