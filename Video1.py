#These are notes for the video I watched as homwork where he explains why 0.1 + 0.2 isn't equal to 0.3 in python
#Why floating-point numbers sometimes give a slightly off result


#1st section = sign (1 number: 0 = positive, 1 = negative), 2nd = exponent (11), 3rd = fraction (52)
#Exponents show the scale of the number #Fractions give the digits that build up the number

#In this case, the problem 0.1 + 0.2 is not equal to 0.3 
#Looking at the bits that make up the numbers 0.1 and 0.2
#Fraction contains 52 bits so they end up rounding the decimal and therefore not get the exact answer - Rounding error!

#-0 esists, it says 0 = -0 but they're two different

#You can write infinity as a float using all 1's on exponents and all 0's on fractions

#Nan (not a number): exponent to all 1's, fraction anything but all 0. Nan is not equal to nan