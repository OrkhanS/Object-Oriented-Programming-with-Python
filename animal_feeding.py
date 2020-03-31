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
        flag = 1
        i=0
        with open('feeding.txt') as f:
            lines = f.read().splitlines()
            for line in lines:
                if line.count(str(a_id)) and line.count(date):
                    i += 1
            if i == 2:
                flag = 0
                return False
        if flag==1:
            self.date = date
            self.time = time
            self.foodName = foodName
            self.manufacturer = manufacturer
            self.weight = weight
            self.staff = staff

            f=open("feeding.txt", "a+")
            f.write("\n"+str(a_id)+' '+date+" "+time+" "+ foodName+" "+manufacturer+" "+str(weight)+" "+staff)
            return True
    
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