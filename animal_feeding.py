from random import randint
from datetime import datetime

class Animal_feeding:  
    def feed(self, a_id, foodName, manufacturer, weight, staff):
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        time = now.strftime("%H:%M")
        date = day+"/"+month+"/"+year
        self.animalNo = a_id
        self.date = date
        self.time = time
        self.foodName = foodName
        self.manufacturer = manufacturer
        self.weight = weight
        self.staff = staff

    def getDetailsofAnimalFeed(self):
        return {"animalNo": self.a_id, "foodName": self.foodName, "manufacturer": self.manufacturer, "weight": self.weight, "staff": self.staff}

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