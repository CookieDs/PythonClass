#Q1 List comprehension
for i in range(1,11):
    print(i+13)

#Q2 List comprehension
l1 = "The quick brown fox jumps over the lazy dog." 
l2 = "My name is Inigo Montoya. You killed my father. Prepare to die."
l3 = "Luke, I am your father"
list1 = [i for i in l1[::2]] #Creating lists of the even indexes in the sentences
list2 = [j for j in l2[::2]]
list3 = [k for k in l3[::2]]
print(list1, "\n", list2,"\n", list3)

#Q3 String Manipulation
s1 = "A day without sunshine is like, you know, not a day."
s1_2 = s1.find("d")

s2 = "Dreams come true. Without a dream, nothing happens."
s3 = "Dry day in a drought."
s4 = "Dance or die. The choice is dreadfully simple."

#Q4 String Manipulation
print("My cat is my best friend.".replace("cat", "dog"), "\n" "This cat is outrageous.".replace("cat", "dog"), "\n" "We have a cat problem.".replace("cat", "dog"))

#Q5 String Manipulation
sentence = "Hello happy Diana"
print(sentence[:5], sentence[6:11], sentence[-5:])
'''
#Q6 String manipulation
#Use:"ATGCTTCAGAAAGGTCTTACG" as example
s =  input("Enter a DNA string: ")
sc = "ACGT"
print("A C G T")
for i in sc:
    print(s.count(i), end = " ")
print(" ") #Did this because the last one cancels out the end which makes the #Q7 start right next to it

#Q7 String manipulation
t = input("Enter a DNA string to turn it into RNA: ")
u = t.replace("T", "U") #Replacing the T into U
print(u)

#Q8 String manipulation
s =  input("Enter a DNA string: ")
#sc = s[::-1].replace("T", "A").replace("A", "T").replace("C", "G").replace("G", "C")
sc = s[::-1]

chars1 = "TACG"
chars2 = "ATGC"
index = 0
print(sc)
for char in chars1:
    sc_new = sc.replace(char, chars2[index])
    index = index + 1
print(sc_new)
'''

#Q9 General
important_words = ["list", "function", "string", "integer", "float", "index", "loop", "range"]
definitions = ["A variable containing multiple items.", "It performs specific tasks that are easy to manipulate.", "Characters that aren't functioning as integers.", "A number.", "A decimal.", "Every character has its own place that is numbered as an index, starting at 0 going up.", "To make something run over and over again.", "Run within a range, using minimum, maximum and the size of the steps between."]

for i in range(len(important_words)):
    print(important_words[i].title(), "=", definitions[i])

#Q10 Functions

#Bonus:
#Q1 List comprehension
print(num ** 2 for num in range(1, 11))
 
#Q2 Functions
bob_story = "There once was a little boy named Bob. Bob was a good guy that loved to be with Bob's friends and eat Bob's ice cream during Bob's summer befoe Bob went swimming in Bob's pool."
print(bob_story.count("Bob"))

#Q3 Functions
def palindrome(pal):
    print(f"{pal}")
    pal = f"{pal}"
    if pal == pal[::-1]:
        print(f"Yes, {pal} is a palindrome!")
    else:
        print(f"No, {pal} is not a palindrome.")

palindrome("hello")
palindrome("racecar")
