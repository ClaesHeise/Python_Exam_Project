import csv
import platform


class AllFirms():
    def __init__(self, firms=None):
        if firms is None:
            firms = []
        self.firms = firms
        
    # def __repr__(self):
    #     return 'Student(%r, %r, %r, %r)' % (self.name, self.gender, self.data_sheet, self.image_url)

    def __str__(self):
        firmsString = "[\n"
        for f in self.firms:
            firmsString = firmsString + "  " + f.toString() + "\n"
        firmsString = firmsString + "]"
        return 'Firms: {firms}'.format(
            firms=firmsString)
    
    def firms_to_csv(self):
        if platform.system() == 'Windows':
            newline = ''
        else:
            newline = None
        print("Hello2")
        with open("firms.csv", 'w', newline=newline) as of:
            return_file = csv.writer(of)
            
            return_file.writerow(["Name","Prices"])
            for element in self.firms:

                return_file.writerow([str(element.name), [price for price in element.prices]])