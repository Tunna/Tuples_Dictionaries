
# # str = "1,2,3,4,5"
# # split_str = str.split(",")
# # # split_str = int(split_str)
# # print split_str

# # str = "One fish two fish red fish blue fish"
# # split_str = str.split("fish")
# # print split_str
def calculate_grocery_bill(quantity, price):
	return quantity * price 

str = ("item:apples,quantity:4,price:1.50/n")    #string to split the string at the commas
split_str = str.split(",")
quantity_str = split_str[1]
quantity_list = split_str[1].split(":")
quantity = quantity_list[1]
quantity = float(quantity)
# print split_str
# print quantity

price_str = split_str[2]   # split the string at index 2, yields ("price:1.50\n")
price_list = price_str.split(":")
price_list = split_str[2].split(":")   #take the split string at index 2 and split it again at the colon, yields ("price", "1.50\n")
price = price_list[1]   # assign a variable to index 2, yields ("1.50")
price = "1.50\n".strip()
price = float(price)
# print price 

my_list = ["item:apples,quantity:4,price:1.50\n","item:pears,quantity:5,price:2.00\n","item:cereal,quantity:1,price:4.49\n"] 
str = "".join(my_list)
split_str1 = str.split(",")
quantity_str1 = split_str1[3]
quantity_list1 = split_str1[3].split(":")
quantity1 = quantity_list1[1]
quantity1 = float(quantity1)
print quantity1

str["item:apples,quantity:4,price:1.50\n","item:pears,quantity:5,price:2.00\n","item:cereal,quantity:1,price:4.49\n"] 
split_str2 = str.join(",")
# price_str1 = split_str2[4]   # split the string at index 2, yields ("price:1.50\n")
# price_list1 = price_str.pslit(":")
# price_list1 = split_str[4].split(":")   #take the split string at index 2 and split it again at the colon, yields ("price", "1.50\n")
# price1 = price_list[1]   # assign a variable to index 2, yields ("1.50")
# price1 = "2.00\n".strip()
# price1 = float(price)
print split_str





bill = calculate_grocery_bill(quantity, price)
print bill


	
