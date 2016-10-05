STOPS = ['P', 'B', 'T', 'D', 'K', 'G']
AFFRICATES = ['CH', 'JH']
FRICATIVES = ['F', 'V', 'TH', 'DH', 'S', 'Z', 'SH', 'ZH', 'HH']
NASALS = ['M', 'EM', 'N', 'EN', 'NG', 'ENG']
LIQUIDS = ['L', 'EL', 'R', 'DX', 'NX']
SEMIVOWELS = ['Y', 'W', 'Q']

MONOPHTHONGS = ['AO', 'AA', 'IY', 'UW', 'EH', 'IH', 'UH', 'AH', 'AX', 'AE']
DIPHTHONGS = ['EY', 'AY', 'OW', 'AW', 'OY']
RCOLORED = ['ER', 'AXR', 'EHR', 'UHR', 'AOR', 'AAR', 'IHR', 'IYR', 'AWR']

CONSONANTS = STOPS + AFFRICATES + FRICATIVES + NASALS + LIQUIDS + SEMIVOWELS
VOWELS = MONOPHTHONGS + DIPHTHONGS + RCOLORED

LONG_VOWELS = ['EY', 'IY', 'AY', 'OW', 'UW']
SHORT_VOWELS = ['AE', 'EH', 'IH', 'AA', 'AH', 'ER']

NORMAL_CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
NORMAL_CONSONANT_DIGRAPHS = ['bl', 'br', 'ch', 'ck', 'cl', 'cr', 'dr', 'fl', 'fr', 'gh', 'gl', 'gr', 'ng', 'ph',  'th', 'tr', 'tw', 'wh', 'wr', 'lv']
NORMAL_CONSONANT_TRIGRAPHS = ['nth', 'sch', 'shr', 'spl', 'spr', 'squ', 'str', 'thr']