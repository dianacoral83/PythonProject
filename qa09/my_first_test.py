from operator import index
from platform import processor

print('my_name_is_Diana')
first_name = "Diana"
last_name = "Coral"
legs_amount = 2
full_name ="Leo Messi"
price="25nis"

print (f"my name is {first_name} {last_name} I have {legs_amount} legs")
len_first_name = len(first_name)
len_last_name = len(last_name)
print(len_first_name, len_last_name)
print("test and")

price_by_slice = price[-3:]

print ("test end")

single_char = full_name[5]
single_char = full_name[-3]

full_name = full_name.replace

FirstName = ("Diana")
LastName = ("Coral")

print(FirstName, LastName)

print(first_name,last_name[0])

hello = "Hello World"
h = hello[0:5]
w = hello[6:11]

print(h)
print(w)


x = 20%2

print(x)
i=1
while i <= 6:
    print(i)
    i +=1
for a in range(1, 100):
    if a * a == 4 * a:
        print('side length:', a)

div_by_3 = []
div_by_5 = []
div_by_3_and_5 = []

for i in range(1, 101):
    if i % 3 == 0:
        div_by_3.append(i)
    if i % 5 == 0:
        div_by_5.append(i)
    if i % 3 == 0 and i % 5 == 0:
        div_by_3_and_5.append(i)

print("Divisible by 3:", div_by_3)
print("Divisible by 5:", div_by_5)
print("Divisible by both 3 and 5:", div_by_3_and_5)




