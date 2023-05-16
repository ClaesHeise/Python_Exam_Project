import pandas as pd
from FirmClass import Firm


# Læser en .csv fil og omdanner den til en Pandas dataframe
firms_df = pd.read_csv('firms.csv')

# En function til at finde den mindste værdi af den liste (af priser) der bliver givet
def calc_min(x):
    l = [float(y.strip(' []')) for y in x.split(',')]
    return min(l)

# En function til at finde den største værdi af den liste (af priser) der bliver givet
def calc_max(x):
    l = [float(y.strip(' []')) for y in x.split(',')]
    return max(l)

# Laver dataframe om til en liste af FirmClass, som returneres
def df_to_firms():
    output = []
    for index in range(firms_df["Name"].size):
        l = [float(y.strip(' []')) for y in firms_df["Prices"][index].split(',')]
        output.append(Firm(firms_df["Name"][index], l))
    return output

# Finder det firma, med den laveste pris i procent, i forhold til dens forrige priser og returnerer det object (FirmClass)
def cheapest_firm_percentage():
    firms = df_to_firms()
    cheapest_firm = firms[0]
    for firm in firms:
        if firm.get_avg_price() < cheapest_firm.get_avg_price():
            cheapest_firm = firm
    return cheapest_firm

# Finder den mindste pris, for hvert firma, og returnerer en liste af tupler med hvert firma navn og pris som String
def get_all_min():
    output = []
    min_val = firms_df["Prices"].apply(calc_min)
    for index in range(min_val.size):
        output.append((firms_df["Name"][index], min_val[index]))
    return output

# Samme som overstående, bare for de højeste priser
def get_all_max():
    output = []
    max_val = firms_df["Prices"].apply(calc_max)
    for index in range(max_val.size):
        output.append((firms_df["Name"][index], max_val[index]))
    return output

# Returnere det firma, som har haft den billigste pris, generelt set, som en tuple
def get_cheapest_firm():
    min_list = get_all_min()
    i_min = min_list[0]
    for tuple in min_list:
        if tuple[1] < i_min[1]:
            i_min = tuple
    return i_min

# Samme som overstående, bare med den dyreste pris
def get_most_expensive_firm():
    max_list = get_all_max()
    i_max = max_list[0]
    for tuple in max_list:
        if tuple[1] > i_max[1]:
            i_max = tuple
    return i_max

## Prints
# printer det billigste firma i procent
print("Cheapest firm in percentage")
cheapest = cheapest_firm_percentage()
print(cheapest)
print("Percentage: ",cheapest.get_avg_price(),"%")
print()

# printer alle firmaer og deres billigste priser
print("All firms cheapest prices")
cheap_list = get_all_min()
for tuple in cheap_list:
    print(tuple)
print()

# printer alle firmaer og deres dyreste priser
print("All firms most expensive prices")
expensive_list = get_all_max()
for tuple in expensive_list:
    print(tuple)
print()

# printer den billigste firmas billigste pris
print("The cheapest price of all firms")
print(get_cheapest_firm())
print()

# printer den dyreste firmas dyreste pris
print("The most expensive price of all firms")
print(get_most_expensive_firm())