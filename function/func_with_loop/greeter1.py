def get_formatted_name(first_name, last_name):
    """Return full name, neatly fromatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quite)")

    f_name  = input("first name: ")
    if f_name == 'q':
        break
    l_name = input("last name: ")
    if l_name == 'q':
        break
formatted_name = get_formatted_name(f_name, l_name)
print("\nHello {formatted_name}!")
