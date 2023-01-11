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

# Declaring user detail variables
firstName = ""
phoneNumber = ""
emailAddress = ""
homeAddress = ""

# User prompts
namePrompt = "What is your name?"
phoneNumberPrompt = "What is your phone number?"
emailAddressPrompt = "What is your email address?"
homeAddressPrompt = "What is your home address?"

# User incorrect entry prompts
reenterName = "First name field is empty. Please re-enter your first name"


# User feedback prompts
feedbackName = "Username accepted"

# App formatting
chevronIndicator = ">"
newLine = "\n"

# Function to verify the name is acceptable
def nameVerification():
    if not name:
        print(f"{reenterName}")
    else:
        global mainAppLoop 
        mainAppLoop = 1
        print(f"{feedbackName}")

# Function to verify the phone number is acceptable
def phoneNumberVerification():
    if not phoneNumber:

"""
phoneNumber = input(f"{phoneNumberPrompt}{newLine}{chevronIndicator}")
emailAddress = input(f"{emailAddressPrompt}{newLine}{chevronIndicator}")
homeAddress = input(f"{homeAddressPrompt}{newLine}{chevronIndicator}")
"""

while(mainAppLoop == 0):
    name = input(f"{namePrompt}{newLine}{chevronIndicator}")

    nameVerification()

print(name) #, phoneNumber, emailAddress, homeAddress)