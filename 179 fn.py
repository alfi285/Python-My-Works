# Question 5:
# Combining Arguments, Arbitrary Arguments, Keyword Arguments, and Return Values
# -Define a function called order_summary that takes a required argument
# customer_name, an arbitrary number of *items, and a keyword argument delivery_fee with a default value of 5.
# The function should return a string listing the customer name, items ordered,
# and the total cost (sum of item prices + delivery fee). Call the function
# with the arguments customer_name="John Doe", items priced at 10, 20, and 15, and delivery_fee=3.

def order_summary(name,deliveryfee=5,**items):
     print(f"Customer name:{name}")
     sum = 0
     for key,value in items.items():
         sum = sum + value
         print(f"{key}:{value}")
     print("Total cost:",sum+deliveryfee)

order_summary("John",3,apple = 10,banana= 20,cherry = 15)
