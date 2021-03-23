

#Welcome User
def welcomeUser():
    print("\nWelcome to the text analysist tool, will mine and analyze a body of text from a file you give me")

# Get Username
def getUsername():  
    #Print message prompting user to input their name
    usernameFromInput = input("\n To beging, please enter your username:\n")
         
    if len(usernameFromInput) < 5 or not usernameFromInput.isidentifier():
        print("Your username must be at least 5 characters long, alphanumeric only (a-z/A-Z/0-9), have no spaces, and cannot start with a number!")
        usernameFromInput = "User123"
        print("Assigning new username: " + usernameFromInput)

    return usernameFromInput

# Greet the User
def greetUser(name): 
    print("Hello, " + name)


welcomeUser() 
username = getUsername()
greetUser(username)



