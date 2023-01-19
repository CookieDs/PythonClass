'''
area = 0
bas = 1
for x in range(1,100):
    y = 20 * 1.3 ** x 
    area = area + bas * y
    if area > 11000:
        print("Antal rektanglar med bas 1 m som har arean 11 000 m^2:", area)
        break

#print("Det gröna området har arean", round(area,2), "m^2.")

area = 0
bas = 0.5
for x in range(1, 13):
    y = 0.2 * x **2
    area = area + bas * y

print("Röda programets area:", area, "m^2.")

import random
antal = 0
n = int(input("Hur många tärningskast vill du göra?"))

for i in range(n):
    t1 = random.randint(1,6)
    t2 = random.randint(1,6)
    t3 = random.randint(1,6)
    t4 = random.randint(1,6)
    t5 =random.randint(1,6)
    summa = t1 + t2 + t3 + t4 + t5
    if summa == 25:
        antal += 1

andel = round(((antal/n) * 100), 2)
print("Andel kast med poängsumman 25:", andel, "%") #Stabiliserar runt 2800 i 12 med 4

Emax = 0
for x in range(0, 41): #Stora lådor
    for y in range(1, 86): #Små lådor
        V = 200*x + 50*y #Beräkna volymen av x och y
        m = 5*x + 20*y #Beräkna vikt av x och y
        if V <= 8000 and m <= 1700:
            E = 40*x + 25*y
            #print(E)
            if E > Emax:
                Emax = E
                stora = x
                små = y

print("Tony ska lasta", stora, "stora lådor och", små, "små lådor för att få maximal ersättning.\nErsättningen blir:", Emax)

Emax = 0
for x in range(0, 29): #Stora lådor
    for y in range(1, 491): #Små lådor
        V = 200*x + 50*y #Beräkna volymen av x och y
        m = 5*x + 20*y #Beräkna vikt av x och y
        if V <= 57000 and m <= 9800:
            E = 40*x + 25*y
            #print(E)
            if E > Emax:
                Emax = E
                stora = x
                små = y
print("Lastbil nr.1:", Emax)
Emax = 0
for x in range(0, 342): #Stora lådor
    for y in range(1, 407): #Små lådor
        V = 200*x + 50*y #Beräkna volymen av x och y
        m = 5*x + 20*y #Beräkna vikt av x och y
        if V <= 68200 and m <= 8120:
            E = 40*x + 25*y
            #print(E)
            if E > Emax:
                Emax = E
                stora = x
                små = y
print("Lastbil nr.2:", Emax)

for x in range(0, 41): #Stora lådor
    for y in range(1, 86): #Små lådor
        V = 200*x + 50*y #Beräkna volymen av x och y
        m = 5*x + 20*y #Beräkna vikt av x och y
        if V <= 8000 and m <= 1700:
            E = 40*x + 25*y
            #print(E)
            if E > Emax:
                Emax = E
                stora = x
                små = y

    
xoxBoard = [['-', '-', '-',], ['-', '-', '-',], ['-', '-', '-',]]
xoxBoard[0][2] = 'X'
a = 0
print("A  B  C")
for row in xoxBoard:
    for collumn in row:
        if collumn == '-':
            print(' ', end='  ')
        else:
            print(collumn, end='  ')
    print(a,"\r")
    a += 1


p = -0.88
q = 0.19
x1 = round(-p/2 + ((p/2)**2 - q)**0.5, 3)
x2 = round(-p/2 - ((p/2)**2 - q)**0.5, 3)

print("x1 =", x1, "och x2 =", x2)

print("\n\n")

a = 8
b = -56
c = -480
p = b/a
q = c=a
x1 = round(-p/2 + ((p/2)**2 - q)**0.5, 3)
x2 = round(-p/2 - ((p/2)**2 - q)**0.5, 3)

print("x1 =", x1, "och x2 =", x2)

p = 1
q = 12
k = (p**3)/27 + (q**2)/4
x = ((q/2) + (k**0.5))**(1/3) + ((q/2) - (k**0.5))**(1/3)
if k>0:
    print("x =", round(x, 3))

'''
x1 = 2
y1 = 2
x2 = 1
y2 = 1

d1 = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

x = (x1 + x2)/2
y = (y1 + y2)/2

print("Sträckans längd:", round(d1, 2), "\nMittpunkten: ", (x,y))

x3 = 4
y3 = 4
x4 = 5
y4 = 5

d2 = ((x4 - x3)**2 + (y4 - y3)**2)**0.5

if d1 == d2:
  print("Sträckorna är lika långa, båda är", round(d1,2), "l.e.")
else:
  print("Sträckorna är inte lika långa.")
  
k1 = (y2-y1)/(x2-x1)
k2 = (y4-y3)/(x4-x3)

if k1 == k2:
  print("Sträckorna är parallella, båda har k-värdet:", k1)
else:
  print("Sträckorna är inte parallella.")

if k1*k2 == -1:
  print("Sträckorna är vinkelräta.")
else:
  print("Sträckorna är inte vinkelräta.")

