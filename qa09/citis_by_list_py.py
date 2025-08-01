from qa09.lesson_1 import even_number

cities = ["Rome","New-----York","London","Tokyo","Tel-Aviv"]




for city in cities:
    l = len(city)
    print(f"the length of {city} is {l}")
    if (city.count("l")>0):
        print (f"found city with L , city name is {city} ")


cities = ["fgfggf","gfgf"]

for city in cities:
    l=len(city)
    print(l)
    print (city)

list=[1,2,3,4] # Define list
B= 5 in list #False
A= 1 in list #True
print(len(list))
print ("hjhjhjhjhjhjhjhjhjhjh ",A,B)

list.insert(2,5)
print(list)

nums=[1,2,3,4,5,6,7,8]
for num in nums:
    if num%2==0:
        print("even number is ",num)

mails = ["dfdf@hgh.com","<gggg.com>","pomik@jjjj.com"]

for mail in mails:
    if mail.count(".")>0 or mail.count("@")>0:
        print(mail)

ages= [5,15,13,25,71]
for age in ages:
    if age <= 18 :
        print("child :" , age)
    if age >= 18 and age <= 61 :
        print("adult :" , age)
    if age >= 61 and age <= 120 :
        print("senior :" , age)

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
