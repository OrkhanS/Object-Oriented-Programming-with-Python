from random import randint
from datetime import datetime

class Animal_feeding:  
    def feed(self, animal, food, staff):
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        time = now.strftime("%H:%M")
        date = day+"/"+month+"/"+year
        self.animal = animal
        self.date = date
        self.time = time
        self.food = food
        self.staff = staff

    def getDetailsofAnimalFeed(self):
        return {"animal": self.animal,"date":self.date, "time":self.time, "food": self.food, "staff": self.staff}

    def feedingDetails(self, id):
        with open('feeding.txt') as f:
            i=0
            lines = f.read().splitlines()
            print("\n--- Feeding Details of "+ str(id) + " ---\n\n")
            print("------------------------------------------------------\n")
            for line in lines:
                text = line.split(" ")
                if text[0] == str(id):
                    i=1
                    print(line)
                    print("------------------------------------------------------\n")

            if i==0:
                print("!!! - There is no animal, with this id.")
            else:
                print("\n")