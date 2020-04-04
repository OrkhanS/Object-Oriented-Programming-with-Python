class Application:
    staffList = []
    foodList = []
    animalList = []
    feedingList = []
#________________________________________________________STAFF________________________________________________________

    def addStaffToList(self, staffObject):
        self.staffList.append(staffObject)

    def getAllStaff(self):
        return self.staffList

#________________________________________________________Food________________________________________________________

    def addFoodToList(self, FoodObject):
        self.foodList.append(FoodObject)

    def getAllFood(self):
        return self.foodList

#________________________________________________________Animal________________________________________________________

    def addAnimalToList(self, AnimalObject):
        self.animalList.append(AnimalObject)

    def getAllAnimal(self):
        return self.animalList

#________________________________________________________Feeding________________________________________________________

    def addFeedingToList(self, FeedObject):
        self.feedingList.append(FeedObject)

    def getAllFeedingDetails(self):
        return self.feedingList