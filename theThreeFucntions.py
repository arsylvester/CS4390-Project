# deta is sotred (Name, Quantity, Date). 
#Date is stored year-month-day
#               xxxx-xx-xx
DATABASE = [
            ('Milk', 10, "2013-02-07"),
            ('Butter', 5, "2021-04-20"),
            ('Cheese', 20, "2020-10-10"),
            ('Tuna', 1, "2010-04-10"),
            ('Sugar', 40, "2021-05-10"),
            ('Beer', 5, "2021-07-04"),
            ('Wine', 50, "2008-12-30"),
            ('Yogurt', 20, "2005-12-15"),
            ('Oil', 1, "2011-10-04"),
            ('Rice', 21, "2018-05-28"),
            ('Water', 10, "2000-01-01"),
            ('Beans', 0, "2001-05-05"),
            ('Onions', 17, "2011-10-30"),
            ('Honey', 6, "2005-08-21"),
            ('Toothpaste', 120, "2009-11-06"),
            ('Salt', 12, "2003-12-30"),
            ('Nuts', 1000, "1990-05-21")
        ]


# Prints the list specified by user 
def returnOrder(choice):
# If choice = 0 it will print the list in random order 
    if choice == 0:
        for d in DATABASE:
            print("{:10s} {:5} {:10}".format(*d))

# If choice = 1 it will print the list in qty order
    elif choice == 1:
        DATABASE.sort(key=lambda row: row[1])
        print("Data is sorted by QTY")
        for d in DATABASE:
            print("{:10s} {:5} {:10}".format(*d))

# If choice = 2 it will print the list in date order
    elif choice == 2:
        DATABASE.sort(key=lambda row: row[2])
        print("This is ordered by date")
        for d in DATABASE:
            print("{:10s} {:5} {:10}".format(*d))
    else:
        print("Error printing order...")
        


# Pass list and size it will remove that row.
# If name is in list return True
# If name is not in list returns False
def deleteFromList(name, size):
    index = 0
    index2 = -1

    while index < size:
        if DATABASE[index][0] == name:
            index2 = index
        index += 1

    if index2 == -1:
        return False
    else:
        DATABASE.pop(index2)
        return True



# Pass list, size, and new qty amount 
# If name is in list return True
# If name is not in list returns False
def updateQuantity(name, size, qty):
    index = 0
    index2 = -1

    while index < size:
        if DATABASE[index][0] == name:
            index2 = index
        index += 1

    if index == -1:
        return False
    else:
        tempList = list(DATABASE[index2])
        tempList[1] = qty
        DATABASE[index2] = tuple(tempList)
        return True





# This is a lil test. will not stay
# Each fucntion have been tested!
sizeOfList = len(DATABASE)
didItWork = updateQuantity("Milk", sizeOfList, 10000)

if didItWork == True:
    returnOrder(2)

elif didItWork == False:
    Print("Item not in list")





    
    
