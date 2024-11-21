#use print function to print the string
print("Hello World")


#assigning variable to the name 
name = input("What is your name : ").strip().title()

# #Remove whitespace from str
# name = name.strip()

# #capitalize users name
# name = name.title()

print("Hello " + name)

#split users name into first name and last name
first, last = name.split(" ")


#use of sep and end
print("Hello",name, sep="???? ")
#print(name)
print("Hello", "World", sep=" ", end="!!!!\n") # use at the end of print statement

#escape use to high light text with cots
print("Hello, \"Friend\"") # use \\ to escape the \n

#f string 
print(f" Hello, {name} This is the python programming language.")


