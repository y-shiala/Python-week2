def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
      discount = price * (discount_percent / 100)
      return price - discount
    else:
       return price

#User prompt
try: 
  price = float(input("Enter the original price of the item"))
  discount_percent = float(input("Enter the discoun percentage"))

  final_price = calculate_discount(price, discount_percent)

  if discount_percent >= 20:
    print(f"Final Price after discount. Final Price: ${final_price:.2f}")
  else:
    print(f"Final price without discount. Final Price: ${final_price:.2f}")
    
except ValueError:
   print("Invalid input, please enter numeric values. ")    