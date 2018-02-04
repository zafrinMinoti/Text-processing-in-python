# Get Text
text = 'My Name is Zafrin'

# preprocesses text
words = text.lower().split()

# get a dictionary of words with their lenghs
words_size = dict()
for word in words:
	words_size[word] = len(word)
print(words_size)

# sort words by length
words_sorted_by_size = list()
for word,length in words_size.items():
	words_sorted_by_size.append((length, word))
words_sorted_by_size = sorted(words_sorted_by_size, reverse=True)

# print the largest word
print('The largest word is:', words_sorted_by_size[0][1])