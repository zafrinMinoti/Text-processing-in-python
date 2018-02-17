'''
This program take a text file as input and
returns a dectionary where
	- keys are the unique first caracters of the lines
	- values are lists of all line numbers where 
	the character is the first letter
'''

def make_char_dict(filename):
    textfile = open(filename)

    char_dict = {}
    line_number = 0

    for line in textfile:
        line_number += 1
        char = line[0]
        if char in char_dict:
            char_dict[char].append(line_number)

        else:
            char_dict[char] = [line_number]

    return char_dict
