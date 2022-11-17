#-------------------------------------#
#Title: Loading List Data from a File
# Dev: BLampman
# Date: 11/15/2022
# Change Log: Created Script 11/15/22
#------------------------------------#

#Declare my variables
objFileName = "ToDoFile.txt"  #An object that represents a file
#strData = "" #a row of text data from the file
#dicrow = {} #A row of data separeated into elements of a dictionary
lstTable = [] #A dictionary that acts as a table of rows
#strMenu = "" #A menu of user options
#strChoice = "" #Capture the user option selection
strFile =  "ToDoFile.txt"

#Process the Data
objFile = open(objFileName, "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow= {"Task":lstRow[0].strip(),"Priority":lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()
    #print(lstTable)
    #print(lstRow[0]+'|')

#input/output
#Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save data to file
    5) Exit program""")
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print() #Add extra line for looks

# Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        continue  # to show the menu

# Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        strTask = str(input("What is the task? - ")).strip()
        strPriority = str(input("What is the priority? [high|low] - ")).strip()
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print("Current Data in table:")
        # for dicRow in lstTable:
        #     print(dicRow)

#Step 4a - Show the current items in the table
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        continue  # to show the menu

# Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        #Step 5a - Allow user to indicate which row to delete
        strKeyToRemove = input("Which TASK would you like removed? - ")
        blnItemRemoved = False  # Creating a boolean Flag
        intRowNumber = 0
        for row in lstTable:
            task, priority = dict(row).values()
            if task == strKeyToRemove:
                del lstTable[intRowNumber]
                blnItemRemoved = True
            intRowNumber += 1
            #end if
        # end for loop
        #Step 5b - Update user on the status
        if(blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")
        #Step 5c - Show the current items in the table
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        continue  # to show the menu

# Step 6 - Save tasks to the ToDoFile.txt file
    elif(strChoice == '4'):
        #Step 5a - Show the current items in the table
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")

#Step 5b - Ask if they want save that data
        if("y" == (input("Save this data to file? (y/n) - ")).strip().lower()):
            objFile = open(objFileName, "w")
            for dicRow in lstTable:
             objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            objFile.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
                input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue  # to show the menu

    elif (strChoice == '5'):
        break   # and Exit the program
