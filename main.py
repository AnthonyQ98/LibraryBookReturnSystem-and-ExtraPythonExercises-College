"""
Anthony Quinn
X00138635
14/12/2020
Week 10 Lab Exercises
"""

#Exercise 1

length = 0
width = 0
price = 0
amount = 0
count = 0

price_per_metre = float(input("Please enter the price per metre of the office space here: "))

print("\t\t\t5m\t\t\t10m\t\t\t15m\t\t\t20m\t\t\t25m\t\tAverage Cost")
for length in range(10, 101, 10):
    total = 0
    print(length, "m\t", end="")
    for width in range(5, 26, 5):
        count += 1
        price = width * length * price_per_metre
        price = round(price, 2)
        amount += price
        print("€", price, end="\t")
    print("€", amount / count, end="\t")
    print()

#Exercise 2
"""
week_list = []
total = 0
average = 0
for number in range(7):
    rainfall = float(input("Please enter the rainfall in centimetres here: "))
    week_list.append(rainfall)

for rainfall in week_list:
    total += rainfall

average = total / len(week_list)
print("The total amount of rainfall for the week was", str(round(total, 2)) + "cm.")
print("The average amount of rainfall for the week was", str(round(average, 2)) + "cm.")
"""


#Exercise 3
"""
intialize_list = []

for number in range(10, 101, 10):
    intialize_list.append(number)
    if number % 2 == 0:
        print(number)

userNumber = int(input("Please enter number here: "))
intialize_list.insert(0, userNumber)
print(intialize_list)

if 30 in intialize_list:
    location30 = intialize_list.index(30)
    intialize_list.remove(intialize_list[location30])
    print(intialize_list)
"""