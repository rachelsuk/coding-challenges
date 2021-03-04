def print_table(n):
    """ Prints n times table """
    try:
        for row in range(1,n+1):
            row_numbers = ''
            longest_len = len(str(n**2))
            for column in range(1,n+1):
                product = row*column
                spaces = longest_len - len(str(product)) + 2
                row_numbers += f'{" " * spaces}{product}'
            print(row_numbers)
    except TypeError:
        print('argument must be an integer')



        
