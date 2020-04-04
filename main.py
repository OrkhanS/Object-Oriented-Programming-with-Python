from Staff_room import Staff_room
from animal_feeding import Animal_feeding
from food import Food
from animal import Animal
from observation import Observation
import random
from application import Application
from random import randint
from datetime import datetime
from dateutil.parser import parse


appliaction = Application()

# ________________________________________________________STAFF________________________________________________________


def addStaff():
    try:
        print("\nPlease type details of Staff\n")
        fname = input("Name: ")
        sname = input("Surname: ")
        office = input("Office: ")
        tel = input("Tel: ")
        print("\n")
        flag = 0
        while(flag == 0):
            staff_id = str(randint(100000, 999999))
            staffList = appliaction.getAllStaff()
            if len(staffList) != 0:
                for staff in staffList:
                    if staff_id not in staff["staff_id"]:
                        flag = 1
            else:
                flag = 1
        addFlag = 1
        if len(str(tel)) != 4:
            print("\nError, tel should have of 4 digis!\n")
            addFlag = 0
        if office[1:2] != '-' or len(office[2:]) != 3:
            print(
                "\nError, office should should have A-XXX, where X represent a digit!\n")
            addFlag = 0
        if addFlag == 1:
            newStaff = Staff_room()
            newStaff.set(staff_id, fname, sname, office, tel)
            appliaction.addStaffToList(newStaff)
            print("\nA new staff added successfully\n")

    except:
        print("\nSome Error occured, try again.\n")
    main()


def ReportStaff():
    try:
        print("\nDetails of Staff\n")
        contents = appliaction.getAllStaff()
        print("\n-----------------------------------\n")
        for staffContent in contents:
            print(str(staffContent.staff_id)+" "+ str(staffContent.first_name)+" "+str(staffContent.last_name)+" "+str(staffContent.office)+" "+str(staffContent.tel)+"\n")
        print("\n-----------------------------------")
        fileName = "StaffDetails " + str(random.random())
        f = open(fileName, "a+")
        for staff in contents:
            f.write(str(staff)+"\n")
        f.close()
    except:
        print("\nSome Error occured, try again.\n")
    main()

# ________________________________________________________Food________________________________________________________


def addFood():
    try:
        print("Please type details of Food")
        name = input("Name: ")
        manufacturer = input("Manufacturer: ")
        weight = input("Weight: ")
        newFood = Food()
        newFood.set_food(name, manufacturer, weight)
        appliaction.addFoodToList(newFood)
        print("\nA new food added successfully\n")
    except:
        print("\nSome Error occured, try again.\n")
    main()

def ReportFood():
    try:
        print("\nDetails of Foods\n")
        contents = appliaction.getAllFood()
        print("\n-----------------------------------\n")
        for foodContent in contents:
            print(str(foodContent.name)+" "+ str(foodContent.manufacturer)+" "+str(foodContent.weight)+"\n")
        print("\n-----------------------------------\n")
        # fileName = "FoodDetails " + str(random.random())
        # f = open(fileName, "a+")
        # for animal in contents:
        #     f.write(str(animal)+"\n")
        # f.close()
    except:
        print("\nSome Error occured, try again.\n")
    main()
  
# ________________________________________________________ANIMAL________________________________________________________

def addAnimal():
    try:
        print("Please type details of Animal: ")
        gender = input("Gender: ")
        birth = input("Birth: ")
        color = input("Color: ")

        print("\nPlease type Environment Conditions: \n")
        humidity = input("Relative Humidity: ")
        size = input("Enclosure Size (m2): ")
        temperature = input("Temperature: ")
        hours_of_light = input("Hours of light per day: ")

        flag = 0
        while(flag == 0):
            animalNo = str(randint(1000, 9999))
            animalList = appliaction.getAllAnimal()
            if len(animalList) != 0:
                for animal in animalList:
                    if animalNo not in animal["animalNo"]:
                        flag = 1
            else:
                flag = 1
        newAnimal = Animal()
        newAnimal.set(animalNo, gender, birth, color, humidity, size, temperature, hours_of_light)
        appliaction.addAnimalToList(newAnimal)
        print("\nA new animal added successfully\n")
    except:
        print("\nSome Error occured, try again.\n")
    main()

def ReportAnimal():
    try:
        print("\nDetails of Animals\n")
        contents = appliaction.getAllAnimal()
        print("\n-----------------------------------\n")
        for animalContent in contents:
            print(str(animalContent.animalNo)+" "+ str(animalContent.gender)+" "+str(animalContent.birth)+" "+str(animalContent.color)+" "+str(animalContent.humidity)+" "+str(animalContent.size)+" "+str(animalContent.temperature)+" "+str(animalContent.hours_of_light)+"\n")
        print("\n-----------------------------------\n")
        fileName = "AnimalDetails " + str(random.random())
        f = open(fileName, "a+")
        for animal in contents:
            f.write(str(animal)+"\n")
        f.close()
    except:
        print("\nSome Error occured, try again.\n")
    main()
   
# _____________________________________________________ANIMAL FEEDING________________________________________________________


def animalFeed():
    # try:
    print("Please type details of Animal: ")
    newAnimalFeed = Animal_feeding()
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H:%M")
    date = day+"/"+month+"/"+year
    animal_id = input("What is ID of Animal: ")
    foodName = input("Food Name: ")
    staff_id = input("What is ID of Staff: ")

    animals = appliaction.getAllAnimal()
    staffs = appliaction.getAllStaff()
    foods = appliaction.getAllFood()
    flagAnimal = 1
    flagStaff = 1
    flagFood = 1

    for animal in animals:
        if animal_id == animal.animalNo:
            flagAnimal = 0
            animalObject = animal
    if flagAnimal == 1:
        print("\nThere is no such animal, try again!!")

    for staff in staffs:
        if staff_id == staff.staff_id:
            staffObject = staff
            flagStaff = 0

    if flagStaff == 1:
        print("\nThere is no such staff, try again!!")

    for food in foods:
        if foodName == food.name:
            flagFood = 0
            foodObject = food
    if flagFood == 1:
            print("\nThere is no such food, try again!!")

    if(flagAnimal == 0 and flagStaff == 0 and flagFood == 0):
        isFedAlready = 0
        count = 1
        feedingDetails = appliaction.getAllFeedingDetails()
        for feeding in feedingDetails:
            if str(animal_id) == str(feeding.animal.animalNo) and str(date) == str(feeding.date):
                count+=1
        if count == 2:
            print("Uh-oh, you cannot feed an animal more than 2 times a day!!")
        else:
            newAnimalFeed.feed(animalObject, foodObject, staffObject)
            appliaction.addFeedingToList(newAnimalFeed)
            print("\nA feeding record added successfully\n")
        
    # except:
    #     print("\nSome Error occured, try again.\n")
    main()

def feedingDetails():
    # try:
    print("Please type Following details: \n")
    animalnum = input("AnimalNo: ")
    startDate = input("Start Date (12/08/2020):  ")
    endDate = input("End Date (12/08/2020): ")
    animals = appliaction.getAllAnimal()
    feeding = appliaction.getAllFeedingDetails()
    flagAnimal = 1
    for fed in feeding:
        fed.animal
        if animalnum == fed.animal.animalNo:
            flagAnimal = 0
    if flagAnimal == 1:
        print("\nThere is no such animal or this animal hasn't been fed before, try again!!")
    else:
        newFeedingList = []
        for feed in feeding:
            feedDate = parse(feed.date)
            start = parse(startDate)
            end = parse(endDate)
            if feedDate >= start and feedDate <= end:
                newFeedingList.append(str(feed.animal.animalNo)+" "+str(feed.food.name)+" "+str(feed.food.manufacturer)+" "+str(feed.food.weight)+" "+str(feed.staff.first_name)+" "+ str(feed.staff.last_name))
        print("\n-----------------------------------")
        print(newFeedingList)
        print("\n-----------------------------------")
        fileName = "FeedingDetails " + str(random.random())
        f = open(fileName, "a+")
        for feed in newFeedingList:
            f.write(str(feed)+"\n")
        f.close()
    # except:
    #     print("\nSome Error occured, try again.\n")
    main()


# _____________________________________________________Observation________________________________________________________


def addObservation():
    try:
        print("Please type details of Observation\n")
        animalNo = input("AnimalNo: ")
        staffID = input("StaffId: ")
        weight = input("Animal Weight (kg): ")
        temperature = input("Temperature (C*): ")
        note = input("Note: ")
        animals = appliaction.getAllAnimal()
        staffs = appliaction.getAllStaff()
        flagAnimal = 1
        flagStaff = 1

        for animal in animals:
            if animalNo == animal.animalNo:
                flagAnimal = 0
                animalObject = animal
        if flagAnimal == 1:
            print("\nThere is no such animal, try again!!")
            for staff in staffs:
                if staffID == staff.staff_id:
                    staffObject = staff
                    flagStaff = 0

        if flagStaff == 1:
            print("\nThere is no such staff, try again!!")

        newObservation = Observation()
        newObservation.set_observation(animal, weight, temperature, note, staff)
        appliaction.addObservationingToList(newObservation)
        print("\nAn observation record added successfully\n")
    except:
        print("\nSome Error occured, try again.\n")
    main()

def ReportObservation():
    # try:
    print("Please type Following details: \n")
    animalnum = input("AnimalNo: ")
    startDate = input("Start Date (12/08/2020):  ")
    endDate = input("End Date (12/08/2020): ")
    animals = appliaction.getAllAnimal()
    observation = appliaction.getAllObservationDetails()
    flagAnimal = 1
    for observed in observation:
        observed.animal
        if animalnum == observed.animal.animalNo:
            flagAnimal = 0
    if flagAnimal == 1:
        print("\nThere is no such animal or this animal hasn't been observed before, try again!!")
    else:
        newobservationList = []
        for observed in observation:
            observedDate = parse(observed.date)
            start = parse(startDate)
            end = parse(endDate)
            if observedDate >= start and observedDate <= end:
                newobservationList.append(str(observed.animal.animalNo)+" "+str(observed.date)+" "+str(observed.time)+" "+str(observed.weight)+" "+str(observed.temperature)+" "+ str(observed.note))
        print("\n-----------------------------------")
        print(newobservationList)
        print("\n-----------------------------------")
        fileName = "observationDetails " + str(random.random())
        f = open(fileName, "a+")
        for observed in newobservationList:
            f.write(str(observed)+"\n")
        f.close()
    # except:
    #     print("\nSome Error occured, try again.\n")
    main()

def staffWhoObserved():
    # try:
    print("Please type Following details: \n")
    animalnum = input("AnimalNo: ")
    startDate = input("Start Date (12/08/2020):  ")
    endDate = input("End Date (12/08/2020): ")
    animals = appliaction.getAllAnimal()
    observation = appliaction.getAllObservationDetails()
    flagAnimal = 1
    for observed in observation:
        observed.animal
        if animalnum == observed.animal.animalNo:
            flagAnimal = 0
    if flagAnimal == 1:
        print("\nThere is no such animal or this animal hasn't been observed before, try again!!")
    else:
        newobservationList = []
        for observed in observation:
            observedDate = parse(observed.date)
            start = parse(startDate)
            end = parse(endDate)
            if observedDate >= start and observedDate <= end:
                newobservationList.append(str(observed.staff.staff_id)+" "+str(observed.staff.first_name)+" "+str(observed.staff.last_name)+" "+str(observed.staff.office)+" "+str(observed.staff.tel))
        print("\n-----------------------------------")
        print(newobservationList)
        print("\n-----------------------------------")
        fileName = "observationDetails " + str(random.random())
        f = open(fileName, "a+")
        for observed in newobservationList:
            f.write(str(observed)+"\n")
        f.close()
    # except:
    #     print("\nSome Error occured, try again.\n")
    main()

def foodsGiven():
    # try:
    print("Please type Following details: \n")
    animalnum = input("AnimalNo: ")
    animals = appliaction.getAllAnimal()
    feeding = appliaction.getAllFeedingDetails()
    flagAnimal = 1
    for fed in feeding:
        fed.animal
        if animalnum == fed.animal.animalNo:
            flagAnimal = 0
    if flagAnimal == 1:
        print("\nThere is no such animal or this animal hasn't been fed before, try again!!")
    else:
        newFeedingList = []
        print("\n-----------------------------------")

        for feed in feeding:
            if animalnum == feed.animal.animalNo:
                newFeedingList.append(str(feed.food.name)+" "+str(feed.food.manufacturer))
                print(newFeedingList)

        print("\n-----------------------------------")
        fileName = "GivenFoodDetails " + str(random.random())
        f = open(fileName, "a+")
        for feed in newFeedingList:
            f.write(str(feed)+"\n")
        f.close()
    # except:
    #     print("\nSome Error occured, try again.\n")
    main()


def main():

    choice = '0'
    while choice == '0':
        print("\n\n--- Choose 1 of 10 choices ---\n\n")
        print("Choose 1 to add Staff")
        print("Choose 2 to add Animal")
        print("Choose 3 to add Food")
        print("Choose 4 to add Feeding Information")
        print("Choose 5 to add Observation")
        print("Choose 6 for Details of all staff")
        print("Choose 7 for Details of all animals")
        print("Choose 8 for Details of Feeding")
        print("Choose 9 for Details of Foods")


        print("Choose 15 to exit")

        choice = input("Please make a choice: ")

        options = {
            1: addStaff,
            2: addAnimal,
            3: addFood,
            4: animalFeed,
            5: addObservation,
            6: ReportStaff,
            7: ReportAnimal,
            8: feedingDetails,
            9: ReportFood,
            15: exit
        }
        options.get(int(choice), "I don't understand your choice")()


main()
