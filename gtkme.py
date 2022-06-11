print("Welcome to Get To Know Me V1.0.0.0.1")

firstname = input ("Enter First Name")
secondname = input ("Enter Last Name")
age = input ("Enter Your age")
email = input ("Enter your valid e-mail address")
contact = input ("Enter your Phone Number")

print ("Would you like to review your information before proceeding?")
fullinfo = (firstname,secondname,age,email,contact)
print (fullinfo)
basicInfo = (firstname,secondname,age)
print (basicInfo)

print ("Thank you ", secondname)