'''
jsonschema2popo2 -o '.\Day30\playing with json\popo.py' '.\Day30\playing with json\sample.json'
'''
import json

import popo

val_page = 2
per_page = 6
total = 12
total_pages = 2

first_dic = {
    "id": 7,
    "email": "michael.lawson@reqres.in",
    "first_name": "Michael",
    "last_name": "Lawson",
    "avatar": "https://reqres.in/img/faces/7-image.jpg"
}
sec_dict = {
            "id": 7,
            "salary": 90000,
            "first_name": "Michael"
        }

url = "https://reqres.in/#support-heading"
text = "To keep ReqRes free, contributions towards server costs are appreciated!"

list_of_dict = [first_dic,sec_dict]
datum_obj = popo.Datum(id=first_dic["id"],email=first_dic["email"],first_name=first_dic["first_name"]
                       ,last_name=first_dic["last_name"],avatar=first_dic["avatar"])
datum_obj1 = popo.Datum(id=first_dic["id"],email=first_dic["email"],first_name=first_dic["first_name"]
                       ,last_name=first_dic["last_name"],avatar=first_dic["avatar"])

support_obj = popo.Support(url=url, text=text)

welcom_Obj = popo.Welcome10(page=val_page, per_page=per_page, total=total, total_pages=total_pages, data=[datum_obj,datum_obj1],
                           support=support_obj)

"""welcom_Obj._set_page(value=val_page)
welcom_Obj._set_per_page(value=per_page)
welcom_Obj._set_total(value=total)
welcom_Obj._set_total_pages(value=total_pages)"""

"""
popo.Welcome8._set_page(value=val_page)
popo.Welcome8._set_per_page(value=per_page)
popo.Welcome8._set_total(value=total)
popo.Welcome8._set_total_pages(value=total_pages)
"""
var=welcom_Obj.to_dict()
print(var)
myJson = json.dumps(var,indent=4)
print(myJson)
