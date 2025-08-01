from qa09.animals_example.animal_object import animal


class monkeyObject(animal):

    def __init__(self,age):
        self.age = age

    def get_living_place(self):
        print ("Living place of the monkey is Africa")
        return "Africa"
