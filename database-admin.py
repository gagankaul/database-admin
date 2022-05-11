#Database Admin Program

#Welcome message
print("Welcome to the Database Admin Program\n")

#Login and password information for authorized users stored in a dictionary as key-value pairs
login_master = {
    "mooman74":"alskes145",
    "gagank":"world1star",
    "admin00":"admin1234",
    "george2":"booo3oha",
    "jamaicas":"eightsix",
}

#Get user input
username = input("Enter your username: ")

#Check for valid login name first and then authenticate the password
if username in login_master.keys():
    password = input("Enter your password: ")
    if password == login_master[username]:
        print(f"\nHello, {username}. You are now logged in.")

        #Display full dictionary if admin logs in.
        if username == "admin00":
            print("\nHere is the current user database:")
            for key,value in login_master.items():
                print("Username: " + key + "\tPassword: " + value)
        else:
            #Allow standard user to change password
            change_passwd = input("Would you like to change your password (y/n): ").lower().strip()
            #If changing password, check that password is minimum 8 characters
            if change_passwd == "y":
                new_passwd = input("\nWhat would you like your new password to be (minimum 8 characters): ")
                if len(new_passwd) >= 8:
                    login_master[username] = new_passwd
                    print(f"{username}, your new password is {login_master[username]}")
                else:
                    print("new_passwd is less than eight characters.")
            else:
                #Authenticated user would not like to change password
                print("Okay. Goodbye then!")
    else:
        #If username is valid but password is wrong
        print("You seem to have entered an incorrect password.")
else:
    #Username not in database
    print("This is not an authorized user.")