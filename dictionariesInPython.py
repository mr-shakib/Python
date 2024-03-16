info = {
    'name' : 'Shakib',
    'age' : 23,
    'height' : 5.11,
    'eligible' : True,
}

print(info)
print(info['name']) # gives an error if key doesn't exist
print(info.get('name')) # don't give any error if key doesn't exist. Insteed print none

keys = info.keys()
print(keys)
 
for key in info.keys():
    print(key)
    print(info[key]) # gets the value u dumbass

value = info.values()
print(value)

for key, value in info.items():
    print(key)
    print(value)
    
ep1 = {
    122 : 56,
    123 : 69,
    125 : 90,
    234 : 76,
}
print(ep1)

ep2 = {
    222 : 87,
    224 : 95,
}
print(ep2)

"""Update (to add two dictionary)"""
ep1.update(ep2)
print(ep1) 

"""Pop (to remove item)"""
ep1.pop(123)
print(ep1)

"""Popitem (to remove the last item)"""
ep1.popitem()
print(ep1)

"""Clear (to clear all the items from a dictionary)"""
ep1.clear()
print(ep1)

"""to make a empty dict"""
empt = {}
print(empt)

"""Del (to delete entire dictionary or specific key)"""
ep1 = {
    122 : 56,
    123 : 69,
    125 : 90,
    234 : 76,
}

del ep1[125]
print(ep1)

del ep1



