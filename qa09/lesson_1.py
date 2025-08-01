from unicodedata import digit

from qa09.my_first_test import first_name, last_name

number1=35
number2=20
number3=10
avg=(number1+number2+number3)/3
print(avg)


first_name='diana'
last_name='corals'
length1=len(first_name)
length2=len(last_name)
if length1>length2:
    print(first_name)
else:
    print(last_name)

number4=1
number5=8
start = min(number4, number5)
end = max(number4, number5)
for x in range(start, end): # start =1, end=8
    if x % 2 == 0:
        print(x)

even_number= range(18 ,22)
print(even_number)

num =56
if 10 <= num <= 99:
    digit1 = num % 10 # 5*10=50, 56-50=6
    digit2 = num // 10 # 56:10=5

    sum = digit1 + digit2
    print(sum)

grade=90
if(grade <50):
    print ("into less than 50")





