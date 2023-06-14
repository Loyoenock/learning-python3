with open("names22.text", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())
