"""
    Prompts the user to enter an integer value for 'x' and prints its value.

    Raises:
        ValueError: If the input provided by the user is not an integer.

    Usage:
        - Call the 'get_integer' function to prompt the user for an integer value.
        - If the user enters a non-integer value, a 'ValueError' will be raised and
          an error message will be displayed.
"""

try:
    x = int(input("What's x? "))
    print(f'x is {x}')

except ValueError:
    print("x is not an integer")
