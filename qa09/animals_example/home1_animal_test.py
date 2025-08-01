from qa09.animals_example.animal_object import animal
from qa09.animals_example.monkey_object import monkeyObject
# constructors (4 animals , 1 monkey)
dog3_name= "Rexi"
dog1 = animal("Jack",4)
dog2 = animal("Punch",3)
dog3= animal(dog3_name,11)
monkey1 = monkeyObject(12)

# calling function without parameters
dog1.make_noise()
dog2.make_noise()
# calling functions with parameters and returning values
distance_1 = dog1.calc_distance(12,5,"dog1")
distance_2 = dog2.calc_distance(10,3,"dog2")
dog2.calc_distance(4,6,"dog2_second_try")
dog1.calc_distance_no_name(11,4)
# calling function with defaut parameters
dog2.calc_distance_no_name()

# calling dediceted functions from monkey
monkey1.get_living_place()
# calling function for mi=onkey but it define in animal
monkey1.calc_distance(11,23,"Monkey")

if (distance_1> distance_2):
    print ("Distance 1 is longer")


# create dog1
# print by using make_noise function "Hao Hao"
# create dog2
# print by using make_noise function "Hao Hao"