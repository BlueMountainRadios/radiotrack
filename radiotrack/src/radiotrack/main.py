"""
Programmer: BlueMountainRadios
Date: 10/09/2026
Version: 1
"""

from models import RadioStatus, Manufacturer, RadioAccessoryType, RadioAccessory, Radio
from repository import Repository
import sys


def add_radio_status():
    radio_status_name = input("Radio Status Name: ")
    radio_status_meaning = input("Meaning of status: ")
    rs = RadioStatus(radio_status.generate_id(), radio_status_name, radio_status_meaning)
    radio_status.add(rs)
    print(f"Added in {rs.status}, {rs.id}.")

run = False

print("Welcome to RadioTrack..")

print("Creating Radio Repositories...")

radio_status = Repository[RadioStatus]()
manufactuer = Repository[Manufacturer]()
radio_accessory_type = Repository[RadioAccessoryType]()
radio_accessory = Repository[RadioAccessory]()
radios = Repository[Radio]()

print("Repositories have been created...")

run = True

while(run):
    
    print("What would you like to do?")
    print("1: Add Radio Status\n2: Add Manufactuer\n3: Add Radio Accessory Type\n4: Add Radio Accessory\n5: Add a Radio\n6: Exit Application")
    response = input()
    
    match int(response):
        case 1: 
            add_radio_status()
        case 2:
            print("Adding Manufactuer")
        case 3:
            print("Add Radion Accessory")
        case 4:
            print("Add Radio Accessory")
        case 5:
            print("Add Radio")
        case 6:
            print("Exiiting Application")
            sys.exit(0)


    
            

      

