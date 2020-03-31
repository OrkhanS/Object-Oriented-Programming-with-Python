from Staff_room import Staff_room
from animal_feeding import Animal_feeding
from food import Food
from animal import Animal
from observation import Observation
import random


def addStaff():
    newStaff = Staff_room()
    newStaff.set_staff('Rasul', 'Aliyev', 'A-164', 9023)
    
def animalFeed():
    newAnimal = Animal_feeding()
    # here ask which food 
    isFed = newAnimal.feed(3338, 'Pigplus','RHM', 800, 'Rasul Aliyev')
    if(isFed == True):
        print("Fed successfully :)")
    else:
        print("Uh-oh, you can only feed this animal twice :(")

def ReportStaff():
    f = open("staff.txt", "r")
    contents = f.read()
    print("Details of Staff")
    print(contents)
    fileName = str(random.random())
    f = open(fileName, "a+")
    f.write(contents)

def ReportAnimal():
    f = open("feeding.txt", "r")
    contents = f.read()
    print("Details of Animal")
    print(contents)
    # fileName = str(random.random())
    # f = open(fileName, "a+")
    # f.write(contents)

def addFood():
    # ask what is name and manufacturer
    newFood = Food()
    newFood.set_food('NewFORDOG', 'Company-123')

def feedingDetails():
    # ask for animal id
    details = Animal_feeding()
    details.feedingDetails(1234)

def foodDetails():
    detailsFood = Food()
    detailsFood.foodforGivenAnimal(14)


def addAnimal():
    newAnimal = Animal()
    newAnimal.set_animal("M", "25/06/2016", "Black", "63", "10","22", "11")
    # ask if would like to add environmental conditions

def addObservation():
    newObservation = Observation()
    newObservation.set_observation(1234, '25/06/2016', '10:33', 22, 11, "SALAM", "RASUL ALIYEV")

def ReportObservation():
    f = open("observation.txt", "r")
    contents = f.read()
    print("Details of Animal Observation")
    print(contents)
    
def observationDetails():
    observationDetails = Observation()
    observationDetails.details(22)

def staffWhoObserved():
    observationDetails = Observation()
    observationDetails.staffWhoObserved(1234)

# addStaff()
# ReportStaff()
# animalFeed()
# ReportAnimal()
# addFood()
# feedingDetails()
# foodDetails()
# addAnimal()
addObservation()
# ReportObservation()
# observationDetails()
staffWhoObserved()