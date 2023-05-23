import csv
import platform
from FirmClass import Firm
from AllFirmsClass import AllFirms

# firm1 = Firm("Microsoft", [0.2, 0.15, 0.32])
# firm2 = Firm("Apple", [0.03, 0.3, 100])
# firm3 = Firm("Steam", [0.2, 0.05, 0.01])

# firmList = []
# firmList.append(firm1)
# firmList.append(firm2)
# firmList.append(firm3)

# firms = AllFirms(firmList)


def firms_to_csv(lst):
    if platform.system() == 'Windows':
        newline = ''
    else:
        newline = None
    with open("firms.csv", 'w', newline=newline) as of:
        return_file = csv.writer(of)
        
        return_file.writerow(["Name","Prices"])
        for element in lst:
            return_file.writerow([str(element.name), [price for price in element.prices]])

def firms_from_csv():
    list_of_firms = []
    char_removal = ["[", "]", " "]
    with open("firms.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        lst = [rows for rows in csv_reader]
    for element in lst:
        # Make the prices, into a list of strings
        priceList = element[1].split(",")

        # Remove unnecesary chars
        for i in range(len(priceList)):
            for char in char_removal:
                priceList[i] = priceList[i].replace(char, "")

        # Convert to floats, for the object class
        for i in range(len(priceList)):
            priceList[i] = float(priceList[i])
        list_of_firms.append(Firm(element[0], priceList))
    return list_of_firms

# firms.firms[0].name = "Micro"
# firms_to_csv(firms.firms)
# firms = AllFirms(firms_from_csv())
# print("Latest price, compared to average price trend in percentage:")
# for f in firms.firms:
#     print(f.name + ": " + str(f.get_avg_price()) + " %")
# print(firms.firms)


# firms.firms_to_csv