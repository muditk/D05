#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    try:
        user_input = int(input("Enter a number\n"))
        if user_input % 2 == 0:
            print("Thanks for the even number")
        else:
            print("Hey, that's an odd number")
    except:
            print("Please enter a number")
    return


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    for i in range(1, 101):
            print(i, end=" ")
            if i % 10 == 0:
                print("\n")


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    try:
        count = 0
        user_input = 0
        total = 0
        while True:
            user_input = input("Enter numbers, type done to get average")
            if user_input != 'done':
                total = int(total) + int(user_input)
                print(total)
                count += 1
            else:
                print(total/int(count))
    except:
            print("Please enter a number")


##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    #even_odd()
    #ten_by_ten()
    find_average()

if __name__ == '__main__':
    main()
