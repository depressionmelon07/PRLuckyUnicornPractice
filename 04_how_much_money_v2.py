# Functions under this line ******************************************
def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if amount is too high/low then give
            if low < response <= high:
                return response

                # output error
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine under this line ******************************************
how_much = num_check("How much would you like to play with ?", 0, 10)

print("You will be spending ${}".format(how_much))
# print the
