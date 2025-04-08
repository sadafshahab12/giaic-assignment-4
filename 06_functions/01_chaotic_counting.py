# Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch. We've written a done() function which returns True with likelihood DONE_LIKELIHOOD -- at each number, before printing the number, you should call done() and check if it returns True or not. If done() returns True, we're done counting, and you should use a return statement to end the chaotic_counting() function execution and resume execution of main(), which will print "I'm done.". We've written main() for you -- check it out! Notice that we'll only print "I'm done" from main() once chaotic_counting() is done with its execution.

# Here's a sample run of this program:

# I'm going to count until 10 or until I feel like stopping, whichever comes first. 1 2 3 I'm done.

import random


def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return
        print(curr_num)


def done():
    """Return true with a probability of DONE_LIKELIHOOD"""
    DONE_LIKELIHOOD = 0.3 # probability for print number if true counting stop and false then counting will be print
    # randomval = random.random()  generate value from 0 to 1
    # print(randomval)
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False


def main():
    print(
        "I am going to count until 10 or until I feel like stopping, whichever comes first."
    )
    chaotic_counting()
    print("I am done")


if __name__ == "__main__":
    main()
