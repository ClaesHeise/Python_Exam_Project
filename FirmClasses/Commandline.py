import csv
import platform
from FirmClass import Firm
from AllFirmsClass import AllFirms
import pandas as pd
import TestProgram
import PandaOp
import csv
firm1 = Firm("Microsoft", [0.2, 0.15, 0.32])
firm2 = Firm("Apple", [0.03, 0.3, 100])
firm3 = Firm("Steam", [0.2, 0.05, 0.01])
firmList = []

firmList = TestProgram.firms_from_csv()

def selectFirm(firmList):
    j = 0
    while(j!=1):
        print("Please write what you want shown:")
        print("'quit': ends this application")
        print("'lowest': Show the company with the lowest average cost")
        print("'highest': Show the company with the highest average cost")
        print("'lowestp': Show the company with the lowest average cost in procentage")
        print("'allmin': show all minimum prices")
        print("'allmax': show all maximum prices")

        for i, Firm in enumerate(firmList):
            print(f"{i+1}. {firmList[i].name}")
        selected_index = str(input("Enter the number corresponding to your selection: "))
        isNumber = True
        try:
            int(selected_index)
        except ValueError:
            isNumber = False
        if(isNumber == True):
            showAllFirms(selected_index)
        else:
          j = nonDirectChoice(selected_index)

def showAllFirms(selected_index):
    selected_index = int(selected_index)-1
    selected_Firm = firmList[selected_index]
    print(f"You selected:")
    print(f"{selected_Firm.name}")
    print("what would you like to see?")
    print("1. the current price compared to the average price in procentage")
    print("2. all the prices the company has had")
    print("3. the companies name")
    print("4. quit the program")
    print("5. get the company with the average lowest price")
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
        elif selected_index == 5:
            PandaOp.dataframe_from_list(selected_index)

def nonDirectChoice(selected_index):
    if selected_index == "lowestp":
        print(PandaOp.cheapest_firm_percentage())
    elif selected_index == "allmin":
        print(PandaOp.get_all_min)
    elif selected_index == "allmax":
        print(PandaOp.get_all_max)
    elif selected_index == "lowest":
        print(PandaOp.get_cheapest_firm())
    elif selected_index == "highest":
        print(PandaOp.get_most_expensive_firm())
    elif selected_index == "quit":
        return 1
        
selectFirm(firmList)