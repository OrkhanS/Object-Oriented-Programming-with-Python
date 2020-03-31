from random import randint


class Animal:
    def set_animal(self, gender, birth, color, humidity, size, temperature, hours_of_light):
        flag = 0
        while(flag == 0):
            a_id = str(randint(100000, 999999))
            with open('animal.txt') as f:
                    if a_id not in f.read():
                        flag = 1
                        self.animalNo = a_id
        self.gender = gender
        self.birth = birth
        self.color = color
        self.humidity = humidity
        self.size = size
        self.temperature = temperature
        self.hours_of_light = hours_of_light

        f = open("animal.txt", "a+")
        f.write("\n"+a_id+' '+gender+' '+birth+' '+color+' '+humidity+' '+size+' '+temperature+' '+hours_of_light)