# this is our fifth python lesson example showing what we've learned with functions
import math

print "Welcome to our example!"


def sqroot():
    """returns the square root of the user's number"""
    number = raw_input("Enter a number: ")
    if int(number):
        print math.sqrt(int(number))
    else:
        print "You must enter a number!"


sqroot()

print "What you just saw was outputted from a function in our program!"
print "Let's try another!"


def largest_number(a=raw_input("Enter a number: "), b=raw_input("Enter a second number: ")):
    """returns the largest of the two numbers entered"""
    if int(a) and int(b):
        print "The largest number your entered was: %s" % max(int(a), int(b))
    else:
        print "Please enter a valid number! "


largest_number()
