from random import randint


class Animal:
    def set(self, animalNo, gender, birth, color, humidity, size, temperature, hours_of_light):
        self.animalNo = animalNo
        self.gender = gender
        self.birth = birth
        self.color = color
        self.humidity = humidity
        self.size = size
        self.temperature = temperature
        self.hours_of_light = hours_of_light
        
    def getDetailsAnimal(self):
        return {"animalNo": self.animalNo, "gender": self.gender, "birth": self.birth, "humidity": self.humidity, "size": self.size, "temperature":self.temperature,"hours_of_light":self.hours_of_light}
        