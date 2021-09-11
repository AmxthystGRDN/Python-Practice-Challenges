f = open("demofile.txt", "r")

print(f.read())
"""
Hello! Welcome to demofile.txt    
This file is for testing purposes.
Good Luck!

"""

print(f.read(5))
# Hello

print(f.readline())
# Hello! Welcome to demofile.txt

print(f.readline())
print(f.readline())
"""
Hello! Welcome to demofile.txt

This file is for testing purposes.

"""

for x in f:
    print(x)
"""
Hello! Welcome to demofile.txt

This file is for testing purposes.

Good Luck!
"""

print(f.readline())
f.close()
# Hello! Welcome to demofile.txt

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demofile2.txt", "r")
print(f.read())
# Now the file has more content!

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("demofile3.txt", "r")
print(f.read())
# Woops! I have deleted the content!

f = open("myfile.txt", "x")

import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

os.rmdir("myfolder")