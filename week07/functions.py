#1. The first bug I spotted was the missing colon on the second for loop. I found it by running the code and seeing a syntax error which I then looked for throughout the code. 
#2. Apply_discount takes 2 parameters which are price and tier, it checks the tier through an if elif else statement and applies a discount based on whichever tier it is. I think a colleague could use this function without seeing its body if they are familiar with the tiers beforehand.
#3. I didnt use AI like chatgpt but I did use the feature on VS studio where I can hit tab and it will finish the code for me. Im familiar with the stuff being coded right now, so it mainly was a shortcut on the amount of time I spent typing.
#Exercise 1
def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

#Exercise 2
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

#Exercise 3

def final_price(price, tax_rate, discount_tier):
    discount_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discount_price, tax_rate)
    return discount_price + tax

print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

#Exercise 4

orders = [(200, 'gold') , (150, 'silver'), (100, 'bronze'), (50, 'none')]

for price, tier in orders:
    total = final_price(price, 0.07, tier)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

#Excercise 5
#The first error was a missing colon on the second for loop which caused a syntax error because loops need a : at the end of it.
#The second error was the >= sign on the while loop, it should have just been > because the indext has a length of 5, even though the last index is 4, and since theres an = sign the loop would keep trying to accsess the 5th index which doesent exist. 


#Excercise 6

x = 100
def double_it():
    x = 999
    return x *2

print(x)
print(double_it())
print(x)
#I thought the first x would be 100, second x would be 1998, and the third x would be 999.
#X = 100 is a global value but the x inside the function is a local variable so it is only present when the function is called. Global X isnt affected by the local(function) X
          