"""
Write a program that asks the user for their age and whether they have a valid driver's license. 
If the user is at least 16 years old and has a valid driver's license
print "You can drive!" 
Otherwise, 
print "Sorry, you are not eligible to drive."
"""

age = input()
age = int(age)

if age < 16:
    print ("Sorry, you are not eligible to drive.")
else:
    print ("You can drive!")
