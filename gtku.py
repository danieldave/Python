
print("Welcome to Get To Know Us V1.0.0.0.1")

User  = input ("Enter Username: ")
fullname= input ("Enter Your Full Name: ")
colleague1 = input ("Enter colleagues full name: ")
colleague2 = input ("Enter colleagues full name: ")
colleague3 = input ("Enter colleagues full name: ")
colleague4 = input ("Enter colleagues full name: ")
colleague5 = input ("Enter colleagues full name: ")
colleague6 = input ("Enter colleagues full name: ")
colleague7 = input ("Enter colleagues full name: ")
colleague8 = input ("Enter colleagues full name: ")
colleague9 = input ("Enter colleagues full name: ")
colleague10 = input ("Enter colleagues full name: ")

contact = input("Enter " + User + " contact: ")
contact1 = input("Enter " + colleague1 +  " contact: ")
contact2 = input("Enter " + colleague2 +  " contact: ")
contact3 = input("Enter " + colleague3 +  " contact: ")
contact4 = input("Enter " + colleague4 +  " contact: ")
contact5 = input("Enter " + colleague5 +  " contact: ")
contact6 = input("Enter " + colleague6 +  " contact: ")
contact7 = input("Enter " + colleague7 +  " contact: ")
contact8 = input("Enter " + colleague8 +  " contact: ")
contact9 = input("Enter " + colleague9 +  " contact: ")
contact10 = input("Enter "  + colleague10 +  " contact: ")

mail = input("Enter your mail address: ")
mail1 = input("Emter " + colleague1 + " valid mail address: ")
mail2 = input("Emter "+ colleague2 + " valid mail address: ")
mail3 = input("Emter "+ colleague3 + " valid mail address: ")
mail4 = input("Emter "+ colleague4 + " valid mail address: ")
mail5 = input("Emter "+ colleague5 + " valid mail address: ")
mail6 = input("Emter "+ colleague6 + " valid mail address: ")
mail7 = input("Emter "+ colleague7 + " valid mail address: ")
mail8 = input("Emter "+ colleague8 +" valid mail address: ")
mail9 = input("Emter "+ colleague9 + " valid mail address: ")
mail10 = input("Emter "+ colleague10 + " valid mail address: ")

users = [fullname,colleague1,colleague2,colleague3,colleague4,colleague5,colleague6,colleague7,colleague8,colleague9,colleague10]
contacts = [contact,contact1,contact2,contact3,contact4,contact5,contact6,contact7,contact8,contact9,contact10]
mails = [mail,mail1,mail2,mail3,mail4,mail5,mail6,mail7,mail8,mail9,mail10]




print ("Would you like to review your information before proceeding?")
fullinfo = (fullname,mail,contact)
print (fullinfo)
print ("Would you like to see your basic info")
basicInfo = (User,fullname)
print (basicInfo)

print ("Thank you ", User)