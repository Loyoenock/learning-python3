""" Using the append 'a' to write and add more content to an existing file"""

name = input("What's your name? ")


file = open("names1.text", "a")
file.write(f"{name}\n")
file.close()
