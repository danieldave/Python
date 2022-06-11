print ("This program gets a string/ strings from user and sends back the lenght as output")

def stringlength(string):
    lenght  = len(string)
    return lenght

print ("Are you ready to get the lenght of new words? ")

string = input("Enter the word now: ")
print ("The above word", string , "has ", stringlength(string) , "alphabets", "Thank you")