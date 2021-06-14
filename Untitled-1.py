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

#Function to help with viewing the participants
def viewparticipants():
    print("View Participants\n====================") 
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
        else:
            for i in range(startingSlot-1,len(participants)):
                if participants[i] == None:
                    print(str(i+1) + ": [empty]")
                else:
                    print(str(i+1) + ": " + participants[i])
            break 
            return None

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



def cancel():
    print("Participant Cancellation\n================")
    while True:
        try:
            userInput = int(input("Starting slot #[1-" + str(count_of_participants) + "]:"))       
        except ValueError:
            print("Not an integer! Try again.")
            continue
        if userInput > count_of_participants or userInput < 1:
            print("Thats not a valid option.")
        else:
            userInputName = input("Participant Name: ")
            if userInputName == participants[userInput-1]:
                participants[userInput-1] = None
                print(userInputName + " has been cancelled from starting slot #" + str(userInput))
            else:
                print(userInputName + " is not in that starting slot")
            break


def exit():
    print("Exit\n================")
    while True:
        userInput = input("Are you sure you want to exit? Type yes for exit, no to go back to main menu\nAll the data will be lost: ")     
        if userInput == "yes":
            return userInput
        elif userInput == "no":
            return userInput
        else:
            print("That is not a valid input")
     

#MAIN PROGRAM STARTS HERE:
print("Welcome to Tournaments R Us")
count_of_participants = inputNumber("Enter the number of participants:")
participants = []
for i in range(0,count_of_participants):
    participants.append(None)
print("There are " + str(len(participants)) + " participant slots ready for sign-ups.")

while True:
    menu_option = menu()
    if(menu_option == 1):
        signup()
    elif(menu_option == 2):
        cancel()
    elif(menu_option == 3):
        viewparticipants()
    else:
        answer = exit()
        if answer == "yes":
            print("Goodbye")
            break

