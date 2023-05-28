#Assign a name to a variable input
name = input("What is your name ")

#Remove trailing spaces and Capitalize every begining letter of the name
name = name.strip().title()
#Print Greeting + name
print(f"Hello {name}")
