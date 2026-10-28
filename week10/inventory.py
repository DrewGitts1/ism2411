#1. The most supring thing about lists is that they can be changed after you create them.
#2. Sophmore year of HS my 2 friends and I made a mock business of a food truck in class, using formulas and lists would have made it so much faster then manually typing in excel.
#Excercise 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

#Excercise 2
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

#Excercise 3
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

#Excercise 4
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

#Excercise 5
coords = (40.7128, -74.0060)
try:
    coords[0]= 99
except TypeError:
    print("Tuples cant be changed, so that is why its useful for coordinates")
print(coords)

#Excercise 6
sales = [100, 250, 75, 480, 200]
print(f"Total: {sum(sales)}")
print(f"Count: {len(sales)}")
print(f"Average: {sum(sales) / len(sales)}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

#Excercise 7
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print(prices)
print(discounted)

#Excercise 8
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)
print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Avg: {round(sum(high_sales) / len(high_sales), 2)}")
