#Q1 If-Else / For-Loop

n = int(input("Enter a number: "))
if n > 10:
    print("The number is greater than 10.")
else:
    print("The number is less than or equal to 10.")

#Q2  If-Else / For-Loop / Lists / Functions - NOPE
def is_poisonous(mushroom,poisonous_codes):
    for code in poisonous_codes:
        if code in mushroom:
            return True #Poisonous
    return False #Not poisonous

def count_poisonous(mushroom_list, poisonous_codes):
    counter_p = 0
    for mushroom in mushroom_list:
        if is_poisonous(mushroom, poisonous_codes):
            counter_p = counter_p + 1
    return counter_p

poisonous_codes = ['cod', 'arpe', 'xxyt', 'acr', 'bcd', 'xz']
forest_mushrooms = ['htrcd', 'tarpes', 'xxytr', 'ceaar', 'vvbctd', 'vsxz', 'accr', 'ccod', 'ttyt', 'garxxytacr', 'ccd', 'xz']
num_p = count_poisonous(forest_mushrooms, poisonous_codes)
num_m = len(forest_mushrooms)

print(f"Total numbe of mushrooms:\t{num_p}")
print(f"Number of poisonous:\t\t{num_p}")
print(f"Number of edible:\t\t{num_m - num_p}")

#Q3 If-Else / Functions
def temperature(t):
    if t > 40:
        print(f"It's {t}°C, stay inside! It's too hot outside.")
    elif t >= 15:
        print("It's okay to go outside, it's pretty warm.")
    elif t >= 0:
        print("It's okay to go outside, but it's a bit chilly. Wear a jacket!")
    elif t > -10:
        print("It's cold outside but you can still go out in the snow.")
    else:
        print("You should not go outside. It is freezing... Damn!")

temperature(2)
temperature(46)
temperature(29)
temperature(-8)
temperature(-35)

#Q4 If-Else / Functions / Lists #I did it my way, I can't use functions T-T
numbers = [1, 2, 3, 4, 5]
#def largest_number(ln):
if numbers == []:
    print("There are no numbers.")
else:
    l_n = max(numbers)
    print(l_n, "is the largest number.")
#largest_number(numbers)

def largest_number(ln):
    if ln == []:
        print("There are no numbers.")
    else:
        l_n = max(ln)
        print(l_n, "is the largest number.")

largest_number(numbers)

#Q5 If-Else / Functions
def hours(h):
    hs = int(h)
    mins = int((h-hs)*60)
    secs = int((((h-hs)*60)-mins)*60)
    print(hs, "hours,", mins, "minutes,", secs, "seconds.")
hours(3.5)
hours(5.33)
hours(1.53)
hours(7.9973)

#Q6 If-Else / Functions / Lists #I could do it so it applies to any list but I'll do that later
numbers = [1, 2, 3, 4, 5]
number_names = ['one', 'two', 'three', 'four', 'five']

def nums(n):
    if n == []:
        print("None. The list is empty.")
    else:
       n = number_names
    print(n)
nums(numbers)

#Q7 If-Else / Functions
def palindrome(pal):
    if pal == "":
        print("None. The string is empty.")
    else:
        print(f"Checking if {pal} is a palindrome...")
        pal = f"{pal}"
        print(pal == pal[::-1])
palindrome("hello")
palindrome("racecar")
palindrome("bob")
palindrome("")

#Q8 If-Else / For-Loop / Lists / Functions
todo_list = ['wash car', 'buy groceries', 'pay bills']
def add_item(ls, item):
    ls.append(item)
def remove_item(ls, item):
    ls.remove(item)
#def mark_completed(ls, item): #Problem Nope, I tried so many things and I still can't mark it
    #item = (f"x {item}")
    
def mark_completed(ls, item):
    for i in ls:
        if i == item:
            item = "x " + item #ls.replace(item, ("x " + item))
        else:
            i = "- " + i #ls.replace(item, ("- " + item))
            

def print_list(ls):
    for i in ls:
        print("-", i)

add_item(todo_list, 'go to the gym')
remove_item(todo_list, 'pay bills')
mark_completed(todo_list, 'wash car')
print_list(todo_list)

#Q9 For-Loop / Lists / Functions
def fibonacci(f):
    n1 = 0
    n2 = 1
    if f >= 1:
        for i in range(1, f):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        print(n3)
    else:
        print("None")

fibonacci(5)
fibonacci(8)
fibonacci(0)
fibonacci(11)
fibonacci(40)

#Q10 If-Else / Lists / Functions
def multiply_string(string1, string2):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40]
    number_names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty"]
    if string1 in number_names:
        string1 = numbers[number_names.index(string1)]
    elif string1 != "":
        string1 = string1.split(" ")
        string1[0] = numbers[number_names.index(string1[0])]
        string1[1] = numbers[number_names.index(string1[1])]
        string1 = string1[0] + string1[1]
    else:
        string1 = ""

    if string2 in number_names:
        string2 = numbers[number_names.index(string2)]
    elif string2 != "":
        string2 = string2.split(" ")
        string2[0] = numbers[number_names.index(string2[0])]
        string2[1] = numbers[number_names.index(string2[1])]
        string2 = string2[0] + string2[1]
    else:
        string2 = ""
    
    if string1 == "":
        print("None")
    elif string2 == "":
        print("None")
    else:
        print(string1 * string2)

multiply_string("five", "three")
multiply_string("six", "")
multiply_string("twenty two", "three")
multiply_string("fifteen", "thirty one")
multiply_string("zero", "one")