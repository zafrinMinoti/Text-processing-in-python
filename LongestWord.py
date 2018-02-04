# Get Text
while True:
	text = input('Enter a string or name of a text document:\n\t')
	print('Be sure to include .txt extension of the file')

	if text[-4:] == '.txt':
		try:
			text = open(text).read()
			break
		except:
			print('Could not read the file.\nPlease check the destination of the file\nand try again.')
	elif ' ' not in text:
		try:
			text = open(text+'.txt').read()
		except:
			print('Failed to open:', text+'.txt', '. Please try again\n')
	else:
		text = str(text)
		break

# preprocesses text
words = text.lower().split()

# get a dictionary of words with their lenghs
words_size = dict()
for word in words:
	words_size[word] = len(word)
#print(words_size)

# sort words by length
words_sorted_by_size = list()
for word,length in words_size.items():
	words_sorted_by_size.append((length, word))
words_sorted_by_size = sorted(words_sorted_by_size, reverse=True)

# print the largest word
print('The largest word is:', words_sorted_by_size[0][1])

# ways to improve:
# add file handeling in systems
# make loops more comprehensive?
# Any exceptions reading file??