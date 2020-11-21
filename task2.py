FILENAME3 = 'book.txt'
READ_MODE = 'r'
FILENAME6 = "summary2.txt"
WRITE_MODE = 'w'
try:
   with open(FILENAME3) as names_file3:
       pass
except IOError as error:
   print(f'Unable to open file {FILENAME3}. Error message: {error}')
print('After the handling code, program keeps running')
wordlist= []
names_file3 = open(FILENAME3,READ_MODE)
names_file6 = open(FILENAME6,WRITE_MODE)
with names_file3, names_file6:
   for character in names_file3:
       wordlist += character
 
   wordlist = [letter.upper() for letter in wordlist]
       
   character_count = {}
   alpha = list(map(chr,range(65,91)))
   #count each occurrences of each unique word
   for word in wordlist:
       if word in character_count:
           character_count[word] += 1 #update existing key-value pair
       else:
           character_count[word] = 1 #insert new key-value pair
   word_count = 0
   for word, count in sorted(character_count.items()):
       if word in alpha:
           print(f'{word:<2}{count}')
           names_file6.write(f'{word:<2}{count}')
           word_count +=1
      
   if word_count != 26:
       print('It doesn’t have all letters')
       names_file6.write('It doesn’t have all letters')
   else:
       print('It has all letters')
       names_file6.write('It has all letters')
      
 

