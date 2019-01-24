print "Let's do another project with madlibs that we'll call pylibs"

# query the user for words here
place = raw_input("Enter a place: ")
animal = raw_input("Enter an animal: ")
verb = raw_input("Enter a verb: ")

# convert strings to lowercase
placel = place.lower()
animall = animal.lower()
verbl = verb.lower()

if (len(placel) and len(animall) and len(verbl) > 0 and placel.isalpha() and animall.isalpha() and verbl.isalpha()):
    print "Today I was walking to %s, and I saw a crazy looking %s. I tried to %s it. " % (placel, animall, verbl)
else:
    print "cannot be empty or number"