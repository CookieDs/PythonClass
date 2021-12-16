#This week's homework will contain 20 exercises:
#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in numbers:
    print(n)

#2
print(numbers[0:1])
print(numbers[0:2])
print(numbers[0:3])
print(numbers[0:4])
print(numbers[0:5])

numbers2 = [0, 1, 2, 3, 4, 5]

for n in numbers2:
    print(numbers2[1:(n+1)]) #Tried making it in a loop

for i in range(6):
    for j in range(1, i + 1):
        print(j, "", end="")
    print("\r")

#3
print(sum(numbers[0:7])) #Summing up numbers 1-7

'''
#4
n = int(input("Enter a number: "))

for i in range(11):
    print(n*i)
'''

#5
for i in numbers:
    print(i)

#6
print(len("3689"))

#7
for i in range(6):
    for j in range(5, i, -1):
        print(j,"", end="")
    print("\r")

#8
for i in reversed(numbers):
    print(i)

#9
for i in range(-10, 0):
    print(i)

#10
bands = ["Linkin Park", "The Kooks", "Milky Chance", "Bastille", "Fall Out Boy", "5 Seconds of Summer",  "Panic! at the Disco", "The Neighbourhood", "My Chemical Romance", "Twenty One Pilots", ]
for i, b in enumerate(bands):
    print(str(i + 1) + ": " + b)

#11
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(prime_numbers[0:7])

#12
n1 = 0
n2 = 1
for i in range(11):
    print(n1)
    n3 = n2 + n1
    n1 = n2
    n2 = n3
'''
#13
n = int(input("Enter a number to find out its factorial number: "))
sum = 1
for i in range(1, n + 1):
    sum = sum * i
print("!" + str(n), "=", sum)

#14
n = int(input("Enter a large number:"))
print(sorted(n, reverse=True))
n.sort(reverse=True)
print(n)
'''
#15

#18
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end = " ")
    print("")
for i in range(1, 6):
    for j in range(5, i, -1):
        print("*", end = " ")
    print("")

#19 Idk how to do the spaces
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end = " ")
    print("")
for i in range(1, 6):
    for j in range(5, i, -1):
        print("*", end = " ")
    print("")