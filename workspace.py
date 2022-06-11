#def string_length(mystring):
 #    if type(mystring) == int:
  #       return "Sorry, integers don't have length"
   #  elif type(mystring) == float:
    #     return "Sorry, floats don't have length"
     #else:
      #   return len(mystring)
#
#mystring = input("Enter value: ")
#print (string_length(mystring))


def c_to_f(c):    
    if c< -273.15:        
        return "That temperature doesn't make sense!"    
    else:        
        f=c*9/5+32        
        return f
print(c_to_f(-273.4))