thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': '1964'}

print(thisdict["brand"])
# Ford

print(len(thisdict))
# 3

print(type(thisdict))
# <class 'dict'>

x = thisdict["model"]
print(x)
# Mustang

x = thisdict.get("model")
print(x)
# Mustang

x = thisdict.keys()
print(x)
# dict_keys(['brand', 'model', 'year'])

x = thisdict.values()
print(x)
# dict_values(['Ford', 'Mustang', '1964']) 

x = thisdict.items()
print(x)
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', '1964')])

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)
# dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x)
# dict_keys(['brand', 'model', 'year', 'color'])

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)
# dict_values(['Ford', 'Mustang', 1964])

car["year"] = 2020

print(x)
# dict_values(['Ford', 'Mustang', 2020])

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)
# dict_values(['Ford', 'Mustang', 1964])

car["color"] = "red"

print(x)
# dict_values(['Ford', 'Mustang', 1964, 'red'])

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x)
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["year"] = 2020

print(x)
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x)
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["color"] = "red"

print(x)
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
# Yes, 'model' is one of the keys in the thisdict dictionary

thisdict["year"] = 2018
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

thisdict.update({"year": "2020"})
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': '2020'}

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

thisdict["color"] = "red"
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': '1964', 'color': 'red'}

thisdict.update({"color": "red"})
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': '1964', 'color': 'red'}

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

thisdict.pop("model")
print(thisdict)
# {'brand': 'Ford', 'year': '1964'}

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

thisdict.popitem()
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang'}

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

del thisdict["model"]
print(thisdict)
# {'brand': 'Ford', 'year': '1964'}

del thisdict
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

thisdict.clear()
print(thisdict)
# {}

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

for x in thisdict:
    print(x)
"""
brand
model  
year 
"""

for x in thisdict:
    print(thisdict[x])
"""
Ford   
Mustang
1964 
"""

for x in thisdict.values():
    print(x)
"""
Ford   
Mustang
1964 
"""

for x in thisdict.keys():
    print(x)
"""
brand
model  
year 
"""

for x, y in thisdict.items():
    print(x, y)
"""
brand Ford
model Mustang
year 1964
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

mydict = thisdict.copy()
print(mydict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': '1964'}

mydict = dict(thisdict)
print(mydict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': '1964'}

myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : "2004"
    },
    "child2" : {
        "name" : "Tobias",
        "year" : "2007"
    },
    "child3" : {
        "name" : "Linus",
        "year" : "2011"
    }
}

print(myfamily)
# {'child1': {'name': 'Emil', 'year': '2004'}, 'child2': {'name': 'Tobias', 'year': '2007'}, 'child3': {'name': 'Linus', 'year': '2011'}}

child1 = {
    "name" : "Emil",
    "year" : "2004"
}
child2 = {
    "name" : "Tobias",
    "year" : "2007"
}
child3 = {
    "name" : "Linus",
    "year" : "2011"
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(myfamily)
# {'child1': {'name': 'Emil', 'year': '2004'}, 'child2': {'name': 'Tobias', 'year': '2007'}, 'child3': {'name': 'Linus', 'year': '2011'}}