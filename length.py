def length(string):
    
    if type(string) == int:
        return "Sorry Integers does not have length"
        
    else:
        return len(string)


string = input("Enter any word: ")
print (length(string))