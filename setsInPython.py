"""doesn't allow duplicate values, unordered, unchangeable"""
s = {2,4,2,5}
print(s)

info = {"shakib", 23, True, 5.11}
info.add("Dhaka")
print(info)
print(type(info))
if "shakib" in info:
    print("shakib Exist in Dhaka")

"""access set item using for loop"""
for i in info:
    print(i)


"""Set Methods"""

"""Unino (takes every elements once from 2 set)"""
set1 = {1,3,4,5}
set2 = {2,3,4,7}

uniSet = set1.union(set2)
set1.update(set2) # takes what in set2 but not union

print(uniSet)
print(set1)

"""Intersection (takes only common elements from two sets)"""
set1 = {1,3,4,5}
set2 = {2,3,4,7}

intSet = set1.intersection(set2)
print(intSet)

"""Difference (takes teh valu from first set which are not common in two sets)"""
set1 = {1,3,4,5}
set2 = {2,3,4,7}

difSet = set1.difference(set2)
print(difSet)


"""Symmetric Difference (takes values that are not common in two set)"""
set1 = {1,3,4,5}
set2 = {2,3,4,7}

symSet = set1.symmetric_difference(set2)
print(symSet)

"""Disjoint (returns True if no values are same in two sets. False otherwise)"""
set1 = {1,3,4,5}
set2 = {2,3,4,7}
print(set1.isdisjoint(set2))

"""Superset & Subset"""
set1 = {1,2,3,4,5,6,7,8}
set2 = {2,3,4}

print(set1.issuperset(set2))

print(set2.issubset(set1))

"""Add  (to add single item in a set)"""
set1 = {1,3,4,5}
print(set1)
set1.add(2)
print(set1)

"""Update (to add more than one item in a set)"""
set1 = {1,3,4,5}
print(set1)
set1.update([2,7])
print(set1)

"""Remove (to remove a item. if not exist itt will raise an error)"""
set1 = {1,2,3,4,5,6,7,8}
print(set1)
set1.remove(7)
#set1.remove(69) #raise an error
print(set1)

"""Discard (to remove a item. if not exist itt will not raise any error)"""
set1 = {1,2,3,4,5,6,7,8}
print(set1)
set1.discard(7)
set1.discard(69)
print(set1)

"""Pop (remove a random value as sets are unordered)"""
set1 = {1,2,3,4,5,6,7,8}
poped = set1.pop()
print(poped)
print(set1)

"""Clear (to delete all the elements from a set)"""
set1 = {1,2,3,4,5,6,7,8}
set1.clear()
print(set1)


"""Del (to delete an entire set)"""
set1 = {1,2,3,4,5,6,7,8}
del set1
# print(set1)