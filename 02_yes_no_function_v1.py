# PROGRAM JOBS*****************
# If they respond yes, output 'program continues'
# If they say something else, an error message in printed
# If they respond no, output 'display instructions'
# PROGRAM JOBS*****************

# Functions under this line **********************************************
def yes_no(question):
    valid = False
    while not valid:
        response = input("Have you played this game before?").lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer with Yes or No")


# Main routine under this line ******************************************

# Ask user if they have played before
show_instructions = yes_no("Have you played this game before?")

print("You chose {}".format(show_instructions))
print()
having_fun = yes_no("Are you having fun?")
print("You said {} to having fun".format(having_fun)) 
