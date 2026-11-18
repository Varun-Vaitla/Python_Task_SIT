"""
Question 5: Shopping Bill Calculator
Write a Python program to accept the product name, price, and quantity from the user. Calculate:
- Total price
- 10% discount
- Final amount after discount
"""

product_name=input("Enter product name: ")
product_price=float(input("Enter price of Product: "))
product_quantity=int(input("Enter quantity: "))

toatl_price=product_price * product_quantity
discount= toatl_price*0.10
after_discount=toatl_price - discount
print(" Total Price: ",toatl_price)
print(" Discount: ",discount)
print(" Total Amount after discount: ",after_discount)

