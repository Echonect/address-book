# This application is an address book
# The checklist for this project are as follows: 
# 
# 1. The user will be prompted for their details, including a name, phone number, email address, and home address
# - The name must be a non-empty string
# - The phone number may only be digits, no less or longer than 10
# - The email address must contain a username and domain name, separated by a singular '@' symbol. The domain suffix must contain at least one period (.)
# - The home address contains a street number, street name, street prefix (st, dr, etc.), suburb or city, state, postcode, and country    
# 
# 2. The details, once verified, will be saved to a .txt file
#
# 3. The details will be able to be retrieved later, and filtered via various specifications (e.g. people who live in Brisbane)
#
# 4. These will be printed out in the manner specified

# Variables to track app menu location
mainAppLoop = 0

# Variables to track user detail verification status
firstNameVerified = 0
lastNameVerified = 0
phoneNumberVerified = 0
emailAddressVerified = 0
homeAddressVerified = 0

# Declaring user detail variables
firstName = ""
lastName = ""
phoneNumber = ""
emailAddress = ""
homeAddress = ""

# User prompts
firstNamePrompt = "What is your first name?"
lastNamePrompt = "What is your last name?"
phoneNumberPrompt = "What is your phone number?"
emailAddressPrompt = "What is your email address?"
homeAddressPrompt = "What is your home address?"

# User error prompts
firstNameErrorPrompt = "First name not acceptable. Please re-enter your first name."
lastNameErrorPrompt = "Last name not acceptable. Please re-enter your last name."
phoneNumberErrorPrompt = "Phone number not acceptable. Please re-enter you phone number."
emailAddressAtSymbolErrorPrompt = "@ symbol not found in email address. Please re-enter your email address"

# User feedback prompts
feedbackFirstName = "First name accepted."
feedbackLastName = "Last name accepted."
feedbackPhoneNumber = "Phone number accepted."
feedbackEmailAddress = "Email address accepted."
feedbackHomeAddress = "Home address accepted."

# App formatting
chevronIndicator = ">"
newLine = "\n"
tab = "\t"

# Function to verify the first name is acceptable
def firstNameVerification():
    global firstName
    global firstNameVerified

    firstNameVerified = 0

    firstName = input(f"{firstNamePrompt}{newLine}{chevronIndicator} ")
    
    while (firstNameVerified == 0):
        if (not firstName):
            firstName = input(f"{tab}{firstNameErrorPrompt}{newLine}{chevronIndicator} ")
        else:
            firstNameVerified = 1
            print(f"{tab}{feedbackFirstName}{newLine}")

# Function to verify the last name is acceptable
def lastNameVerification():
    global lastName
    global lastNameVerified

    lastNameVerified = 0

    lastName = input(f"{lastNamePrompt}{newLine}{chevronIndicator} ")

    while (lastNameVerified == 0):
        if (not lastName):
            lastName = input(f"{tab}{lastNameErrorPrompt}{newLine}{chevronIndicator} ")
        else:
            lastNameVerified = 1
            print(f"{tab}{feedbackLastName}{newLine}")

# Function to verify the phone number is acceptable
def phoneNumberVerification():
    global phoneNumber
    global phoneNumberVerified

    phoneNumberVerified = 0

    phoneNumber = input(f"{phoneNumberPrompt}{newLine}{chevronIndicator} ")

    while (phoneNumberVerified == 0):

        phoneNumberStringList = list(phoneNumber)

        if (len(phoneNumberStringList) != 10 or phoneNumber.isnumeric() == False):
            phoneNumber = input(f"{tab}{phoneNumberErrorPrompt}{newLine}{chevronIndicator} ")
        else:
            phoneNumberVerified = 1
            print(f"{tab}{feedbackPhoneNumber}{newLine}")

# Function to verify the email address is acceptable
def emailAddressVerification():
    global emailAddress
    global emailAddressVerified

    emailAddressVerified = 0

    emailAddress = input(f"{emailAddressPrompt}{newLine}{chevronIndicator} ")

    while (emailAddressVerified == 0):

        emailAddressSplit = emailAddress.split('@')

        if (emailAddress.find() == -1):
            print("")

        #for emailAddressCharacter in emailAddressStringList:
        #    if (emailAddressCharacter == "@"):
        #        print("@ found")



# Main app loop
while(mainAppLoop == 0):

    firstNameVerification()

    lastNameVerification()

    phoneNumberVerification()

    emailAddressVerification()
    