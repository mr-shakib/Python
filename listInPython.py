# val = "mark","john","chris","spider"

# lst = []

# for i in val:
#     lst.append(i)
# print(lst)

# lstC = [i for i in val]
# print(lstC)

"""List Methods"""

l = [3,6,35,54,34,64,34,64,33,5,35,56,93]
print(l)

"""Append Method"""

l.append(69)
print(l)

"""Reverse Method"""
l.reverse()
print(l)

"""Sort Method Ascending & Descinding using Reverse"""

l.sort()
print(l)

l.sort(reverse=True)
print(l)

"""Index Method (return the index of a value for first occurance)"""

print(l.index(69))

"""Count Method (count how many times a value occured in the list)"""

print(l.count(64))

"""Copy Method (copy the list so that the values don't change)"""
# m = l {the values will change if we cahnge together}

m = l.copy()
print(m)

m[3] = 69

print(l[3])
print(m[3])


"""Insert Method"""

l.insert(5, 70)
print(l[5])


"""Extend Method"""
n = ["this","is","using","extend","method"]

k = l + n #makes a new list combining two
print(k)

l.extend(n)
print(l)

