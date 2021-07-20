"""Write a function that encrypts a string with a variable rotary cipher.

The function should take in a number and string and shift the string's
characters by that number:

>>> rot_encode(1, 'abcxyz')
'bcdyza'

It should be able to shift characters by any number:

>>> rot_encode(3, 'abcxyz')
'defabc'

It should preserve capitalization, whitespace, and any special characters:

>>> rot_encode(1, 'Wow! This is 100% amazing.')
'Xpx! Uijt jt 100% bnbajoh.'
"""


def rot_encode(shift, txt):
    """Encode `txt` by shifting its characters to the right."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_txt = ""
    for char in txt:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            if index+shift >= len(alphabet):
                new_index = (index+shift) % len(alphabet)
            else:
                new_index = index + shift
            new_char = alphabet[new_index]
            if char not in alphabet:
                new_char = new_char.upper()
            new_txt = new_txt + new_char
        else:
            new_txt = new_txt + char
    return new_txt


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
