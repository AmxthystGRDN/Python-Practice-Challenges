thisset = {"apple", "banana", "cherry"}
print(thisset)
# {'banana', 'apple', 'cherry'} (random order)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
# {'banana', 'apple', 'cherry'} (random order)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))
# 3

myset = {"apple", "banana", "cherry"}
print(type(myset))
# <class 'set'>

thisset = set(("apple", "banana", "cherry"))
print(thisset)
# {'banana', 'apple', 'cherry'} (random order)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)
"""
banana
apple 
cherry (random order)
"""

print("banana" in thisset)
# True 

thisset.add("orange")
print(thisset)
# {'apple', 'cherry', 'banana', 'orange'} (random order)

tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)
# {'cherry', 'papaya', 'banana', 'orange', 'mango', 'apple', 'pineapple'} (random order)

thisset = {"apple", "banana", "cherry"}
myset = ["kiwi", "orange"]

thisset.update(myset)
print(thisset)
# {'kiwi', 'apple', 'banana', 'orange', 'cherry'} (random order)

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
print(thisset)
# {'apple', 'cherry'} (random order)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")
print(thisset)
# {'apple', 'cherry'} (random order)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)
# apple/banana/cherry

print(thisset)
# {'apple/banana/cherry', 'apple/banana/cherry'}

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
# set()
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
# {1, 2, 3, 'b', 'c', 'a'} (random order)

set1.update(set2)
print(set1)
# {1, 2, 3, 'b', 'c', 'a'} (random order)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)
# {'apple'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}


z = x.intersection(y)
print(z)
# {'apple'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)
# {'google', 'cherry', 'microsoft', 'banana'} (random order)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
print(z)
# {'google', 'cherry', 'microsoft', 'banana'} (random order)