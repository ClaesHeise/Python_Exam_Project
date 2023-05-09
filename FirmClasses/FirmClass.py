class Firm():

    def __init__(self, name, prices=[]):
        self.name = name
        self.prices = prices 
        
    # def __repr__(self):
    #     return 'Firm(%r, %r, %r, %r)' % (self.name, self.gender, self.data_sheet, self.image_url)
    
    def __str__(self):
        return self.toString()
        # priceString = "[\n"
        # for p in self.prices:
        #     priceString = priceString + " " + p.toString() + "\n"
        # priceString = priceString + "]"
        # return 'Name: {name},\nPrices: {prices}'.format(
        #     name=self.name, prices=priceString)
    
    def toString(self):
        priceString = "[\n"
        for p in self.prices:
            priceString = priceString + " " + str(p) + "\n"
        priceString = priceString + "]"
        return 'Name: {name},\nPrices: {prices}'.format(
            name=self.name, prices=priceString)
    
    def get_avg_price(self):
        prices = self.prices
        sum_of_prices = sum(prices)
        avg_price = sum_of_prices / len(prices)
        latest_price = prices[-1]
        return latest_price / avg_price * 100
    
    # def percentDone(self):
    #     totalEcts = []
    #     for cour in self.data_sheet.courses:
    #         totalEcts.append(cour.ects)
    #     return sum(totalEcts) / 1.5