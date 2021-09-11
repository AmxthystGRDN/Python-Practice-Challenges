import numpy

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = numpy.mean(speed)

print(x)
# 89.76923076923077

x = numpy.median(speed)

print(x)
# 87.0

speed = [99, 86, 87, 88, 86, 103, 87, 94, 78, 77, 85, 86]

x = numpy.median(speed)

print(x)
# 86.5

'''
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)
# ModeResult(mode=array([86]), count=array([3]))
'''

speed = [86, 87, 88, 86, 87, 85, 86]

x = numpy.std(speed)

print(x)
# 0.9035079029052513

speed = [32, 111, 138, 28, 59, 77, 97]

x = numpy.std(speed)

print(x)
# 37.84501153334721

x = numpy.var(speed)

print(x)
# 1432.2448979591834

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

x = numpy.percentile(ages, 75)

print(x)
# 43.0

x = numpy.percentile(ages, 90)

print(x)
# 61.0

x = numpy.random.uniform(0.0, 0.5, 250)

print(x)
"""
[0.12253368 0.49948911 0.43717161 0.04088207 0.16381353 0.12803668
 0.41169329 0.16246406 0.12036654 0.12454032 0.47684194 0.32192904
 0.33801588 0.11153573 0.27443262 0.16067745 0.28428275 0.03603363
 0.46679461 0.08632547 0.43144392 0.41130074 0.47885823 0.42136766
 0.2206311  0.13573473 0.18480637 0.160558   0.31878779 0.42126533
 0.46248143 0.19711065 0.46366464 0.47838655 0.23271201 0.23395379
 0.24505996 0.18526204 0.28675974 0.04281898 0.09124075 0.34478924
 0.29201532 0.14786408 0.03181189 0.08821184 0.35355426 0.08482416
 0.06978706 0.12498561 0.17424476 0.23511171 0.25100372 0.36933727
 0.05743264 0.34278252 0.17000196 0.1191467  0.40378252 0.14605272
 0.29620476 0.28316939 0.34273792 0.27627989 0.27024107 0.43888684
 0.17379233 0.19704836 0.18006425 0.44843044 0.26639403 0.19225701
 0.11598607 0.18805825 0.36089763 0.00395929 0.27623377 0.43720824
 0.01377456 0.17285216 0.11431206 0.16623205 0.05361548 0.00562565
 0.36658423 0.05586074 0.46242494 0.26205902 0.1208962  0.11133156
 0.34006219 0.43107758 0.41018548 0.35542414 0.15363573 0.07220691
 0.06746837 0.19420174 0.16390957 0.24712326 0.47099112 0.39084543
 0.3991078  0.4861349  0.09769864 0.13009411 0.13874382 0.32393591
 0.37487015 0.20250987 0.15523479 0.18005605 0.10127483 0.09920766
 0.35902202 0.21911798 0.320398   0.14086012 0.2052454  0.15592775
 0.08045024 0.47196051 0.05111814 0.40680952 0.13802155 0.41047901
 0.07484104 0.13977008 0.38901918 0.38210707 0.29143232 0.46031198
 0.07305799 0.37059765 0.48859098 0.45351215 0.10874385 0.45058283
 0.08461854 0.154884   0.01694559 0.43306041 0.46368509 0.37529166
 0.16319106 0.25782567 0.22626487 0.0780364  0.44051262 0.34940404
 0.1582363  0.17520228 0.37414014 0.24284971 0.32228546 0.40568123
 0.34937402 0.46553532 0.08076016 0.09504004 0.28981849 0.17827249
 0.43128031 0.37781039 0.06754375 0.18179521 0.27903303 0.09879883
 0.00444931 0.0490141  0.1686404  0.3291866  0.07309559 0.48916448
 0.15979564 0.31410819 0.36791395 0.28558234 0.05655372 0.16820751
 0.18712451 0.26550362 0.24516459 0.2571566  0.20364395 0.13263517
 0.09777309 0.1518145  0.02033209 0.09701778 0.46850773 0.32633786
 0.4820672  0.24053305 0.09911316 0.22626875 0.1389302  0.43998166
 0.01643966 0.04623128 0.05520237 0.02720358 0.38218875 0.17382717
 0.02691811 0.47553364 0.49355679 0.34871032 0.14914014 0.44968733
 0.31776402 0.10405571 0.38631821 0.02003632 0.39273576 0.24763814
 0.27256504 0.32105502 0.37964801 0.47487278 0.44791611 0.46253414
 0.48658336 0.3470744  0.41759128 0.13491811 0.10484118 0.36686267
 0.08454269 0.09388525 0.34129971 0.14998879 0.15102501 0.19466536
 0.35580971 0.31388814 0.40017033 0.31951182 0.03390851 0.38723607
 0.18274063 0.24985859 0.40260239 0.11064046 0.30353659 0.21480821
 0.09150431 0.41770193 0.32248295 0.06827115]
"""

import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.image as pltimg

x = numpy.random.uniform(0.0, 0.5, 250)

plt.hist(x, 5)
plt.show()

x = numpy.random.uniform(0.0, 0.5, 100000)

plt.hist(x, 100)
plt.show()

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

plt.scatter(x, y)
plt.show()

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

print(r)
# -0.758591524376155

speed = myfunc(10)

print(speed)
# 85.59308314937454

x = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20, 26, 29, 48, 64, 6, 5, 36, 66, 72, 40]
y = [21, 46, 3, 35, 67, 95, 53, 72, 58, 10, 26, 34, 90, 33, 38, 20, 56, 2, 47, 15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

print(r)
# 0.01331814154297491

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

plt.scatter(x, y)
plt.show()

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

print(r2_score(y, mymodel(x)))
# 0.9432150416451027

speed = mymodel(17)
print(speed)
# 88.87331269697987

x = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20, 26, 29, 48, 64, 6, 5, 36, 66, 72, 40]
y = [21, 46, 3, 35, 67, 95, 53, 72, 58, 10, 26, 34, 90, 33, 38, 20, 56, 2, 47, 15]

plt.scatter(x, y)
plt.show()

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(2, 95, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

print(r2_score(y, mymodel(x)))
# 0.009952707566680652

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)
# [107.2087328]

print(regr.coef_)
# [0.00755095 0.00780526]

predictedCO2 = regr.predict([[3300, 1300]])

print(predictedCO2)
# [114.75968007]

scale = StandardScaler()

scaledX = scale.fit_transform(X)

print(scaledX)
"""
[[-2.10389253 -1.59336644]
 [-0.55407235 -1.07190106]
 [-1.52166278 -1.59336644]
 [-1.78973979 -1.85409913]
 [-0.63784641 -0.28970299]
 [-1.52166278 -1.59336644]
 [-0.76769621 -0.55043568]
 [ 0.3046118  -0.28970299]
 [-0.7551301  -0.28970299]
 [-0.59595938 -0.0289703 ]
 [-1.30803892 -1.33263375]
 [-1.26615189 -0.81116837]
 [-0.7551301  -1.59336644]
 [-0.16871166 -0.0289703 ]
 [ 0.14125238 -0.0289703 ]
 [ 0.15800719 -0.0289703 ]
 [ 0.3046118  -0.0289703 ]
 [-0.05142797  1.53542584]
 [-0.72580918 -0.0289703 ]
 [ 0.14962979  1.01396046]
 [ 1.2219378  -0.0289703 ]
 [ 0.5685001   1.01396046]
 [ 0.3046118   1.27469315]
 [ 0.51404696 -0.0289703 ]
 [ 0.51404696  1.01396046]
 [ 0.72348212 -0.28970299]
 [ 0.8281997   1.01396046]
 [ 1.81254495  1.01396046]
 [ 0.96642691 -0.0289703 ]
 [ 1.72877089  1.01396046]
 [ 1.30990057  1.27469315]
 [ 1.90050772  1.01396046]
 [-0.23991961 -0.0289703 ]
 [ 0.40932938 -0.0289703 ]
 [ 0.47215993 -0.0289703 ]
 [ 0.4302729   2.31762392]]
"""

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)
# [97.07204485]

numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

plt.scatter(train_x, train_y)
plt.show()

plt.scatter(test_x, test_y)
plt.show()

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

r2 = r2_score(train_y, mymodel(train_x))

print(r2)
# 0.7988645544629795

r2 = r2_score(test_y, mymodel(test_x))

print(r2)
# 0.8086921460343556

print(mymodel(5))
# 22.879625918116744

df = pandas.read_csv("shows.csv")

print(df)

d = {'UK' : 0, 'USA' : 1, 'N' : 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES' : 1, 'NO' : 0}
df['Go'] = df['Go'].map(d)

print(df)

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

print(X)
print(y)

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file = None, feature_names = features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img = pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()

print(dtree.predict([[40, 10, 7, 1]]))

print(dtree.predict([[40, 10, 6, 1]]))