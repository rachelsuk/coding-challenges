"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(s):
    """Evaluate expression."""
    stack = []
    operators = {"-", "+", "*", "/"}
    s_list = s.split(" ")

    while s_list:
        char = s_list.pop()
        if char in operators:
            num_1 = int(stack.pop())
            num_2 = int(stack.pop())
            if char == "-":
                stack.append(num_1-num_2)
            elif char == "+":
                stack.append(num_1+num_2)
            elif char == "*":
                stack.append(num_1*num_2)
            elif char == "/":
                stack.append(num_1/num_2)
        else:
            stack.append(char)
    return int(stack[0])


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n")
