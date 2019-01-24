print "This is my second example for Python Projects using strings."

#Ask for info
name = "jeff"
age = 39
color = "fuscia"

#playing around with strings
print name.lower()
print age
print color.upper()

print "Your name is: %s. Your age is %s. Your favorite color is %s." % (name.upper(), str(age), color.lower())
print "The first letter of your name is: " + name[0]
print "There are %s. Letters in your name." % (len(name))

characters = name + str(age) + color

print "You typed in %s Characters" % (len(characters))