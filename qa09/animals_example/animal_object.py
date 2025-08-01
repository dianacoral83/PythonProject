from qa09.animals_example.monkey_object import monkeyObject


class animal:

    def __init__(self,name,age):
        print (f"init animal in age {age}")
        age= age+1
        self.noise = "Hao Hao"
        self.name=name
        self.age=age


    def make_noise(self):
        print ("Hao Hao")

    def calc_distance(self,time,speed,animal_name):
        print ("calculating the distance ")
        distance = time * speed
        print (f"the distance of {animal_name} is {distance}")
        return distance
# example of default values , using in case of no parameters
    def calc_distance_no_name(self,time=3,speed=8):
        print (f"calculating the distance {time} , {speed} ")
        distance= time * speed
        print (f"the distance of {self.name} is {distance}")
        return self.name


if __name__ == '__main__':
    object1 = animal("<UNK>",1)
    object1.make_noise()
    #monkey = monkeyObject(1)
    #monkey.get_living_place()
