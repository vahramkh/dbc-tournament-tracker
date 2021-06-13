#Functions

#Function to help determine the number of participants

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    if(userInput < 1):
        print("Type a positive integer")
    else:
       return userInput 
       break 

#Function to help determine which menu option was chosen
def menu():
    print("Participant menu\n================\n1. Sign Up\n2. Cancel Sign Up\n3. View Participants\n4. Exit")
    while True:
        try:
            userInput = int(input("Enter a menu option: "))       
        except ValueError:
            print("Not an integer! Try again.")
            continue
        if userInput > 4:
            print("Thats not a valid option.")
        elif(userInput < 1):
            print("Type a positive integer")
        else:
            return userInput 
            break 

#Function to help with the sign up
def signup():
    print("Participant Sign Up\n====================")
    while True:
        userInput = input("Participant Name: ")     
        if(userInput == ""):
            print("Please input something")
            continue
        elif(" " not in userInput):
            print("First AND last name needed")
        elif(not userInput.replace(" ","").isalpha()):
            print("Input a valid name")
        else:
            break     
    while True:
        try:
            startingSlot = int(input("Desired starting slot #[1-" + str(count_of_participants) +"]:"))       
        except ValueError:
            print("Not an integer! Try again.")
            continue
        if startingSlot > count_of_participants:
            print("Your input is greater than " + str(count_of_participants)+ ": Please input a smaller integer")
        elif(int(startingSlot) < 1):
            print("Type a positive integer")
        elif None not in participants:
            print("All the slots are full!")
            break
        elif participants[startingSlot-1] != None:
            print("Slot #" + str(startingSlot) + " is filled.  Please try again.")
        else:
            participants[startingSlot-1] = userInput
            break 
            return None


     

#MAIN PROGRAM STARTS HERE:
print("Welcome to Tournaments R Us")
count_of_participants = inputNumber("Enter the number of participants:")
participants = []
for i in range(0,count_of_participants):
    participants.append(None)
print("There are " + str(len(participants)) + " participant slots ready for sign-ups.")
menu_option = menu()
if(menu_option == 1):
    signup()
#elif(menu_option == 2):
#
#elif(menu_option == 3):

#else:

