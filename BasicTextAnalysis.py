__author__ = "Zafrin R. Minoti"
__email__ = "zafrin.minoti@gmail.com"
__date__ = "January 10, 2018"
__institution__ = "Galvanize"
__project__ = "Take home assignment - Question 1"

#########################################################################

'''
This is a content analizer. It tekes text files (with .txt extentions) as
input. Then it provides different statistics about the content.
'''

import string

############ Function(s) #############
def frequency_counter(input_list):
    '''
    This function takes a list of words/phrases as input_list
    Counts the frecuncy of unique words/phrases from the list
    Returns a sorted list of tuples with decending frequency
    '''
    counter = dict()
    word_frequency = list()

    for word in input_list:
        counter[word] = counter.get(word,0) + 1

    for word, count in counter.items():
        word_frequency.append( (count, word) )
    word_frequency.sort(reverse=True)

    return(word_frequency)

########################################

######### Get and read file ############
while True:
    filename = input('Enter file url: ')

    # Catching errors and invalid input
    if filename[-4:] != '.txt':
        print('Please enter a valid url of a text file with an extention .txt')
        continue

    else:
        text = open(filename).read()
        break

############ reformat text ############
text = text.replace('\n', ' ')
text = text.replace('  ', ' ')
text = text.lower()

# Create test string without punctuation and with END-OF-SENTENCE indicator
sentence_end_punctuation = ['. ', '? ', '! ']
sentence_end_keyword = ' SENTANCEendPUNC '

plain_text_with_end_punc = text
for punc in sentence_end_punctuation:
    plain_text_with_end_punc = plain_text_with_end_punc.replace(punc, sentence_end_keyword)
for punc in string.punctuation:
    plain_text_with_end_punc = plain_text_with_end_punc.replace(punc,'')

# get plain text of words only
plain_text = plain_text_with_end_punc.replace(sentence_end_keyword, ' ')


############# Text Analysis #############

# Bag of words
bow = plain_text.split()

# list of sentences
sentences = plain_text_with_end_punc.split(sentence_end_keyword)

# Word Count
word_count = len(bow)
unique_word_count = len(set(bow))

# Sentence Count
sentence_count = len(sentences)

# Average words count in a sentence
sentence_length = list()
for sentence in sentences:
    length = len(sentence.split())
    sentence_length.append(length)
sentence_length = sum(sentence_length)/len(sentence_length)

# List of words in order of descending frequency
word_frequency = frequency_counter(bow)

# 3 word phreses
# probably better to use tokenizer fron NLTK
phrases = list()
index = 0
for word in bow:
    phrases.append(' '.join(bow[index:index+3]))
    index +=1
phrases = phrases[:-2]  # gets ris of the last 1 and 2 word phrases

phrase_frequency = frequency_counter(phrases)

########### Print textual statistics ############
print('\nThe text contains: \n\t {} words'.format(word_count))
print('\t {} unique words'.format(unique_word_count))
print('\t {} sentences'.format(sentence_count))
print('\t An average of {} words per sentence'.format(sentence_count))

# Word frequency
if (word_frequency[0][0] > 1):
    print('\nThe 10 most frequent words are:')
    for freq, word in word_frequency[:10]:
        print('\t', freq, word)
else: print('All words in the text has equal frequency.')

print()

# Phrase frequency
if (phrase_frequency[0][0] > 1):
    print('\nThe 10 most frequent words are:')
    for freq, word in phrase_frequency[:10]:
        print('\t', freq, word)
else: print('All phrases in the text has equal frequency.')
