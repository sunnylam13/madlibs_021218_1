# -*- coding: utf-8 -*-

#! python3
# ! /usr/local/Cellar/python3/3.6.1

# USAGE
# python3 madlibs_021218_1.py <filename or file path>

import sys, re

#####################################
# REGEX
#####################################

# regex
# VERB? - https://regexr.com/3kqam
# https://regexr.com/3kqbe

adjectiveRegex = re.compile(r'\b(ADJECTIVE)')
nounRegex = re.compile(r'\b(NOUN)')
adverbRegex = re.compile(r'\b(ADVERB)')
verbRegex = re.compile(r'\b(VERB)')

adjectiveRegex_2 = re.compile(r'\b(ADJECTIVE)([\.\?\!\,\;\"\'])')
nounRegex_2 = re.compile(r'(\b(NOUN)([\.\?\!\,\;\"\']))')
adverbRegex_2 = re.compile(r'\b(ADVERB)([\.\?\!\,\;\"\'])')
verbRegex_2 = re.compile(r'\b(VERB)([\.\?\!\,\;\"\'])')

txtEndStripRegex = re.compile(r'(\.txt)$')

#####################################
# END REGEX
#####################################

# access a specific text file
# text file is supplied as an argument at runtime
# read the text file and/or copy it

madlib_file = open(sys.argv[1],'r') # open the file in read mode
# print("Printing variable madlib_file") # for testing
# print(madlib_file) # for testing

# temp_file = madlib_file.readlines() # results in a string with ASCII \n carriage return breaks

# join all the lines into one long string so you can break it down into words for analysis

myOneStringFile = []
for line in madlib_file:
	# print(line) # for testing
	myOneStringFile.append(line)

# print("Printing variable myOneStringFile") # for testing
# print(myOneStringFile) # for testing

# turn the list of lines into a single string for breakdown

myOneStringFile_2 = ' '.join(myOneStringFile)

# print("Printing variable myOneStringFile_2") # for testing
# print(myOneStringFile_2) # for testing

# break the combined super string into words

wordBrkFile = myOneStringFile_2.split() # this results in a list like ['check', 'mate', 'bloke']
# print("Printing variable wordBrkFile") # for testing
# print(wordBrkFile) # for testing

# replace all instances of ADJECTIVE, NOUN, ADVERB, VERB with user inputted words in the order they appear in the text
# since the data is supplied as a string this should be easier

remadeWordList = []

# user_inWord = "" # define user_inWord as a string before looping

def change_word(regex,new_word,old_word):
	return regex.sub(new_word,old_word)
	# return regex.sub("" + new_word + "\1",old_word) # to account for ".", ",", "?", "!", etc.

def add_quotes(word):
	return "'" + word + "'"

print("Please enter your words with quotes ("")")

for word in wordBrkFile:
	user_inWord = "" # define user_inWord as a string before looping
	if adjectiveRegex.search(word):
		# print(adjectiveRegex.search(word)) # for testing
		user_inWord = str(input("Enter an adjective:\n"))
		# print("user_inWord is:  " + user_inWord) # for testing
		remadeWordList.append(change_word(adjectiveRegex,user_inWord,word))
	elif adjectiveRegex_2.search(word):
		user_inWord = str(input("Enter an adjective:\n"))
		# print("user_inWord is:  %s" % user_inWord) # for testing
		remadeWordList.append(change_word(adjectiveRegex_2,user_inWord,word))
	elif nounRegex.search(word):
		user_inWord = str(input("Enter a noun:\n"))
		# print("user_inWord is:  %s" % user_inWord) # for testing
		remadeWordList.append(change_word(nounRegex,user_inWord,word))
	elif nounRegex_2.search(word):
		user_inWord = str(input("Enter a noun:\n"))
		# print("user_inWord is:  %s" % user_inWord) # for testing
		remadeWordList.append(change_word(nounRegex_2,user_inWord,word))
	elif adverbRegex.search(word):
		user_inWord = str(input("Enter an adverb:\n"))
		# print("user_inWord is:  %s" % user_inWord) # for testing
		remadeWordList.append(change_word(adverbRegex,user_inWord,word))
	elif adverbRegex_2.search(word):
		user_inWord = str(input("Enter an adverb:\n"))
		# print("user_inWord is:  %s" % user_inWord) # for testing
		remadeWordList.append(change_word(adverbRegex_2,user_inWord,word))
	elif verbRegex.search(word):
		user_inWord = str(input("Enter a verb:\n"))
		# print("user_inWord is:  %s" % user_inWord) # for testing
		remadeWordList.append(change_word(verbRegex,user_inWord,word))
	elif verbRegex_2.search(word):
		user_inWord = str(input("Enter a verb:\n"))
		# print("user_inWord is:  %s" % user_inWord) # for testing
		remadeWordList.append(change_word(verbRegex_2,user_inWord,word))
	else:
		remadeWordList.append(word) # add the word with no changes

# print("Printing variable remadeWordList") # for testing
# print(remadeWordList) # for testing

# join all of the strings in the `wordBrkFile` or word list file together again

finalWordList = " ".join(remadeWordList)
# print("Printing variable finalWordList") # for testing
# print(finalWordList) # for testing

# print the new version to the screen

print(finalWordList)

# save the new version to a file

finalWordFile = open(txtEndStripRegex.sub('_final.txt',sys.argv[1]),'w') # remove the .txt from the ending of the inputted file name, add `_final.txt` instead...  if the file doesn't exist it will be created

# write the data from the finalWordList to the finalWordFile

finalWordFile.write(finalWordList)

# close file

madlib_file.close() # close the input file
finalWordFile.close() # close the new file

#####################################
# DOCUMENTATION
#####################################

# reads text files
# lets user add own text anywhere the word ADJECTIVE, NOUN, ADVERB, VERB appear
# program finds instances and asks user to replace them as they appear
# result should be printed to screen
# result should be saved to a new text file

# test data
# madlibs_data_021218_1.txt

# regex
# strip .txt - https://regexr.com/3kobs

# References
# https://stackoverflow.com/questions/16922214/reading-a-text-file-and-splitting-it-into-single-words-in-python
# http://www.dreamincode.net/forums/topic/19504-reading-text-file-word-by-word-in-python/
# https://www.afterhoursprogramming.com/tutorial/python/reading-files/
# https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
# https://www.tutorialspoint.com/python3/list_append.htm
# https://stackoverflow.com/questions/36094979/convert-a-list-of-strings-into-one-string
# https://stackoverflow.com/questions/36787345/how-to-convert-user-input-to-string-in-python-2-7
# https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3

#####################################
# END DOCUMENTATION
#####################################