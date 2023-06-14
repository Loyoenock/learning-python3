""" Using the append 'a' to write and add more content to an existing file"""

name = input("What's your name? ")


with open("names22.text", "a") as file:
    file.write(f"{name}\n")
