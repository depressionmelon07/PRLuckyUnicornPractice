# Functions under this line ******************************************


# Main routine under this line ******************************************

error = "Please enter a whole number between 1 and 10\n"

valid = False
while not valid:
    try:
        # ask the question
        response = int(input("How much money would you like to play with? "))
        # if amount is too high/low then give
        if 0 < response <= 10:
            print("You have asked to play " "with ${}".format(response))

            # output error
        else:
            print(error)

    except ValueError:
        print(error)
    # print the
