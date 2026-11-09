#1. I would use .get() when information is missing because it doesent cause an error. Brackent notation is used when you know there is a key that needs a value.
#2. Python is more useful for larger datasets because alot of python can be automated.

#Excercise 1
customer = {
    "name": "Drew" ,
    "email": "drewgittelman@usf.edu",
    "tier": "gold",
    "ytd_spending": 1000.00,
}
print(customer['name'])
print(customer['email'])
print(customer['tier'])
print(customer['ytd_spending'])

#Excercise 2
customer["phone"] = "954-610-6680"
customer['tier'] = "platinum"
print(customer)

del customer["email"]
print(customer) 

#Excercise 3
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("Keyerror no email on file")

#Excercise 4
for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print(key)

#Excercise 5
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.1,
    "platinum": 0.15,
}
tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
price = 200
final_price = price * (1 - discount)
print("Tier:", tier)
print("Discount:", discount * 100, "%")
print("Final Price: $", round(final_price, 2))

#Excercise 6
customers = [
    {"name": "Drew", "tier": "platinum"},
    {"name": "Chris", "tier": "gold"},
    {"name": "Alex", "tier": "silver"}
]
for customer in customers:
    name = customer["name"]
    tier = customer["tier"]

    discount = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount
    print(f"{name}: {tier}, Discunt: ${discount_amount:.2f}")

#Excercise 7
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}

}
for product, details in catalog.items():
    if details["stock"] < 20:
        print("LOW STOCK:", product)

#Excercise 8
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

summary = {}
for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    summary[region] = summary.get(region, 0) + amount

for region in sorted(summary):
    print(region, ":", summary[region])
