from ShopListClassRDBI import ShopListRDBI

#function to create the shopping list/cart and store information inside of a list
def shopping_cartRDBI():
    shoppingList = [] #creating an empty list for the food that will store the foods to be purchased later
    numItem = 0 #creating a variable to be used in a loop

    #Loop to ask customer for products they will order
    while numItem <= 0:
        numItem = int(input("How many different products will you order? "))
        if numItem <= 0:
            print("You must choose at least 1 product")

    for k in range(numItem):
        print(f"Item {k+1}:")
        print()
    
        name = str(input("What is the name of the food you would like to purchase?: ")) #obtaining food name

    
        amount = 0
        #This loop is obtain the amount(in pounds) of a food product that a user wants
        while amount <= 0:
           amount = float(input(f"How many pounds of {name} do you want?: "))
           print()
           if amount <= 0:
               print("You must enter a number of pounds greater than 0.")
               print() #spacing4

        shoppingList.append(ShopListRDBI(name, amount)) #adds information to the list

    return shoppingList

#function to display a list of information of the order
def orderinfoRDBI(Foods):
    print("Order Information:")
    print()

    for ShopListRDBI in Foods: #for loop to go through all ordered items and the associated information
        print("Item: " + str(ShopListRDBI.getNameRDBI()))
        print("Amount Ordered(in pounds): " + str(ShopListRDBI.getAmountRDBI()))
        print("Price per pound: $" + str(ShopListRDBI.getPriceRDBI()))
        print("Price of order: " + str(ShopListRDBI.getTotalRDBI()))
        print()
    # print() is used to create spacing between the text

def pricetotalRDBI(Foods): #calculates the total cost from ALL the orders together
    total = 0
    for orders in Foods: #For loop that loops equal to the number of orders there are
        total = orders.getTotalRDBI() + total #calculates total of a specific order and adds it to the grand total
        
    roundTotal = format( total, ",.2f") #rounds total to 2 decimal places
    print(f"Total cost: ${roundTotal}") #displays the total cost of every order together

def main(): #function to call all other functions
    Foods = shopping_cartRDBI() #a variable to be used in the 2 functions called below
    orderinfoRDBI(Foods) #Displays the info of the orders made
    pricetotalRDBI(Foods) #displays the total price

print("Available products: Dry Cured Iberian Ham, Wagyu Steaks, Matsutake Mushrooms, Kopi Luwak Coffee, Moose Cheese, White Truffles, Blue Fin Tuna, Le Bonnotte Potatoes")
print("To properly input orders, do not misspell the word. Also keep in mind that it is case sensitive.") #info for proper use
main() #calls main, which runs the main function.
