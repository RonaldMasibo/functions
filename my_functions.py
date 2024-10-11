
price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the percentage discount of the product: "))

def calculate_discount(price, discount_percentage):

    if discount_percentage >= 20 and discount_percentage < 100:
        discounted_price = (discount_percentage/100) * price
        final_price = price - discounted_price
        return final_price
    
    elif discount_percentage < 20:
        print("There is no discount on this item!!")
        return price
    
    else:
        return ("Discount can't be more than the original price")

print(calculate_discount(price, discount_percentage))