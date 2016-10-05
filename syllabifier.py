import re
import alphabet as a
from nltk.corpus import cmudict

#creates ipa_word-to-arpabet dictionary
arpabet = cmudict.dict()

def is_vowel(token):
	if re.sub('(0|1|2)', '', token) in a.VOWELS:
		return True
	else:
		return False

def is_consonant(token):
	if not(re.sub('(0|1|2)', '', token) in a.VOWELS):
		return True
	else:
		return False

def is_long_vowel(token):
	if re.sub('(0|1|2)', '', token) in a.LONG_VOWELS:
		return True
	else:
		return False

def is_short_vowel(token):
	if re.sub('(0|1|2)', '', token) in a.SHORT_VOWELS:
		return True
	else: 
		return False

def has_same_double_consonant(word):
	for i in range(len(word)):
		if i < len(word) - 1 and word[i] in a.NORMAL_CONSONANTS and word[i] == word[i+1]:
			return word[i]
	return False

def syllabifier(word):
	#gets arpabet IPA transcription of the ipa_word
	ipa_word = arpabet[word][0]
	syllables = []
	
	for i, token in enumerate(ipa_word):
		#seperating between double consonants (that are not consonant digraphs) like kit-ten or pil-grim
		if 0 < i < len(ipa_word) - 1 and is_consonant(token) and is_vowel(ipa_word[i-1])  and (has_same_double_consonant(word) == token.lower() or is_consonant(ipa_word[i+1])):
			if has_same_double_consonant(word) != False:
				if not syllables:
					syllables.append(ipa_word[:i+1])
					syllables.append(ipa_word[i:])
				else:
					syllables.append(ipa_word[i:])
			else:
				if not syllables:
					syllables.append(ipa_word[:i+1])
					syllables.append(ipa_word[i+1:])
				else:
					syllables.append(ipa_word[i:])			
		if 0 < i < len(ipa_word) - 1 and (is_consonant(token) and is_short_vowel(ipa_word[i-1]) and is_vowel(ipa_word[i+1]) and not has_same_double_consonant(word)) or re.sub('(0|1|2)', '', token) == 'ER':
			if not syllables:
				syllables.append(ipa_word[:i+1])
				syllables.append(ipa_word[i+1:])
			else:
				syllables.append(ipa_word[i+1:])
		if 0 < i < len(ipa_word) - 1 and is_consonant(token) and is_long_vowel(ipa_word[i-1]) and is_vowel(ipa_word[i+1]) and i != len(ipa_word) - 2:
			if i == len(ipa_word) - 3 and word.endswith('le'):
				if not syllables:
					syllables.append(ipa_word[:len(ipa_word)-2])
					syllables.append(ipa_word[len(ipa_word)-2:])
				else:
					syllables.append(ipa_word[len(ipa_word)-2:])
			else:
				if not syllables:
					syllables.append(ipa_word[:i])
					syllables.append(ipa_word[i:])
				else:
					syllables.append(ipa_word[i:])
		if i == len(ipa_word) - 1 and word.endswith('ckle'):
			if not syllables:
				syllables.append(ipa_word[:len(ipa_word)-2])
				syllables.append(ipa_word[len(ipa_word)-2:])
			else:
				syllables.append(ipa_word[len(ipa_word)-2:])
		if i == len(ipa_word) - 1 and word.endswith('le') and word[len(word)-3] != 'k' and is_consonant(ipa_word[len(ipa_word)-3]):
			if not syllables:
				syllables.append(ipa_word[:len(ipa_word)-2])
				syllables.append(ipa_word[len(ipa_word)-2:])
			else:
				syllables.append(ipa_word[len(ipa_word)-2:])
	#if the word is indivisible add the entire word to syllable list
	if not syllables:
		syllables.append(ipa_word)	
	#removes duplicates and empty syllables
	for i, syllable in enumerate(syllables):
		if i < len(syllables) - 1 and syllables[i+1] == syllable:
			del syllables[i]
		if not syllable:
			del syllables[i]		
	#cleans up the thing
	rev = syllables[::-1]
	for i,syllable in enumerate(rev):
		for j, token in enumerate(syllables):
			if 0 < j < len(syllables) - 1 and syllable[len(token) - len(syllable):] == token:
				if has_same_double_consonant(word) != False:
					 = [:(len(token) - len(syllable)) + 1]
				else:
					 = [:len(rev[i+1]) - len(syllable)]

	return syllables

print syllabifier('combination')
