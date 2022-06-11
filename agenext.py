
def age_next(age):
    new_age = int(age) + 1
    return new_age

def age_year(age):
    year_age = 2022 - int(age) 
    return year_age


name = input("Kindly Enter Your Name ")
greeting = ("Welcome to your dashboard", name)
print  (greeting)
age = input("Enter your age please ")
print (name, "will be ___ old next year ")
confirm = input("Will you like to proceed ?")
if confirm == "yes":
    print (name, "will be", (age_next(age)), "next year")
else:
     print ("I didnt get that")
print ("Would you like to check the year ,", name , "was born?" )
confirm = input("Will you like to proceed ?")
print (name , "was born in the year", (age_year(age)))

status = input("What is your current marital status? ")
if status == "single":
    print("You're ready to get married") 
elif status == "married":
    print("Wow, that's cool and how many kids do you have?")
else:
    print("What happened?, You are not single and married, are you divorced ?")