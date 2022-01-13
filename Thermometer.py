# ----------- SMALL TERMOMETER ----------------

ABSOLUTE_ZERO = -273.15
temp_list = []; #This list will store all the measurements


def my_max():
    """This function will return the maximum Temperature registered"""
    
    if not temp_list: #Checking if the list is empty
        print("The Measurements are empty, please enter at least a number\n")
    else:
        print("The Highest Temperature registered is {temp} °C\n".format(temp=max(temp_list)))



def my_min():
    """This function will return the minimum Temperature registered"""
    
    if not temp_list: #Checking if the list is empty
        print("The Measurements are empty, please entrer at least a number\n")
    else:
        print("The Lowest Temperature registered is {temp} °C\n".format(temp=min(temp_list)))    



def my_average():
    """This function will return the average of the Temperatures registered"""
    
    if not temp_list: #Checking if the list is empty
        print("The Measurements are empty, please entrer at least a number\n")
    else:
        print("The Average Temperature is {temp} °C\n".format(temp=sum(temp_list)/len(temp_list)))
    
    

def clear():
    """This function will clear all the Temperatures registered"""
    
    temp_list.clear()
    print("Measurements cleared\n")
    


def enter():
    while True:
        try:
            user_input = float(input('Enter a measurement: ')) 
            if user_input > ABSOLUTE_ZERO : #Making sure the measurement is above absolute zero
                temp_list.append(user_input); #Adding the measurements to the list
                print('{temp} °C measurement was saved '.format(temp=user_input))
            else:
                print("Temperature below absolute zero, Impossible. Please enter a valid temperature.\n")
        except ValueError: #If input isn't a float, then break. That's how we go back to the 'menu'
            print('\nText detected, going back to the menu \n')
            helping()
            break

def helping():
    """This function is used to inform the user about the choices available"""
    
    print(" Enter", '\033[1m', "'enter'",'\033[0m', "to register a temperature \n")    
    print(" Enter", '\033[1m', "'max'",'\033[0m',"for Maximum")
    print(" Enter", '\033[1m', "'min'",'\033[0m' "for Minimum")
    print(" Enter", '\033[1m', "'average'",'\033[0m', "for Average")
    print(" Enter", '\033[1m', "'clear'",'\033[0m' ,"to clear the measurements")
    print("\n Enter", '\033[1m', "'quit'",'\033[0m' ,"to quit \n")




helping() #Since we don't want the help commands to be written every time, we just write them down when we start, or if we call them
while True:
    print("Choose what you'd like to do : ")
    choice=input(" ")
    if choice!= "quit": #The key word to end the program is 'quit', any other input will be interpreted to call designated functions
        if choice == 'max':
            my_max()
        elif choice == 'min':
            my_min()
        elif choice == 'average':
            my_average()
        elif choice == 'clear':
            clear()
        elif choice == 'enter':
            enter()
        elif choice == 'help':
            helping()
        else: #If no input matches the available commands (but is NOT 'quit') then...
            print("Nothing matched your input, Please try again \n")
    else:
        break
