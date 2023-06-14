with open("students.csv") as file:
    for line in file:
        name, residence  = line.rstrip().split(",")
        print(f"{name} stays in {residence}")
