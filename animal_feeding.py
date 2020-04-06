from datetime import datetime

class Animal_feeding:
    def feed(self, animal, food, weight, staff):
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
        self.weight = weight
    def getDetailsofAnimalFeed(self):
        return {"animal": self.animal,"date":self.date, "time":self.time, "food": self.food, "weight":weight, "staff": self.staff}