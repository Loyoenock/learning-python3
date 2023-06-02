def greet_users(names):
    """Print asimple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


usernames = ['Hanok', 'Shalom', 'Daud']
greet_users(usernames)

