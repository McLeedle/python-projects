print "This is our forth example and will cover conditionals and control flow"


#create function storestock with a variable of instock
def storestock(instock):
    print "This store has %s Items in stock." % (str(instock))

#conditional parameters to evaluate if instock is true and prints if true
    if instock == 400:
        return "Store's stock is full"
    elif instock > 400:
        return "Store's stock is overflowing "
    elif instock < 200 and instock > 0:
        return "Store's stock is half full"
    else:
        return "Store is out of stock"


#these statements change the value of instock to test and make all statements true
print storestock(400)
print storestock(800)
print storestock(150)
print storestock(0)