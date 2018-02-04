'''
	This program takes a string or a text file as input
	and finds the largest word in the document.
	it prints out the word in console.
'''

# Get Text and haldel possible errors
while True:
	text = input('Please enter a string or name/path of a text document:\n\t')

	#ideal - .txt file in with the (.txt) extension
	if text[-4:] == '.txt':
		try:
			text = open(text).read()
			break
		except:
			print('Could not read the file.\nPlease check the destination of the file\nand try again.')
	# in case user put non-text file
	elif '.' in list(text):
		print('That does not looks like a text file.')
		continue
	# In case user forgot the .txt extension
	elif ' ' not in text:
		try:
			text = open(text+'.txt').read()
			break
		except:
			print('Failed to open:', text+'.txt', '. Please try again\n')
		continue
	# if user input was a string
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
# make loops more comprehensive?
# Any exceptions reading file??
# filter only for words... 
	# no hypens, symbols, sequence of numbers, etc