from random import randint

class Observation:
    def set_observation(self, a_id, date, time, weight, temperature, note, staff):
        self.a_id = a_id
        self.date = date
        self.time = time
        self.weight = weight
        self.note = note
        self.temperature = temperature
        self.staff = staff
        print("\nAnimals should be observer more than three times a day!!")
        f = open("observation.txt", "a+")
        f.write("\n"+str(a_id)+' '+str(date)+' '+str(time)+' '+str(weight)+' '+str(temperature)+' '+str(note)+' '+staff)
    
    def details(self, id):
        with open('observation.txt') as f:
            i=0
            lines = f.read().splitlines()
            print("\n--- Observation Details of "+ str(id) + " ---\n\n")
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

    def staffWhoObserved(self, id):
        with open('observation.txt') as f:
            i=0
            lines = f.read().splitlines()
            print("\n--- Staff who observed "+ str(id) + " ---\n\n")
            print("------------------------------------------------------\n")
            for line in lines:
                text = line.split(" ")
                if text[0] == str(id):
                    i=1
                    with open('staff.txt') as f1:
                        lines1 = f1.read().splitlines()
                        for line1 in lines1:
                            text1 = line1.split(" ")
                            if text1[1].lower() == text[6].lower() and text1[2].lower() == text[7].lower():
                                print(line1+"\n")
                                j=1
                    print("------------------------------------------------------\n")

            if i==0:
                print("\n!!! - There is no animal, with this id, which is observed.")
                j=1
            else:
                print("\n")