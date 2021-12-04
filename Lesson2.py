#Lists and Tuples

#Lists:
#Variable_name = [items]
students = ["Tarik", "Diana", "Yusuf", "Nilgun", "Jonas", "Huze"]
print(students)

#Naming and Defining:
#Name the variable as plural for your own sake #Defining the items by picking a suitable/fitting name
colors = ["r", "g", "b"]

#Accessing elements:
#First element is 0, then 1, then 2, 3, 4, ..., n #var_name[n]
print(colors[0])

the_color = colors[0]
print(the_color)

#Access reverse:
print(colors[-1]) #Going backwards, starts from [-1, -2, -3, ...]


#IndexError: list index out of range #The index (accessing element) is too big or too small for your list
#Example: print(colors[4])


#Exercises:
#0
languages = ["python", "c", "java"]
print(languages[0])
print(languages[1])
print(languages[2])

#1
print("The programming language we are using is " + languages[-3])
print("A nice programming language is " + languages[-2])
print("Another one is " + languages[-1])

#2
flavours = ["chocolate", "vanilla", "strawberry", "lemon"]
print("I love the flavour", flavours[0])

#Loops in Lists
names = ["Tarik", "Diana", "Yusuf", "Nilgun", "Jonas", "Huze"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])

for name in names: #Instead of copying "print(var[n])" a thousand times
    print(name)

#for var_name in list_name:
#-> code to run

#Enumerate
tech_comps = ["microsoft", "apple", "google"]
for i, comp in enumerate(tech_comps): #Enumerate seperates the index (i) and the comp #microsoft i = 1...
    print(str(i + 1), comp.title()) #If we wanna see which number it is #With string you can put +
    print((i + 1), comp.title())

l1 = ["1", "2", "3"]
l2 = ["one", "two", "three", "four"] 

for i in range(len(tech_comps)): #len = length
    print(i) #Prints out the range, this case 0-2
    print(tech_comps[i]) #Does the same thing as a normal loop?
    print(range(i)) #Range of numbers #Go from 0-10

for i in range(len(l1)): #Length of l1, so even if l2 is longer it'll only show l1's range
    print(l1[i], l2[i])


#Exercises:
#3
for language in languages:
    print(language)

#4 
for language in languages:
    print("A nice programming language is", language)

#Common Op ?
#Modify
tech_comps[0] = "amazon" #The original (this case "microsoft") gets replaced
print(tech_comps)

#Find
print(tech_comps.index("apple")) #Find an index (0,1,2..) #If you try to find microsoft (the one we switched out) it'll say error

print("microsoft" in tech_comps) #Asking if microsoft is in tech_comps

#Appending
tech_comps.append("microsoft") #Add in the end
print(tech_comps)

#Inserting
tech_comps.insert(0, "deepmind") #Inserting wherever you want the item
print(tech_comps)

social_medias = [] #Adding empty list and adding items 
social_medias.append("facebook")
social_medias.append("instagram")
social_medias.append("snapchat")

for i, sm in enumerate(social_medias):
    print(str(i + 1) + '-' + sm.title())

#Sorting a list
tech_comps.sort() #Alphabetic order
for i, tc in enumerate(tech_comps):
    print(str(i + 1) + '-' + tc.title())

tech_comps.sort(reverse=True) #Reverse the sorted order z-a
for tc in tech_comps:
    print(tc)

tech_comps_sorted = sorted(tech_comps) #New list
print(tech_comps)
print(tech_comps_sorted) #Question for Bedir, how do I unsort the items?

#Exercise
#5
students.sort(reverse=True) 
for s in students:
    print(s)
print(students[::-1]) #Another way of reversing order z-a #In this case I'm re-reversing because I already reversed before

nums = [1, 3, 2, 5, 4]
print(nums)
print(sorted(nums))
print(sorted(nums, reverse=True))
nums.reverse() #Reverse order

print(sorted(flavours)) #Writing like this does not sort them forever, compare: "flavours.sort()"
print(flavours)

#Length
length = len(nums) #Doesn't include a 0, only gives you amount
print(length)

#Exercises:
#6
for language in languages:
    print(language)
    print("sorted from a-z:", sorted(languages))
    print(language)
    print("sorted from z-a:", sorted(languages, reverse=True))
    print(language)
    for r in reversed(languages): #Reverse order using a loop
        print("languages reversed order:", r)
    print(language)

languages.sort()
print("Sorted a-z:", languages)
languages.sort(reverse=True)
print("Sorted z-a:", languages)

#7
nums= [2, 4, 9, 1, 7]
for n in nums:
    print(n)
    print("Increasing order:", sorted(nums))
    print(n)
    print("Decreasing order:", sorted(nums, reverse=True))
    print(n)
    for rev in reversed(nums):
        print("Reversed order:", rev) 
    print(n)

nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

#Remove
nums = [1, 3, 2, 5, 4]
del nums[0] 
print(nums)

#By value
nums. remove(2) #Remove value 2
print(nums)

#Pop
nums = [1, 2, 3, 4, 5]
print(nums)
last = nums.pop() #Default value is last item, removes it
print(last)

one = nums.pop(0) #Choosing which value to remove
print(nums) #nums is now permanently changed and lost 2 values
print(one)

#Exercise:
#8 
famous = ["Kim K", "Selena Gomez", "Adele", "Lady Gaga"]
print(famous)
famous.pop()
print(famous)
famous.pop(0)
print(famous)
del famous[0]
print(famous)
famous. remove("Adele") 
print("There are no famous people left in my list, look:", famous)

#Slicing
#var_name[start_idx:stop_index:step_size] 
#Default normal order is [0:end:1] #Up to "end" (<end) #Backwards = [-1::-1]
nums = [1, 2, 3, 4, 5]
print(nums[0:3])
print(nums[::1])
print(nums[::-1])
print(nums[-1:0:-1]) ##-1:: is last (think as loop). :0: up to 0, doesn't include 0. ::-1 one step backwards
print(nums[-1::-1]) #Default to -1 if you just write ::-1 no probs 
print(nums[0:4:1],"\n") #Just to see where the numbers above end and the underneath start

copy_nums = nums[:] #Making new list copied exactly last one, you change the first this one doesn't because it's a new list
copy_nums_wrong = nums
nums[0] = 2
print(nums)
print(copy_nums) #Doesn't change, because it was copied before we changed "nums[0] = 2"
print(copy_nums_wrong)

#Range (Start, end, step)
for n in range(1, 11, 2): #Starts at 1, up to "end" (<11), takes 2 steps
    print(n)

nums = list(range(1, 11, 2))
print(nums)

for n in range(0, 15, 3):
    print(n)

#min, max, sum
ages = (23, 25, 35, 18, 16, 77)
 
youngest = min(ages)
oldest = max(ages)
total_age = sum(ages)

print(youngest, oldest, total_age)