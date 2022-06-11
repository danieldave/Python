
#an interactive interface that asks about how you are feeling and takes in input of your name and age and perform little arithmetic functions

greeting1 = "Hi, welcome to your first windows application with python"
print(greeting1)

greeting2 = input("I'm your Personal Assitant, How are you feeling today?")
print(greeting2)

name = input("Whats your name?")
print("Welcome " + name)

print("Lets do some aritmetic operations")
ready = "Are you ready ?"
print(ready)

print("A=2")
print("B=4")
print("a + b = ?")
answer=input("What is the sum of A and B")
print(answer) 

age = input("Enter your age: ")

new_age = int(age) + 50
print(new_age)

print (name[0:3])
print (name[-4:-1])

remarks = ["You're ", 100, "ready"]
print(remarks)
