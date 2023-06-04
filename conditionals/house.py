name = input('What is your name: ')

match name:
    case 'Harry':
        print('Gryffindor')
    case 'Hermione':
        print('Gryffindor')
    case 'Ron':
        print('Griffindor')
    case 'Draco':
        print('Slytherin')
    case _:
        print('Who')
