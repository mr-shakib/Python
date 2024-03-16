"""tup = (12,) #necessary to put comma for 1 element in tuple"""

tup = (2,44,54,56,57,5,325,65,74,56,65,"tuple",True)

print(tup)

print(tup[4:9])

if "tuple" in tup:
    print("Tuple exist")

tlist = list(tup)
print(tlist)

tlist.pop(8)
tlist.append(69)
tup = tuple(tlist)
print(tup)

"""Tuple is not changeable. to manipulate tuple convert the tuple to a list.
then do the manipulation and convert back to tuple"""