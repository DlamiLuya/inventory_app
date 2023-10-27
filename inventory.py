from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    # A constructor that will define the class object with the following attributes.
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity 
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''

    # Define a class function that will return the cost attribute of the given object.    
    def get_cost(self):
        return self.cost
        '''
        Add the code to return the cost of the shoe in this method.
        '''
    
    # Define a class function that will return the quantity attribute of a given object.
    def get_quantity(self): 
        return self.quantity
        '''
        Add the code to return the quantity of the shoes.
        '''

    # Define a special function that will return the string representation of the class.
    def __str__(self):
        return f'{self.country},{self.code},{self.product},{self.cost},{self.quantity}'
        '''
        Add a code to returns a string representation of a class.
        '''

    # Define a special function that will give the objects of the class the ability to use indexing.
    # This will allow for the retrieval of object attributes without having to specify the attribute, but rather specifying the attribute as an index of the object.
    def __getitem__(self, i):
        if i == 0:
            return self.country
        elif i == 1:
            return self.code
        elif i == 2:
            return self.product
        elif i == 3:
            return self.cost
        elif i == 4:
            return self.quantity
        

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
# Define a list variable that will store the contents of the inventory.txt file in a list
# The first line variable stores the first line of the inventory.txt file, this will be used for output purpose.
shoe_list = []
first_line = "Country,Code,Product,Cost,Quantity"
#==========Functions outside the class==============
# Define a function that will read through the inventory.txt file and store all the data into the shoe_list variable.
def read_shoes_data():
    try: # The use of try/except statements will make sure that if the file is not found, an appropriate message will be printed.
        inventory = open("inventory.txt", 'r')
    except FileNotFoundError:
        print("File not found")
        exit()

    # These statements read through the txt file and stores each line in the shoe_list variable
    inventory_contents = inventory.read()
    line_inventory_contents = inventory_contents.split('\n')
    line_inventory_contents.pop(0) # pops out the first line in the txt file
    for line in range(len(line_inventory_contents)):
        list_inventory_content = line_inventory_contents[line].split(',')
        shoe_list.append([])
        shoe_obj = Shoe(list_inventory_content[0],list_inventory_content[1],list_inventory_content[2],list_inventory_content[3],list_inventory_content[4])
        shoe_list[line] = shoe_obj
        
    # Close the open txt file.  
    inventory.close()    

    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''


# Define a function that will allow the user to enter data for new shoes.
def capture_shoes():
    # Prompt user to enter the particulars of the specific shoe.
    shoe_country = input("Enter country: ")
    shoe_code = input("Enter Shoe CODE: ")
    shoe_product = input("Enter product name: ")
    shoe_cost = input("Enter Shoe cost: ")
    shoe_quantity = input("Enter Shoe quantity: ")
    # create an Shoe object of the using the data given by the user and append to the shoe_list.
    shoe_list.append(Shoe(shoe_country,shoe_code,shoe_product,shoe_cost,shoe_quantity))
    
    # These next statements serve to write the new shoe  details on the txt file, therefore updating the txt file.
    inventory = open("inventory.txt", 'w')
    inventory.write(f"{first_line}\n")
    for line in range(len(shoe_list)):
        if line == len(shoe_list)-1:
            inventory.write(f"{shoe_list[line]}")
        else:
            inventory.write(f"{shoe_list[line]}\n")
    
    inventory.close()
    print("Shoe added to database \n")
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''


# Define a function that will printout all the details of the shoes in the txt file in a table format.
def view_all():
    # Define a list variable that will store the data of the objects in shoe_list in the string representation.
    str_shoe_list = []
    # iterate through the shoe_list and append each of the objects in their string representation into the new list variable.
    for line in range(len(shoe_list)):
        str_item_shoe= str(shoe_list[line])
        item_list = str_item_shoe.split(',')
        str_shoe_list.append(item_list)

    # Print out the data of the string representations in a tabular format using the tabulate method that was imported for a more user friendly format.
    head = "country","code","product","cost","quantity"
    print(tabulate(str_shoe_list,headers= head,tablefmt='grid'))

    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''


# Define a function that will check for the shoe with the lowest quantity and  restock it.
def re_stock():
    # Define a new variable that will store the first object of the shoe_list
    lowest_quantity_shoe = shoe_list[0]
    item = 1 # Iterate through shoe_list but starting from index 1, since we already have index 0. 
    for item in range(len(shoe_list)):
            # retrieve the quantity of objects using the defined class function "get_quantity".
            # Compare the quantities of shoes. and always save the one with the lowest quantity till you have iterated through all the objects in shoe_list
            if int(Shoe.get_quantity(lowest_quantity_shoe)) < int(Shoe.get_quantity(shoe_list[item])):
                pass
            else:
                lowest_quantity_shoe = shoe_list[item]

    # Remove the object with the lowest  quantity, since it will be amended and re entered into the shoe_list variable.
    shoe_list.remove(lowest_quantity_shoe)

    # Prompt user if they would like to add onto the existing quantity of shoes or enter a new quantity. 
    user_input = input(f'''Shoe: {lowest_quantity_shoe[2]}
Code: {lowest_quantity_shoe[1]}
has the lowest quantity.
Add this quantity? YES/NO: ''').lower()
    while True: # The while loop ensures that the user inputs one of the available options, if not, user will be prompted to re-enter option.
        # IF and elif statements help choose which ever option the user ha dentered.  
        if user_input == "yes": 
            try:# Try/ except statements will ensure that for this the user enters only numbers for quantity.
                # Prompt user to enter the quantity they adding.
                new_quantity = int(input("Enter quantity your adding: "))
            except ValueError:
                print("you can only input numbers for this.\n")
            # Add the quantity the user entered to the existing quantity and amend the object to be changed with the new quantity and append to the shoe_list.
            new_quantity = new_quantity + int(Shoe.get_quantity(lowest_quantity_shoe))
            lowest_quantity_shoe = Shoe(lowest_quantity_shoe[0],lowest_quantity_shoe[1],lowest_quantity_shoe[2],lowest_quantity_shoe[3],new_quantity)
            shoe_list.append(lowest_quantity_shoe)
            break

        elif user_input == "no":
            try:# Try/ except statements will ensure that for this the user enters only numbers for quantity.
                # Prompt user to enter quantity.
                new_quantity = int(input("Enter quantity: "))
            except ValueError:
                print("you can only input numbers for this.\n")
            # Take the value the user entered and amend the object to be changed with the new quantity and append to the shoe_list.
            lowest_quantity_shoe = Shoe(lowest_quantity_shoe[0],lowest_quantity_shoe[1],lowest_quantity_shoe[2],lowest_quantity_shoe[3],new_quantity)
            shoe_list.append(lowest_quantity_shoe)
            break

        else:
            # If the user had input an invalid option, print out a relevant message.
            print("You entered an invalid option, enter either yes/no: ")
    
    # These statements are to write the new list which has the amended object of the lowest quantity on the inventory.txt file.  
    inventory = open("inventory.txt", 'w')
    inventory.write(f"{first_line}\n")
    for line in range(len(shoe_list)):
        if line == len(shoe_list)-1:
            inventory.write(f"{shoe_list[line]}")
        else:
            inventory.write(f"{shoe_list[line]}\n")

    inventory.close()
    print("\nstock added\n")
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''


# Define a function that will search for a shoe using the code of the shoe and return the object to the user.
def seach_shoe():
    shoe_code = input("Enter shoe code: ")
    count = 0
    head = "country","code","product","cost","quantity"
    for item in range(len(shoe_list)):
        if shoe_code == shoe_list[item][1]:
            count += 1
            print('============================================')
            print(f'\n{shoe_list[item]}\n')
            print('============================================')
        else:
            pass

    if count == 0:
        # If the code goven by the user does not match any of the codes on file, an appropriate message should be printed.
        print("shoe code does not match any available shoe.\n")
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''


# Define a function that will printout the value of each shoe in the txt file
# The value is the total amount of money the total stock of a particular shoe has.
def value_per_item():
    shoe_value_list = []
    for item in range(len(shoe_list)):
       # Use of the class method get.cost and get.quantity.
       # These are multiplied to get the total value of a specific shoe and this will be printed on the console fpr the user. 
       shoe_value =  int(Shoe.get_cost(shoe_list[item]))* int(Shoe.get_quantity(shoe_list[item]))
       shoe_value_list.append([shoe_list[item][2],shoe_value])
    head = 'shoe', 'Value'
    print(tabulate(shoe_value_list, headers= head,tablefmt='grid'))
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''


# This function will retrieve the shoe with the highest quantity and put it on sale.
def highest_qty():
    # Define a new variable that will store the first object of the shoe_list
    highest_quantity_shoe = shoe_list[0]
    item = 1# Iterate through shoe_list but starting from index 1, since we already have index 0
    for item in range(len(shoe_list)):
            # retrieve the quantity of objects using the defined class function "get_quantity".
            # Compare the quantities of shoes. and always save the one with the highest quantity till you have iterated through all the objects in shoe_list
            if int(Shoe.get_quantity(highest_quantity_shoe)) > int(Shoe.get_quantity(shoe_list[item])):
                pass
            else:
                highest_quantity_shoe = shoe_list[item]

    # Print out a statements that puts the shoe with the highest quantity on sale.
    print(f'{highest_quantity_shoe[2]} is on sale')
    ''' Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
read_shoes_data()
while True: # While loop will ensure that the menu is the first thing to be printed and will always show unless user exits the programme.
    menu = input('''1. Add new stock of shoes
2. View all stock
3. Re-stock shortage of shoes
4. search shoe
5. Value of shoes
6. sale
e. exit
input option: ''') # Prompt user to enter an option presented to them by the menu.
    
    if menu == "1":
        capture_shoes() # call the capture_shoes method
    elif menu == "2":
        view_all()# call the view_all method
    elif menu == "3":
        re_stock()# call the re_stock method
    elif menu == "4":
        seach_shoe()# call the seach_shoe method
    elif menu == "5":
        value_per_item() # call the value_per_item method
    elif menu == "6":
        highest_qty() # call the highest_qty method
    elif menu == "e":
        exit()
    else: # If the user hasn't entered an available option an appropriate message is printed and it promts user to re-enter.
        print("oops youve entered an invalid option.")
