from itertools import count
from collections import Counter

FILENAME3 = 'book.txt'
READ_MODE = 'r'
FILENAME4 = "summary.txt"
WRITE_MODE = 'w'

try:
   with open(FILENAME3) as names_file3:
       pass
except IOError as error:
   print(f'Unable to open file {FILENAME3}. Error message: {error}')
print('After the handling code, program keeps running')
wordlist = []
names_file3 = open(FILENAME3,READ_MODE)
names_file4 = open(FILENAME4,WRITE_MODE)
with names_file3, names_file4:
    for word in names_file3:
       wordlist  += word.split()
    #convert list to string
    text = ' '.join([str(elem) for elem in wordlist])

    # Total count of words 
    no_special_character= text.translate({ord(c): " " for c in "!@#$%'^&*”;—:,.'“’/<>?\|`~-=_+"})
    word_count = no_special_character.split()
    print(f'Total words count: {len(word_count)}')
    names_file4.write(f'Total words count: {len(word_count)}\n')

    #Number of characters in this string
    character_count = 0
    for char in text:
        character_count +=1
    print(f'Total character count: {character_count}')
    names_file4.write(f'Total character count: {character_count}\n')
    #Average word length in this string
    average_word = sum(len(word)for word in word_count)/len(word_count)
    print(f'The average word length: {average_word:.2f}')
    names_file4.write(f'The average word length: {average_word:.2f}\n')
    #Average sentence length in this string
    sentence = text.split('.')
    average_sentence = sum(len(i)for i in sentence)/len(sentence)
    print(f'The average sentence length: {average_sentence:.2f}')
    names_file4.write(f'The average sentence length: {average_sentence:.2f}\n')
  
    #Word distribution of words ending in ly
    words_ly = [word_count for word_count in text.split() if word_count.endswith("ly")]
    print(f'A word distribution of all words ending in "ly":')
    names_file4.write(f'A word distribution of all words ending in "ly":\n')
    for ab in words_ly:
        print(f'{ab:<15} : {words_ly.count(ab)}')
        names_file4.write(f'{ab:<15} : {words_ly.count(ab)}\n')

    #Top ten longest words

    Ten_large = 10
    longest = count()
    longest_word = sorted(word_count, key=lambda w: (len(w),next(longest)),reverse=True)[:Ten_large]
    print(longest_word)
    names_file4.write(f'List of top 10 longest words:{longest_word}')

