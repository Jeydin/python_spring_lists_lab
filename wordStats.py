def numVowels(word):
  vowels = "aeiouAEIOU"
  counter = 0
  for let in word:
    if vowels.find(let) != -1:
     counter += 1
  return counter

def numConsonants(word):
	return len(word) - numVowels(word)