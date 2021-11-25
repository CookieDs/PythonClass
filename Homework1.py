#This part of the program is me changing the sentence below using functions:
text = "  hi, i AM DOiNg my firST HOMEwork"

print(text) #Printing the text I wrote to show how imperfect it is
print(text.title()) #Every word in the sentence gets first capital letter
print(text.upper()) #Changing the sentence to all upper-case letters
print(text.lower()) #Changing the sentence to all lower-case letters
print(text.strip()) #Removing the white space in the start of the sentence
print(text.title().strip()) #Adding functions together

text1 = "Today is thursday   "
text2 = "tomoRRow IS FRiday"

print(text1.strip() + " and " + text2.lower() + "!") #Printing a text using two different variables

#I'm printing out values of added and multiplied integers:
date = 5 * (3-1)**2 + 5
print("Tomorrow's date is November", date)

#I'm calculating using floating-point numbers:
calc = 3.0 * 0.5
print("3 x 0.5 =", calc) 