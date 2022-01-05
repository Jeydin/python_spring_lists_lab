from wordStats import *

def getNumWordsWithNVowels(wordlist, num):
	counter = 0
	for word in wordlist:
		if numVowels(word) == num:
			counter += 1
	return counter

def getNumWordsOfLengthN(wordlist, length):
	counter = 0
	for word in wordlist:
		if len(word) == length:
			counter += 1
	return counter

def getAvgWordLength(wordlist):
  counter = 0
  characters = 0
  while counter < len(wordlist):
    characters += len(wordlist[counter])
    counter += 1
  average = characters/len(wordlist)
  return average

def removeWordsOfLengthN(wordlist, length):
  removedlist = []
  counter = 0
  while counter < len(wordlist):
    if len(wordlist[counter]) == length:
      removedlist.append(wordlist[counter])
      wordlist.remove(wordlist[counter])
    counter += 1
  return removedlist

def getNumVowelsInList(wordlist):
  counter = 0
  vowels = 0
  while counter < len(wordlist):
    vowels += numVowels(wordlist[counter])
    counter += 1
  return vowels