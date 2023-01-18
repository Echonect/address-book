# This application is an address book

# Menu banner art
menuBanner = "+--------------------+\n|    ADDRESS BOOK    |\n+--------------------+"

menuSelect = ""

# Variables to track user detail verification status
firstNameVerified = 0
lastNameVerified = 0
phoneNumberVerified = 0
emailAddressVerified = 0
streetNumberVerified = 0
streetNameVerified = 0
streetPrefixVerified = 0
suburbVerified = 0
cityVerified = 0
stateVerified = 0
postcodeVerified = 0
countryVerified = 0

# Declaring user detail variables
firstName = ""
lastName = ""
phoneNumber = ""
emailAddress = ""
streetNumber = ""
streetName = ""
streetPrefix = ""
suburb = ""
city = ""
state = ""
postcode = ""
country = ""

# User prompts
firstNamePrompt = "What is your first name?"
lastNamePrompt = "What is your last name?"
phoneNumberPrompt = "What is your phone number?"
emailAddressPrompt = "What is your email address?"
streetNumberPrompt = "What is your street number?"
streetNamePrompt = "What is your street name?"
streetPrefixPrompt = "What is your street suffix?"
suburbPrompt = "What is your suburb?"
cityPrompt = "What is your city?"
statePrompt = "What is your state?"
postcodePrompt = "What is your postcode?"
countryPrompt = "What is your country?"


# User error prompts
firstNameErrorPrompt = "First name not acceptable. Please re-enter your first name."
lastNameErrorPrompt = "Last name not acceptable. Please re-enter your last name."
phoneNumberErrorPrompt = "Phone number not acceptable. Please re-enter you phone number."
emailAddressErrorPrompt = "Email address not acceptable. Please re-enter your email address."
streetNumberErrorPrompt = "Street number not acceptable. Please re-enter your street number."
streetNameErrorPrompt = "Street name not acceptable. Please re-enter your street name."
streetPrefixErrorPrompt = "Street suffix not acceptable. Please re-enter your street suffix."
suburbErrorPrompt = "Suburb not acceptable. Please re-enter your suburb."
cityErrorPrompt = "City not acceptable. Please re-enter your city."
stateErrorPrompt = "State not acceptable. Please re-enter your state."
postcodeErrorPrompt = "Postcode not acceptable. Please re-enter your postcode."
countryErrorPrompt = "Country not acceptable. Please re-enter your country."


# User feedback prompts
feedbackFirstName = "First name accepted."
feedbackLastName = "Last name accepted."
feedbackPhoneNumber = "Phone number accepted."
feedbackEmailAddress = "Email address accepted."
feedbackStreetNumber = "Street number accepted." 
feedbackStreetName = "Street name accepted."
feedbackStreetPrefix = "Street prefix accepted."
feedbackSuburb = "Suburb accepted."
feedbackCity = "City accepted."
feedbackState = "State accepted."
feedbackPostcode = "Postcode accepted."
feedbackCountry = "Country accepted."

# App formatting
chevronIndicator = ">"
newLine = "\n"
tab = "\t"

acceptableDomainTypes = ["com", "org", "gov", "edu", "net", "au", "nz", "za", "us"]
acceptableStreetPrefix = ["st", "dr", "tce", "rd"]

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
    global acceptableDomainTypes

    emailAddressVerified = 0

    emailAddress = input(f"{emailAddressPrompt}{newLine}{chevronIndicator} ")

    while (emailAddressVerified == 0):
        
        # Check @ symbol exists
        if ("@" in emailAddress):
            
            emailAddressSplit = emailAddress.split("@")

            # Check that username exists
            if (len(emailAddressSplit[0]) > 0):
                
                # Check that domain exists
                if (len(emailAddressSplit[1]) > 0):

                    if ("." in emailAddressSplit[1]):
                        
                        emailAddressDomainSplit = emailAddressSplit[1].split(".")

                        for domainType in acceptableDomainTypes:
                            if (emailAddressDomainSplit[1] == domainType):
                                emailAddressVerified = 1
                                print(f"{tab}{feedbackEmailAddress}{newLine}")
        
        if (emailAddressVerified == 0):
            emailAddress = input(f"{tab}{emailAddressErrorPrompt}{newLine}{chevronIndicator} ")

def streetNumberVerification():
    global streetNumber
    global streetNumberVerified

    streetNumberVerified = 0

    streetNumber = input(f"{streetNumberPrompt}{newLine}{chevronIndicator} ")

    while (streetNumberVerified == 0):
        if (streetNumber.isnumeric() == True):
            streetNumberVerified = 1
            print(f"{tab}{feedbackStreetNumber}{newLine}")
        else:
            streetNumber = input(f"{tab}{streetNumberErrorPrompt}{newLine}{chevronIndicator} ")

def streetNameVerification():
    global streetName
    global streetNameVerified

    streetNameVerified = 0

    streetName = input(f"{streetNamePrompt}{newLine}{chevronIndicator} ")

    while (streetNameVerified == 0):
        if (not streetName):
            streetName = input(f"{tab}{streetNameErrorPrompt}{newLine}{chevronIndicator} ")
        else:
            streetNameVerified = 1
            print(f"{tab}{feedbackStreetName}{newLine}")

def streetPrefixVerification():
    global streetPrefix
    global streetPrefixVerified

    streetPrefixVerified = 0

    streetPrefix = input(f"{streetPrefixPrompt}{newLine}{chevronIndicator} ")

    while (streetPrefixVerified == 0):

        if (streetPrefix in  acceptableStreetPrefix):
            streetPrefixVerified = 1
            print(f"{tab}{feedbackStreetPrefix}{newLine}")    
        else:
            streetPrefix = input(f"{tab}{streetPrefixErrorPrompt}{newLine}{chevronIndicator} ")

def suburbVerification():
    global suburb
    global suburbVerified

    suburbVerified = 0

    suburb = input(f"{suburbPrompt}{newLine}{chevronIndicator} ")

    while (suburbVerified == 0):

        if (not suburb): 
            suburb = input(f"{tab}{suburbErrorPrompt}{newLine}{chevronIndicator} ")
        else:
            suburbVerified = 1
            print(f"{tab}{feedbackSuburb}{newLine}")

def cityVerification():
    global city
    global cityVerified

    cityVerified = 0

    city = input(f"{cityPrompt}{newLine}{chevronIndicator} ")

    while (cityVerified == 0):

        if (not city): 
            city = input(f"{tab}{cityErrorPrompt}{newLine}{chevronIndicator} ")
        else:
            cityVerified = 1
            print(f"{tab}{feedbackCity}{newLine}")

def stateVerification():
    global state
    global stateVerified

    stateVerified = 0

    state = input(f"{statePrompt}{newLine}{chevronIndicator} ")

    while (stateVerified == 0):

        if (not state): 
            state = input(f"{tab}{stateErrorPrompt}{newLine}{chevronIndicator} ")
        else:
            stateVerified = 1
            print(f"{tab}{feedbackState}{newLine}")

def postcodeVerification():
    global postcode
    global postcodeVerified

    postcodeVerified = 0

    postcode = input(f"{postcodePrompt}{newLine}{chevronIndicator} ")

    while (postcodeVerified == 0):

        if (postcode.isnumeric() == True and len(postcode) == 4):
            postcodeVerified = 1
            print(f"{tab}{feedbackPostcode}{newLine}")
        else:
            postcode = input(f"{tab}{postcodeErrorPrompt}{newLine}{chevronIndicator} ")


def countryVerification():
    global country
    global countryVerified

    countryVerified = 0

    country = input(f"{countryPrompt}{newLine}{chevronIndicator} ")

    while (countryVerified == 0):

        if (not country):
            country = input(f"{tab}{countryErrorPrompt}{newLine}{chevronIndicator} ")
        else:
            countryVerified = 1
            print(f"{tab}{feedbackCountry}{newLine}")

def writeToFile():
    file = open("addressbook.txt", "w")

    file.write(f"{firstName}\n{lastName}\n{phoneNumber}\n{emailAddress}\n{streetNumber}\n{streetName}\n{streetPrefix}\n{suburb}\n{city}\n{state}\n{postcode}\n{country}")

    file.close()

def readFromFile():
    file = open("addressbook.txt", "r")

    details = file.readlines()

    print(details)

    file.close()

print(menuBanner)

menuSelect = input(f"{newLine}Please type a menu option{newLine}(1) Add user details to address book{newLine}(2) Check address book details\n{chevronIndicator} ")

while (menuSelect != 1 or menuSelect != 2):
    menuSelect = input(f"{newLine}Please type a menu option{newLine}(1) Add user details to address book{newLine}(2) Check address book details\n{chevronIndicator} ")

match menuSelect:
    case "1":
        firstNameVerification()
        
        lastNameVerification()
        
        phoneNumberVerification()
        
        emailAddressVerification()
        
        streetNumberVerification()
        
        streetNameVerification()
        
        streetPrefixVerification()
        
        suburbVerification()
        
        cityVerification()
        
        stateVerification()
        
        postcodeVerification()
        
        countryVerification()
        
        writeToFile()

    case "2":
        readFromFile()

    case _:
        print("There seems to be a problem. Please restart the program")