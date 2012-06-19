# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

20 %9

# <codecell>

20/4.

# <codecell>

False

# <codecell>

True

# <codecell>

float('7.5')+float('6')

# <codecell>

a = 5

# <codecell>

a

# <codecell>

print a

# <codecell>

print a, 6, 'six'

# <codecell>

l = ['zero', 1, 2.0, '3',4,5.0,'six']

# <codecell>

l

# <codecell>

l[0]

# <codecell>

float(l[3])

# <codecell>

len(l)

# <codecell>

l[1:4]

# <codecell>

l[4:]

# <codecell>

l[:4]

# <codecell>

l[:5]

# <codecell>

l[1] += 99

# <codecell>

l

# <codecell>

t = ('zero',1,2.0)

# <codecell>

t

# <codecell>

t[0:]

# <codecell>

t[1.5:]

# <codecell>

l[1:]

# <codecell>

d = { 'first': 'alpha', 'two':2, 2: 'two'}

# <codecell>

d

# <codecell>

d['first']

# <codecell>

d['two']

# <codecell>

d[2]

# <codecell>

d['hi'] = 'SC'

# <codecell>

d['hi']

# <codecell>

print d

# <codecell>

d

# <codecell>

len(d)

# <codecell>

x = -5
if x < 0:
    
        

# <codecell>

x = 5
if x < 0:
    print 'x is negative'
elif x > 0:
    print 'x is positive'
    print 'maybe'
elif x == 0:
    print 'x is zero'

# <codecell>

fruits = ['apples','oranges','pears','bananas']
fruits[0]

# <codecell>

i = 0
while i < len(fruits):
    print fruits[i]
    i += 1

# <codecell>

for fruit in fruits:
    print fruit

# <codecell>

for i in range(1,len(fruits),2):
    print i

# <codecell>

prices = [.49,.99,1.49,0.32]
for fruit, price in zip(fruits, prices):
    print fruit, "cost", price, "each"

# <codecell>

"%s cost %f each" % (fruit,price)

# <codecell>

prices = { 'apples': 0.49, 'oranges':0.99,'pears':1.49,'bananas':0.32}

# <codecell>

for fruit,price in prices.items():
    print fruit, price

# <codecell>

prices.values()

# <codecell>

sum = 0
prices = [0.49, 0.99, 1.49, 0.32]
for price in prices:
    sum = sum+price

# <codecell>

print sum

# <codecell>

print price

# <codecell>

sum

# <codecell>

def square(x):
    return x * x

# <codecell>

square(2)

# <codecell>

def hello(time, name):
    """
   Prints a message
    """
    return "Good " + time + ", " +name + "!"
    

# <codecell>

help(l)

# <codecell>

b

# <codecell>

print b

# <codecell>

f = open("animals.txt","r")

# <codecell>

a = f.readlines()

# <codecell>

a

# <codecell>

f.seek(0)

# <codecell>

for line in f:
    print line

# <codecell>

f.seek(0)

# <codecell>

for line in f:
    print line.split()

# <codecell>

parts = line.split()
parts

# <codecell>

int(parts[3])

# <codecell>

f.seek(0)

# <codecell>

dates = []
times =[]
animals = []
numbers = []
for line in f:
    date, time, animal, number = line.split()
    dates.append(date)
    times.append(time)
    animals.append(animal)
    numbers.append(int(number))

# <codecell>

numbers

# <codecell>

animals

# <codecell>

dates

# <codecell>

date

# <codecell>

times

# <codecell>


