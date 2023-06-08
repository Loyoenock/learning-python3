"""Print students and their coresponding Hall from the dictionary"""
students = {
        "Hermione": "Gryffindor",
        "Harry": "Gryffindor",
        "Ron": "Gryffindor",
        "Draco": "Slytherin"
        }


for student in students:
    print(student, students[student], sep=', ')
