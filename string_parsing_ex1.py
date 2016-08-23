str = "item:apples,quantity:4,price:1.50/n"   #string to split
split_str = str.split(",")   # split the string at the commas, yields the result ("item:apples", "quantity:4", "price:1.50\n")
price_str = split_str[2]   # split the string at index 2, yields ("price:1.50\n")
price_list = split_str[2].split(":")   #take the split string at index 2 and split it again at the colon, yields ("price", "1.50\n")
price = price_list[1]   # assign a variable to index 2, yields ("1.50")
price = float(price)
#testing
# print split_str
# print price_list
print price