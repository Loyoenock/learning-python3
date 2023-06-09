"""
    Prompts the user to enter an integer value for 'x' and prints its value.

    Raises:
        ValueError: If the input provided by the user is not an integer.
"""

try:
    x = int(input("What's x? "))

except ValueError:
    print("x is not an integer")
else:
    print(f'x is {x}')
