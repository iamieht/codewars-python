# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
def group_strings_into_lists(text):
    final_list = []
    temp_list = []

    for char in text:
        if char != ' ':
            temp_list.append(char)
        else:
            final_list.append(temp_list)
            final_list += [[char]]
            temp_list = []

    final_list.append(temp_list)
    return final_list


def reverse_words(text):
    text_lst = group_strings_into_lists(text)
    reversed_string = ''
    # reverse each sublist
    for sublist in text_lst:
        sublist.reverse()

    # join into a final string
    for sublist in text_lst:
        reversed_string += "".join(sublist)

    return reversed_string


# Examples
text1 = "This is an example!"
print(reverse_words(text1))     # sihT si na !elpmaxe
text2 = "double  spaces"
print(reverse_words(text2))     # elbuod  secaps
text3 = "double  spaced  words"
print(reverse_words(text3))     # elbuod  decaps  sdrow

# print(group_strings_into_lists(text1))
# print(group_strings_into_lists(text2))
# print(group_strings_into_lists(text3))
