print "Welcome to my first github python example"
print "This example will demonstrate my understanding of Variables"

# This variable is a float because it contains a decimal value
gas_price = 2.97
sales_tax = 0.08
final_price = sales_tax * gas_price + gas_price

# This variable is an int because it is not a decimal
gas_purchased = 10

# This variable is a string because it contains a string
gas_station_name = "Python Gas"

print "Welcome to " + gas_station_name + ". The price for gas here is: " + str(gas_price) + ". We charge sales tax which is: " + str(sales_tax)

# client purchases 10 gallons, do calculation
total_sale = gas_purchased * final_price

# print the result
print "You purchased " + str(gas_purchased) + " Gallons of gas. Your total is: " + str(total_sale)