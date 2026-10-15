
# Sales Analysis Project

sales = [12000, 25000, 18000, 30000, 15000]

total = sum(sales)
average = total / len(sales)
maximum = max(sales)
minimum = min(sales)

count = 0
for amount in sales:
    if amount >= 20000:
        count += 1

print("Total Sales:", total)
print("Average Sales:", round(average, 2))
print("Maximum Sales:", maximum)
print("Minimum Sales:", minimum)
print("Sales >= 20000:", count)
