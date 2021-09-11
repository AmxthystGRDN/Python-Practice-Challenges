a = "Hello, World!"
print(a[1])
# e

for x in "banana":
    print(x)
"""
b
a
n
a
n
a
"""

a = "Hello, World!"
print(len(a))
# 13

txt = "The best things in life are free!"
print("free" in txt)
# True

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
# Yes, 'free' is present.

txt = "The best things in life are free!"
print("expensive" not in txt)
# True

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")
# Yes, 'free' is present.

b = "Hello, World!"
print(b[2:5])
# llo

b = "Hello, World!"
print(b[-5:-2])
# orl

a = "Hello World!"
print(a.upper())
# HELLO WORLD!

a = "Hello World!"
print(a.lower())
# hello world!

a = " Hello, World! "
print(a.strip())
# Hello, World!

a = "Hello, World!"
print(a.replace("H", "J"))
# Jello, World!

a = "Hello, World!"
print(a.split(","))
# ['Hello', ' World!']

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
# My name is John, and I am 36

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# I want 3 pieces of item 567 for 49.95 dollars. 

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
# I want to pay 49.95 dollars for 3 pieces of item 567. 

txt = "We are the so-called \"Vikings\" from the north."
print(txt)