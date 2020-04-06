class Food:
    def set_food(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer
    def getDetailsFood(self):
        return {"name": self.name, "manufacturer": self.manufacturer}