#class definition
class ShopListRDBI:
    #initializer method - set up an object
    #self parameter - allows the interpeter to know which 
    #object it is working with
    def __init__(self, name, amount):
        #creates and initializes instance variables/attributes
        #private variables come with double underscore before them
        self.__name = name
        self.__amount = float(amount)
        self.__price = self.__setPrice_listRDBI()
        self.__total_price = self.setCalc_totalRDBI() 

    #mutator methods - aka setter allow you to update attributes
    def __setPrice_listRDBI(self): 
        #This mutator method is used to get the price of food(per pound) that will be purchased
        #double underscore before the name of the function makes it private
           if self.__name == "Dry Cured Iberian Ham":
               return 177.80
           elif self.__name == "Wagyu Steaks":
               return 450.00
           elif self.__name == "Matsutake Mushrooms":
               return 272.00
           elif self.__name == "Kopi Luwak Coffee":
               return 306.50
           elif self.__name == "Moose Cheese":
               return 487.20
           elif self.__name == "White Truffles":
               return 3600
           elif self.__name == "Blue Fin Tuna":
               return 3603.00
           elif self.__name == "Le Bonnotte Potatoes":
               return 270.81
           else:
               return 0
    
    def setCalc_totalRDBI(self): 
        #This mutator method simply calculates the price that will be paid based on how many
        #pounds a person wants to purchase by multiplying price(per pound) with amount(in pounds)
        return (self.__amount * self.__price)

    #accessor methods - aka getter allows you to retrieve data
    #In order from top to bottom accessor for food name, amount of food(in pounds),
    #price associated with a food name, and Total price
    def getNameRDBI(self):
        return self.__name

    def getAmountRDBI(self):
        return self.__amount

    def getPriceRDBI(self):
        return self.__price

    def getTotalRDBI(self):
        return self.__total_price

