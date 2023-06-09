"""
    Prompts the user to enter an integer value for 'x' and prints its value.

    Raises:
        ValueError: If the input provided by the user is not an integer.
"""
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))

        except ValueError:
            print("x is not an integer")
        
            
main()
