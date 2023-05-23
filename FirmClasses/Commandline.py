import csv
import platform
from FirmClass import Firm
from AllFirmsClass import AllFirms
import pandas as pd
import csv
firm1 = Firm("Microsoft", [0.2, 0.15, 0.32])
firm2 = Firm("Apple", [0.03, 0.3, 100])
firm3 = Firm("Steam", [0.2, 0.05, 0.01])
firmList = []
##firmList.append(firm1)
##firmList.append(firm2)
##firmList.append(firm3)
with open('FirmClasses/firms.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        line_count += 1
        firm1 = Firm(row[0],row[1])
        firmList.append(firm1)
    print(f'Processed {line_count} lines.')
def selectFirm(firmList):
    print("Please select a name from the list:")
    for i, Firm in enumerate(firmList):
        print(f"{i+1}. {firmList[i].name}")
    selected_index = int(input("Enter the number corresponding to your selection: ")) - 1

    selected_Firm = firmList[selected_index]
    print(f"You selected:")
    print(f"{selected_Firm.name}")
    print("what would you like to see?")
    print("1. the current price compared to the average price in procentage")
    print("2. all the prices the company has had")
    print("3. the companies name")
    print("4. quit the program")
    i = 0
    while i != 1:
        selected_index = int(input())
        if selected_index == 1:
            print(f"{selected_Firm.get_avg_price()}%")
        elif selected_index == 2:
            print(f"{selected_Firm}")
        elif selected_index == 3:
            print(f"{selected_Firm.name}")
        elif selected_index == 4:
            i=1



selectFirm(firmList)