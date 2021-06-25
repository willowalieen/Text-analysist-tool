

#Welcome User
def welcomeUser():
    print("\nWelcome to the text analysist tool, will mine and analyze a body of text from a file you give me")

# Get Username
def getUsername():  

    maxAttempts = 3
    attempts = 0

    while attempts < maxAttempts:

        #Print message prompting user to input their name
        inputPrompt = ""
        if attempts == 0:
            inputPrompt = "\n To beging, please enter your username:\n"
        else:
            inputPrompt = "\nPlease try again\n"
        usernameFromInput = input(inputPrompt)

        #Validate Username
        if len(usernameFromInput) < 5 or not usernameFromInput.isidentifier():
            print("Your username must be at least 5 characters long, alphanumeric only (a-z/A-Z/0-9), have no spaces, and cannot start with a number!")
        else: 
            return usernameFromInput
        
        attempts += 1

    print("\nExhausted all" + str(maxAttempts)  + "attempts, assigning username instead...")
    return generate_username()[0]       
        
# Greet the User
def greetUser(name): 
    print("Hello, " + name)


welcomeUser() 
username = getUsername()
greetUser(username)



