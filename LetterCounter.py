from collections import *
import string

# get the text file
textfile = open('dracula.txt').read().lower()

count_letters_raw = Counter(textfile)
#print(count_letters_raw)


# Get a list of letters
letters = list(string.ascii_letters)

# Clean dict for letters
count_letters = dict()
for k,v in count_letters_raw.items():
	if k in letters:
		count_letters[k] = v

print(count_letters)

### Ways of improving
# take file input
# system file handeling