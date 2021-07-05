def commonChars(A):
    common_char_list = []
    first_word = A.pop()
    for letter in first_word:
        common = True
        for word in A:
            if letter not in word:
                common = False
                break
        if common:
            common_char_list.append(letter)
            for index, word in enumerate(A):
                l_index = word.index(letter)
                A[index] = word[:l_index]+word[l_index+1:]

    return common_char_list


commonChars(["cool", "lock", "cook"])
