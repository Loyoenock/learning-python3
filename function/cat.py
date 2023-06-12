""" Receive an in put from a user that prints how many times a cat meows"""
def main():
    number = get_number()
    meow(number)



def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
