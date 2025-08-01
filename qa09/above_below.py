numbers=[1,2,8,4,15,11,0,8]

sum_above_10 = 0
sum_below_10 = 0

for number in numbers:
    if number == 0:
        break
    if number > 10:
        sum_above_10 += number
    elif number < 10:
        sum_below_10 += number

print(f"above 10 : {sum_above_10}")
print(f"below 10 : {sum_below_10}")