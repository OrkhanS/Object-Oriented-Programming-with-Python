from random import randint


class Food:
    def set_food(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer
        f = open("food.txt", "a+")
        f.write("\n"+name+' '+manufacturer)

    def foodforGivenAnimal(self, id):
        with open('feeding.txt') as f:
            i = 0
            lines = f.read().splitlines()
            print("\n--- Foods that have been fed to " + str(id) + " ---\n\n")
            print("------------------------------------------\n")

            for line in lines:
                text = line.split(" ")
                if text[0] == str(id):
                    i = 1
                    print("Name: " + text[3])
                    print("Manufacturer: " + text[4]+"\n")
                    print("------------------------------------------\n")
            if i == 0:
                print("There is no animal, with this id.")
            else:
                print("\n")
