emails = ['abc@gmail.com','def@hotmail.com','ghji@yahoo.com','klmn@gmail.com','opq@outlook.com','freshboy@gmail.com','saveme@yahoo.com','wemove@outlook.com']

for items in emails:
    if 'gmail' in items:
        print (items)

c = [10,-20,-289,100]
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f


for values in c:
    print(c_to_f(values))
