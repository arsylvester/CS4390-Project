#theThreeFunctions.py: These are all of the commands that the server uses to interact with the database.

# deta is sotred (Name, Quantity, Date). 
#Date is stored year-month-day
#               xxxx-xx-xx
with open ('Database.txt') as load_file:
    DATABASE = [tuple(line.split()) for line in load_file]


# sorts the list and prints. choice = which sort method will be used 
# choice = 0 = Random | choice = 1 = Sort by qty | choice = 2 = sort by date
def returnOrder(choice):
# If choice = 0 it will print the list in random order 
    if choice == 0:
        DATABASE.sort(key=lambda row: row[0])

        f = open("Database.txt", "w")
        for t in DATABASE:
            line = ' '.join(str(x) for x in t)
            f.write(line + '\n')
        f.close()

# If choice = 1 it will print the list in qty order
    elif choice == 1:
        DATABASE.sort(key=lambda row: int(row[1]))

        f = open("Database.txt", "w")
        for t in DATABASE:
            line = ' '.join(str(x) for x in t)
            f.write(line + '\n')
        f.close()

# If choice = 2 it will print the list in date order
    elif choice == 2:
        DATABASE.sort(key=lambda row: row[2])

        f = open("Database.txt", "w")
        for t in DATABASE:
            line = ' '.join(str(x) for x in t)
            f.write(line + '\n')
        f.close()
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

    f = open("Database.txt", "w")
    for t in DATABASE:
        line = ' '.join(str(x) for x in t)
        f.write(line + '\n')
    f.close()

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

    f = open("Database.txt", "w")
    for t in DATABASE:
        line = ' '.join(str(x) for x in t)
        f.write(line + '\n')
    f.close()

    if index2 == -1:
        return False
    else:
        tempList = list(DATABASE[index2])
        tempList[1] = qty
        DATABASE[index2] = tuple(tempList)
        return True

