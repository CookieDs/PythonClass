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


what_now = "Now, I'm goNNA do MoRE stUFF beCAUse Github IS CurrentLY NOt workING FOr me."
print(what_now.title())

good = "it'S GOoD to PraCTise LIke this mULTIple times" #Talking to myself to practise functions
why = "   Why?, you MAy ask"
answer = "WeLL, beCAuse\tYou LeaRN them BETTEr" #Trying out the \t
question = "is that tRUE?  "
answer2 = "    If it wASN't I WOuldn't be RememberING these FunCtions that I'm usiNg"
next = "yOU THink to yourself:" #Writing this one to use the + too
you = "Yeah, THat MAkes sense"

print(good.upper()) #Printing out the whole conversation with myself
print(why.lstrip().lower())
print(answer.upper())
print(question.rstrip().lower())
print(answer2.lstrip().upper())
print(next.title() + " " + you.lower()) #Realizing there is a missing sace so I added " " like Bedir taught us