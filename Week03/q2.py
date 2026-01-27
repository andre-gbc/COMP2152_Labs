print("="*50)
print("Question 2: Shopping Cart")
print("="*50)

cart = ["apple", "banana", "orange", "bread", "apple", "milk"]

apple_count = cart.count("apple")
print("Number of apples in the cart:", apple_count)

milk_position = cart.index("milk")
print("Position of milk in the cart:", milk_position)

cart.remove("apple")

# Pop an item
removed_item = cart.pop()
print("Removed item from the cart:", removed_item)

print("Is orange in the cart?", "orange" in cart)
print("Final Shopping Cart:", cart)

