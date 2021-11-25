#Strings
#Write it as str
desc = "My name is Diana. I'm almost 17 years old and I live in Sweden." #Description of me

(print(desc))

#Functions
name = "diANa"

print(name.title())
print(name.upper()) #All captial letters
print(name.lower()) #All low letters

#String concatenation
first_name = "Diana"
last_name = "Salim"

print(first_name + " " + last_name) #String concatenation is the +, it combines strings. The " " is to put a space between first and last name :)

full_name = first_name + " " + last_name
print(full_name.title()) 

#Whitespace
print("Hello World") #There's a space between the two words
print("Hello\tWorld") #\t=tab, t isn't shown
#\n = new line 

#Stripping Whitespaces - removing whitespaces
name = "  Diana  "
print(name.lstrip() + last_name)
print(name.rstrip() + last_name)
print(name.strip() + last_name) #Removes only left and right

#Execises:
#3
his_first_name = "Tarik" #Beautiful guy
his_last_name = "Bergström" #Soon gonna be mine ;)
his_name = his_first_name + " " + his_last_name
his_sentence = "There is a boy named " + his_name + " that I love so much."
print(his_sentence)

#Numbers
#Integer
print(3 + 2)
print(3 - 2)
print(5 * 2)
print(4 / 2)

#Power
calc = 5**2 #To the power of 2, instead of 5^2
print(calc)

calc = 5 + 2 * 2
print(calc)

calc = (5 + 2) * 2 #Just like normal maths :)
print(calc)

#Floating-point numbers
print(0.1 + 0.1) #The .1 is not an integer
print(0.1 + 0.2) #Sometimes this happens in python but dw

#Exeercises:
#3
print(0.3 + 0.6) 

'''
This
is
a
multiline
comment
'''
#import this #We are using python in this matter, easter egg 