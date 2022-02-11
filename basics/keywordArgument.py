#!/usr/bin/env python3

# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only



# Method parrot accepts:
# @param one required argument (voltage)
# @param three optional arguments (state, action, and type).
# This function can be called in any of the following ways:

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


def parrotWithNoRequiredArgument(voltage='1000', state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


if __name__ == "__main__":
    # Valid calls:
    parrot(1000)                                          # 1 positional argument
    parrot(voltage=1000)                                  # 1 keyword argument
    parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
    parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
    parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
    parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

    
    print("*******************************************")
    # How does python catch exceptions for all method calls? Guess not possible
    try:
        # Invalid calls:
        parrot()                     # required argument missing
        # parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
        # parrot(110, voltage=220)     # duplicate value for the same argument
        # parrot(actor='John Cleese')  # unknown keyword argument
    except (SyntaxError, TypeError):
        print("!!!!!Something went wrong!!!!!!")
    
    print("*******************************************")
    # required argument missing
    parrotWithNoRequiredArgument()

    # non-keyword argument after a keyword argument
    # Wrong:    parrotWithNoRequiredArgument(voltage=5.0, 'dead')
    parrotWithNoRequiredArgument(voltage=5.0, state='dead')

    # duplicate value for the same argument
    # Wrong:    parrotWithNoRequiredArgument(110, voltage=220)
    parrotWithNoRequiredArgument(voltage=220)

    # unknown keyword argument
    # parrotWithNoRequiredArgument(actor='John Cleese')

    
