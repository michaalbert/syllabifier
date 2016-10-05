	def strip_prefixes(word):

	for prefix in a.PREFIXES:
		res = []
		if word.startswith(prefix):
			return [prefix]+strip_prefixes(re.split(prefix, word)[-1])
	res.append(word)		
	return res

def strip_suffixes(word):
	for suffix in a.SUFFIXES:
		res = []
		if word.endswith(suffix):
			return strip_suffixes(re.split(suffix, word)[-1])+[suffix]		
	return res

	#strip prefixes
	syllables += strip_prefixes(word)[:-1]
	#strip suffixes
	syllables += strip_suffixes(word)
	#remaining word
	rest = re.sub(''.join(strip_suffixes(word)), '' ,strip_prefixes(word)[-1])
	print rest

	#make normal word a list of arpabet tokens
    rest = arpabet[word]

		for i, token in enumerate(rest):
			#seperating between double consonants that are not consonant digraphs
			if i < len(rest) - 1 and is_consonant(token) and is_consonant(rest[i+1]) and not rest[i:i+2] in a.CONSONANT_DIGRAPHS:
				#differentiating where to insert new syllable depending on presence of suffixes
				if not strip_suffixes(word):
					syllables.append(rest[:i+1])
					syllables.append(rest[i+1:])
					#change later so that the syllable atfer the consonant 
					#is syllabified if necessary (rekursion wie bei strip prefixes)
					return syllables
				else:
					syllables.insert(-1, rest[:i+1])
					syllables.insert(-1, rest[i+1:])
					#siehe oben
					return syllables

			if 0 < i < len(rest) - 1 and is_consonant(token) and is_vowel(rest[i-1]) and is_vowel(rest[i+1]):
				if is_short_vowel(rest[i-1]):
					
		return syllables