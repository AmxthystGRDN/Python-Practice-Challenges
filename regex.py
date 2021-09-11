import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x)
# <re.Match object; span=(0, 17), match='The rain in Spain'>

x = re.findall("ai", txt)

print(x)
# ['ai', 'ai']

x = re.findall("Portugal", txt)

print(x)
# []

x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
# The first white-space character is located in position: 3

x = re.search("Portugal", txt)

print(x)
# None

x = re.split("\s", txt)

print(x)
# ['The', 'rain', 'in', 'Spain']

x = re.split("\s", txt, 1)

print(x)
# ['The', 'rain in Spain']

x = re.sub("\s", "9", txt)

print(x)
# The9rain9in9Spain

x = re.sub("\s", "9", txt, 2)

print(x)
# The9rain9in Spain

x = re.search("ai", txt)

print(x)
# <re.Match object; span=(5, 7), match='ai'>

x = re.search(r"\bS\w+", txt)

print(x.span())
# (12, 17)

print(x.string)
# The rain in Spain

print(x.group())
# Spain