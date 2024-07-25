"""
Python Dictionary / JSON
Dictionary khusus di python
JSON penggunaan secara umum
"""
users = { #dictionary ditandai dengan kurung kurawal
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
}

print("\nDictionary")
print(users) #jika ingin menampilkan semua
print(users["name"]) #jika ingin menampilkan satu persatu

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

print("\nDictionary di dalam dictionary")
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

print("\nDictionary dalam dictionary di dalam dictionary")
print(users)
print(users["address"]["geo"]["lat"]) #print dictionary dalam dictionary di dalam dictionary


#Merubah python dictionary menjadi JSON
print("\nMerubah dictionary ke JSON")
import json #ini adalah package python untuk merubah dictionary ke JSON
result = json.dumps(users)
print(result) #lihat hasilnya, jika dictionary menggunakan ", JSON menggunakan '.
