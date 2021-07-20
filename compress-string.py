"""Write a function that compresses a string.

Repeated characters should be compressed to one character and the number of
times it repeats:

>>> compress('aabbaabb')
'a2b2a2b2'

If a character appears once, it should not be followed by a number:

>>> compress('abc')
'abc'

The function should handle letters, whitespace, and punctuation:

>>> compress('Hello, world! Cows go moooo...')
'Hel2o, world! Cows go mo4.3'
"""


def compress(string):
    """Return a compressed version of the given string."""
    new_str = string[0]
    #new_str = "Hel2o"
    current = string[0]
    #current = "o"
    nums = set("0123456789")
    for char in string[1:]:
        #char = o
        if char == current:
            if new_str[-1] in nums:
                new_str = new_str[:-1] + str(int(new_str[-1]) + 1)
            else:
                new_str = new_str + "2"
        else:
            new_str = new_str + char
            current = char
    return new_str


compress("Hello, world! Cows go moooo...")

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
