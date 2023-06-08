"""Prints a list of students from a dictionary"""
students = [
        {'name': 'Hermione', 'house': 'Gryffindor', 'patronous': 'Otter'},
        {'name': 'Harry', 'house': 'Gryffindor', 'patronous': 'Stag'},
        {'name': 'Ron', 'house': 'Gryffindor', 'patronous': 'Jack Russell terrier'},
        {'name': 'Draco', 'house': 'Slytherin', 'patronous': None}
        ]
for student in students:
    print(student['name'], student['house'], student['patronous'], sep=', ')
