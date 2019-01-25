print "This project was done off of stream to test my own capabilities"
print "Tip Calculator"

# ask user for cost of meal
sale = input("The cost of your meal(in number):  ")

# tip variable declaration
tip15 = .15
tip17 = .17
tip20 = .2

# the tip given by the user
option = input("How much would you like to tip? 1. 15% 2. 17% 3. 20%: ")

if option == 1:
    sale = float(sale) * tip15 + float(sale)
    print "Your total is: %s " % (str(sale))
    tip = float(sale) * tip15
    print "Your tip was: %s " % str(tip)

elif option == 2:
    sale = float(sale) * tip17 + float(sale)
    print "Your total is: %s " % (str(sale))
    tip = float(sale) * tip17 + sale
    print "Your tip was: %s " % (str(tip))

else:
    sale = float(sale) * tip20 + float(sale)
    print "Your total is: %s" % (str(sale))
    tip = float(sale) * tip20 + sale
    print "Your tip was: %s " % (str(tip))
