print "This is the first project that will have us use what we've learned so far!"
print "PygLatin"

# variable to store the suffix
pyg = 'ay'

# variable to store the original word
oword = raw_input("Enter a word: ")

# variable to store the word in lowercase
lword = oword.lower()

# variable to store the first letter of the lowercase word
first = lword[0]

# variable to store the new modified word
new_word = lword + first + pyg
new_word = new_word[1:len(new_word)]

# check if the value of oword isn't blank or a number
if len(oword) > 0 and oword.isalpha():
    print new_word
else:
    print "cannot be empty or number"
