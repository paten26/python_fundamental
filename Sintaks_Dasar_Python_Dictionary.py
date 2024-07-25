"""
Python Dictionary / JSON
"""
users = { #dictionary ditandai dengan kurung kurawal
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
}

print (users) #jika ingin menampilkan semua
print (users["name"]) #jika ingin menampilkan satu persatu

#Dictionary di dalam dictionary
users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light", #dictionary di dalam dictionary
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
    }
}

print(users)
print(users["address"])
print(users["address"]["street"])

#Dictionary dalam dictionary di dalam dictionary :)
users = {
"id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159", #dictionary dalam dictionary di dalam dictionary
            "lng": "81.1496"
        }
    }
}

print(users)
print(users["address"]["geo"]["lat"]) #print dictionary dalam dictionary di dalam dictionary