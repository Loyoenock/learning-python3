# Creates an input  with varaible name
name = input("What is your name ")

# Get only the first name
first, last = name.split()
# Print greeting and name
print(f"Hello {first}!")
