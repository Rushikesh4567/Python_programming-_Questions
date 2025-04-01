#problem 8
def shopping_cart():
    cart = []
    
    while True:
        item = input("Enter item to add to cart (type 'done' to finish): ")
        if item.lower() == 'done':
            break
        else:
            cart.append(item)  
    
    print("\nItems in your cart:")
    
    i = 1  
    for product in cart:
        print(f"{i}. {product}")
        i += 1  

shopping_cart()
