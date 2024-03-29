import random

# main routine under this line *************************************


STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens

for item in range(0, 10):
    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

    # if the random # is between 6 and 36,
    # user gets a donkey (minus $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1

    # the token is either a zebra or a horse
    # in both circumstances, subtract $0.50 from balance
    else:
        # if the number is even, set the chosen item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse "
        # otherwise set to a zebra
        else:
            chosen = "zebra"
            balance -= 0.5

    # output
    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))

print()

print("Starting balance: ${:.2f}, Final Balance: {:.2f}".format(STARTING_BALANCE, balance))
