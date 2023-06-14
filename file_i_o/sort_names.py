names = []


with open("names22.text") as file:
    for line in file:
        names.append(line.rstrip())


for name in sorted(names):
    print(f"Hello, {name}")
