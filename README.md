# Object-Oriented-Programming-with-Python
The research institute is responsible for researching and developing methods for animals. It keeps animals in controlled environments and monitors their progress under controlled feeding. You can find some examples of existing manual records of the research institute. You are expected to develop an application to effectively keep track of these details and provide necessary reports

# Animal Research Institute

This is Assignment 1 of Software Development course. 


## To run

Download the files first, open CMD and write following code:

```bash
pip install prettytable
python main.py
```

To see the Reports:

```bash
python main.py <filename>.txt
```


## Details
This Assignment is for:

```bash
1. Practicing Object Oriented programming in Python and maintaining different types of objects
2. Practicing class hierarchy and the relevant design 
   and implementation decisions
3. Practicing with FILES in python
4. Practicing and using abstract classes, and interfaces
```

## Requirements
The application should be able to add a new staff, a new food, a new animal along with the
environment conditions, a report of animal feeding and a report of animal observation.
The application should ensure that each staff has a unique ID with 6 digits. The telephone
number should consist of 4 digits and the office number should be in following format where
X represents a digit: A-XXX.
The application should also ensure that each animal has a unique ID with 4 digits. An animal
should not be fed more than two times in a day and should be observed more than three times
in a day

The application should be able to produce the following reports. Each report should be printed
both on a screen and also exported as txt file.
a. Details of all staff (Staff ID, First name, Last name, Office, Tel)
b. Feeding details of a given animal between specified dates (Date, Time, Food name,
Manufacturer, Weight, Staff)
c. Observation details of a given animal between specified dates (Date, Time, Animal
Weight, Temperature, Note, Staff)
d. Staff who have observed a given animal (Staff ID, First name, Last name, Office, Tel)
e. Foods that have been fed to a given animal (Food name, Manufacturer)


![alt text](https://github.com/OrkhanS/Object-Oriented-Programming-with-Python/blob/master/Capture1.JPG)

## License
[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/DAVFoundation/captain-n3m0/blob/master/LICENSE)
