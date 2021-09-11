x = 5
y = "John"
print(x)
print(y)

x = 4
x = "Sally"
print(x)

x = str(3)
y = int(3)
z = float(3)

x = 5
y = "John"
print(type(x))
print(type(y))

x, y, z = "Orange", "Bananna", "Cherry"
print(x, y, z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruit = ["apple", "banana", 'cherry']
x, y, z = fruit
print(x)
print(y)
print(z)

x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z = x + y
print(z)

x = 10
y = 5
print(x + y)

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)