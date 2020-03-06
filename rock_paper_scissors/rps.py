#!/usr/bin/python


# Hints

#  * You'll want to define a list with all of the possible Rock Paper Scissors plays.
#  * Another problem that asks you to generate a bunch of permutations,
#  so we're probably going to want to opt for using recursion again.
#  Since we're building up a list of results, we'll have to pass the list
#  we're constructing around to multiple recursive calls so that each recursive call
#  can add to the overall result. However, the tests only give our function `n` as
#  input. To get around this, we could define an inner recursive helper function that will
#  perform the recursion for us, while allowing us to preserve the outer function's function signature.
#  * In Python, you can concatenate two lists with the `+` operator. However, you'll want to make sure that both operands are lists!
#  * If you opt to define an inner recursive helper function, don't forget to make an initial call to the recursive helper function to kick off the recursion.

import sys


def rock_paper_scissors(n):
    possible_options = ['rock', 'paper', 'scissors']
    total_combinations = []

    def helper(iterations, total):
        if iterations == 0:
            total_combinations.append(total)
            return total_combinations

        for options in possible_options:
            helper(iterations-1, total + [options])
    helper(n, [])
    return total_combinations


print(rock_paper_scissors(2))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
