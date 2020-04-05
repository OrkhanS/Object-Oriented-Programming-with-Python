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
from prettytable import PrettyTable
import pickle
import sys

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
    # try:
    print("\nDetails of Staff\n")
    allContents = appliaction.getAllStaff()
    print("\n")
    t = PrettyTable(['StaffID', 'Name', 'Surname', 'Office', 'Tel'])
    for staffContent in allContents:
        t.add_row([str(staffContent.staff_id), str(staffContent.first_name), str(staffContent.last_name), str(staffContent.office), str(staffContent.tel)])
    print(t)
    fileName = "StaffDetails " + str(random.random())
    f = open(fileName, "a+")
    for contents in allContents:
        f.write(str(contents.staff_id)+" "+str(contents.first_name)+" "+str(contents.last_name)+" "+str(contents.office)+" "+str(contents.tel)+"\n")
    f.close()
    # except:
    #     print("\nSome Error occured, try again.\n")
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
    # try:
    print("\nDetails of Foods\n")
    allContents = appliaction.getAllFood()
    print("\n")
    t = PrettyTable(['Food Name', 'Manufacturer', 'Weight'])
    for foodContent in allContents:
        t.add_row([str(foodContent.name), str(foodContent.manufacturer), str(foodContent.weight)])
    print(t)
    fileName = "FoodDetails " + str(random.random())
    f = open(fileName, "a+")
    for contents in allContents:
        #data = {"name": contents.name, "manufacturer": contents.manufacturer, "weight": contents.weight} 
        f.write(str(contents.name)+" "+str(contents.manufacturer)+" "+str(contents.weight)+"\n")
    f.close()
    # except:
    #     print("\nSome Error occured, try again.\n")
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
                    if animalNo not in animal.animalNo:
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
    # try:
    print("\nDetails of Animals\n")
    allContents = appliaction.getAllAnimal()
    print("\n")
    t = PrettyTable(['AnimalNo', 'Gender', 'Birth', 'Color', 'Relative Humidity', 'Enclosure Size (m2)', 'Temperature', 'Hours of light per day'])
    for animalContent in allContents:
        t.add_row([str(animalContent.animalNo),str(animalContent.gender),str(animalContent.birth),str(animalContent.color),str(animalContent.humidity),str(animalContent.size),str(animalContent.temperature),str(animalContent.hours_of_light)])
    print(t)
    fileName = "AnimalDetails " + str(random.random())
    f = open(fileName, "a+")
    for contents in allContents:
        #data = {"name": contents.name, "manufacturer": contents.manufacturer, "weight": contents.weight} 
        f.write(str(contents.animalNo)+" "+str(contents.gender)+" "+str(contents.birth)+" "+str(contents.color)+" "+str(contents.humidity)+" "+str(contents.size)+" "+str(contents.temperature)+" "+str(contents.hours_of_light)+"\n")
    f.close()
    # except:
    #     print("\nSome Error occured, try again.\n")
    main()
   
# _____________________________________________________ANIMAL FEEDING________________________________________________________


def animalFeed():
    try:
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
            count = 0
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
            
    except:
        print("\nSome Error occured, try again.\n")
    main()

def feedingDetails():
    #try:
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
        startDate = input("Start Date (12/08/2020):  ")
        endDate = input("End Date (12/08/2020): ")
        print("\n")
        t = PrettyTable(['AnimalNo', 'Date', 'Time', 'Food Name', 'Manufacturer', 'Weight (gr) ', 'Staff'])
        fileName = "FeedingDetails " + str(random.random())
        f = open(fileName, "a+")
        for feed in feeding:
            feedDate = parse(feed.date)
            start = parse(startDate)
            end = parse(endDate)
            if feedDate >= start and feedDate <= end:
                t.add_row([str(feed.animal.animalNo), str(feed.date), str(feed.time), str(feed.food.name), str(feed.food.manufacturer), str(feed.food.weight), str(feed.staff.first_name) + " " +str(feed.staff.last_name)])
                #data = {"animalNo": feed.animal, "date": feed.date, "time": feed.time, "food": feed.food, "staff": feed.staff} 
                f.write(str(feed.animal.animalNo)+" "+str(feed.date)+" "+str(feed.time)+" "+str(feed.food.name)+" "+str(feed.staff.first_name)+" "+str(feed.staff.last_name)+"\n")
        f.close()
        print(t)
    
    # except:
    #     print("\nSome Error occured, try again.\n")
    main()

# _____________________________________________________Observation________________________________________________________


def addObservation():
    # try:
    print("Please type details of Observation\n")
    animalNo = input("AnimalNo: ")
    staffID = input("StaffId: ")
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

    if flagStaff == 0 and flagAnimal == 0:
        weight = input("Animal Weight (kg): ")
        temperature = input("Temperature (C*): ")
        note = input("Note: ")
        newObservation = Observation()
        newObservation.set_observation(animal, weight, temperature, note, staff)
        appliaction.addObservationingToList(newObservation)
        print("\nAn observation record added successfully\n")
        print("\nPlease, keep in mind that an animal should be observed more than three times in a day.\n")
    # except:
    #     print("\nSome Error occured, try again.\n")
    main()

def ReportObservation():
    # try:
    print("Please type Following details: \n")
    animalnum = input("AnimalNo: ")
    animals = appliaction.getAllAnimal()
    observation = appliaction.getAllObservationDetails()
    flagAnimal = 1
    for observed in observation:
        if animalnum == observed.animal.animalNo:
            flagAnimal = 0
    if flagAnimal == 1:
        print("\nThere is no such animal or this animal hasn't been observed before, try again!!")
    else:
        startDate = input("Start Date (12/08/2020):  ")
        endDate = input("End Date (12/08/2020): ")
        print("\n")
        t = PrettyTable(['AnimalNo', 'Date', 'Time', 'Weight', 'Temperature', 'Note', 'Staff'])
        fileName = "ObservationDetails " + str(random.random())
        f = open(fileName, "a+")
        for observed in observation:
            observedDate = parse(observed.date)
            start = parse(startDate)
            end = parse(endDate)
            if observedDate >= start and observedDate <= end:
                t.add_row([str(observed.animal.animalNo), str(observed.date), str(observed.time), str(observed.weight), str(observed.temperature), str(observed.note), str(observed.staff.first_name) + " " +str(observed.staff.last_name)])
                data = {"animal": observed.animal, "date": observed.date, "time": observed.time, "weight": observed.weight, "temperature": observed.temperature, "note":observed.note, "staff":observed.staff} 
                f.write(str(observed.animal.animalNo)+" "+str(observed.date)+" "+str(observed.time)+" "+str(observed.weight)+" "+str(observed.temperature)+" "+str(observed.note)+" "+str(observed.staff.first_name)+" "+str(observed.staff.first_name)+"\n")
                f.close()
        print(t)
    # except:
    #     print("\nSome Error occured, try again.\n")
    main()

def staffWhoObserved():
    # try:
    print("Please type Following details: \n")
    animalnum = input("AnimalNo: ")
    animals = appliaction.getAllAnimal()
    observation = appliaction.getAllObservationDetails()
    flagAnimal = 1
    for observed in observation:
        if animalnum == observed.animal.animalNo:
            flagAnimal = 0
    if flagAnimal == 1:
        print("\nThere is no such animal or this animal hasn't been observed before, try again!!")
    else:
        print("\n")
        t = PrettyTable(['StaffID', 'First name', 'Last name', 'Office', 'Tel'])
        fileName = "StaffWhoObservedDetails " + str(random.random())
        f = open(fileName, "a+")
        for observed in observation:
            t.add_row([str(observed.staff.staff_id), str(observed.staff.first_name), str(observed.staff.last_name), str(observed.staff.office), str(observed.staff.tel)])
            #data = {"staff_Id": observed.staff.staff_id, "first_name": observed.staff.first_name, "last_name": observed.staff.last_name, "office": observed.staff.office, "tel": observed.staff.tel} 
            f.write(str(observed.staff.staff_id)+" "+str(observed.staff.first_name)+" "+str(observed.staff.last_name)+" "+str(observed.staff.office)+" "+str(observed.staff.tel)+"\n")
        f.close()
        print(t)
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
    for observed in feeding:
        if animalnum == observed.animal.animalNo:
            flagAnimal = 0
    if flagAnimal == 1:
        print("\nThere is no such animal or this animal hasn't been fed before, try again!!")
    else:
        print("\n")
        t = PrettyTable(['Food name', 'Manufacturer'])
        fileName = "FoodGivenDetails " + str(random.random())
        f = open(fileName, "a+")
        for fed in feeding:
            t.add_row([str(fed.food.name), str(fed.food.manufacturer)])
            #data = {"foodName": fed.food.name, "manufacturer": fed.food.manufacturer} 
            f.write(str(fed.food.name)+" "+str(fed.food.manufacturer)+"\n")
        f.close()
        print(t)
    # except:
    #     print("\nSome Error occured, try again.\n")
    main()

def defualtPrint():
    print("\nI don't understand your choice\n")

def exitNow():
    dataList = []
    dataList.append(appliaction.getAllStaff())
    dataList.append(appliaction.getAllAnimal())
    dataList.append(appliaction.getAllFood())
    dataList.append(appliaction.getAllFeedingDetails())
    dataList.append(appliaction.getAllObservationDetails())

    with open("app.txt", "wb") as f:
        pickle.dump(dataList, f, pickle.HIGHEST_PROTOCOL)
        f.close()
    return

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        with open("app.txt", "rb") as f:
            try:
                data1 = pickle.load(f)
                for data in data1[0]:
                    appliaction.addStaffToList(data)    
                for data in data1[1]:
                    appliaction.addAnimalToList(data)
                for data in data1[2]:
                    appliaction.addFoodToList(data)
                for data in data1[3]:
                    appliaction.addFeedingToList(data)
                for data in data1[4]:
                    appliaction.addObservationingToList(data)
                sys.argv = []
            except:
                print("\nThere is no data in the text file")            

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
        print("Choose 8 for Details of Foods")
        print("Choose 9 for Details of Feeding")
        print("Choose 10 for Details of Observation")
        print("Choose 11 for Details of Staff who have observed")
        print("Choose 12 for Details of Foods that have been fed")
        print("Choose 13 to exit")

        choice = input("Please make a choice: ")

        options = {
            1: addStaff,
            2: addAnimal,
            3: addFood,
            4: animalFeed,
            5: addObservation,
            6: ReportStaff,
            7: ReportAnimal,
            8: ReportFood,
            9: feedingDetails,
            10: ReportObservation,
            11: staffWhoObserved,
            12: foodsGiven,
            13: exitNow,
            14: defualtPrint
        }
        options.get(int(choice), 14)()


main()
