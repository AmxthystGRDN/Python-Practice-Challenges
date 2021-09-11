import datetime

x = datetime.datetime.now()

print(x)
# 2021-07-13 22:55:43.029046

print(x.year)
print(x.strftime("%A"))
"""
2021   
Tuesday
"""

x = datetime.datetime(2020, 5, 17)

print(x)
# 2020-05-17 00:00:00

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
# June