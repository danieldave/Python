print ("Welcome to password checker")

username = input("Enter Username: ")
password = input("Enter password: ")
password2 = input("Re-Enter password: ")
while password2 != password:
    password2 = input("Re-Enter password: ")
    if password2 == password:
        print("You're logged in " + username)
    else:
        print("Try again, password does not match")