from wordListStats import *

wordlist = ["one", "two", "three", "four", "five", "six", "seven", "alligator"] 

print(getNumWordsWithNVowels(wordlist, 2))

print(getNumWordsOfLengthN(wordlist, 3))

print(getAvgWordLength(wordlist))

print(removeWordsOfLengthN(wordlist, 3))

print(getNumVowelsInList(removeWordsOfLengthN(wordlist, 3)))