thistuple = ("apple", "banana", "cherry")
print(thistuple)
# ('apple', 'banana', 'cherry')

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
# ('apple', 'banana', 'cherry', 'apple', 'cherry')

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
# 3

thistuple = ("apple",)
print(type(thistuple))
# <class 'tuple'>

thistuple = ("apple")
print(type(thistuple))
# <class 'str'>

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
# ('apple', 'banana', 'cherry')

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
# banana

print(thistuple[-1])
# cherry

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
# ('cherry', 'orange', 'kiwi')

print(thistuple[:4])
# ('apple', 'banana', 'cherry', 'orange')
 
print(thistuple[2:])
# ('cherry', 'orange', 'kiwi', 'melon', 'mango')

print(thistuple[-4:-1])
# ('orange', 'kiwi', 'melon')

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple.")
# Yes, 'apple' is in the fruits tuple.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
# ('apple', 'kiwi', 'cherry')

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)
# ('apple', 'banana', 'cherry', 'orange')

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
# ('apple', 'banana', 'cherry', 'orange')

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)
# ('banana', 'cherry')

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
"""
apple
banana
cherry
"""

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
"""
apple
banana
['cherry', 'strawberry', 'raspberry']
"""

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
"""
apple
['mango', 'papaya', 'pineapple']
cherry
"""

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
"""
apple 
banana
cherry
"""

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])
"""
apple 
banana
cherry
"""

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
"""
apple 
banana
cherry
"""

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2

print(tuple3)
# ('a', 'b', 'c', 1, 2, 3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
# ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')