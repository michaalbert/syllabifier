import unittest
import syllabifier as sy
#import arpabet_to_text as arp 

class TestSequence(unittest.TestCase):

	def test_is_vowel(self):
		self.assertTrue(sy.is_vowel('AE'))
		self.assertFalse(sy.is_vowel('P'))

	def test_is_consonant(self):
		self.assertTrue(sy.is_consonant('NG'))
		self.assertFalse(sy.is_consonant('IY'))

	def test_is_long_vowel(self):
		self.assertTrue(sy.is_long_vowel('OW'))
		self.assertFalse(sy.is_long_vowel('EH'))

	def test_is_short_vowel(self):
		self.assertTrue(sy.is_short_vowel('IH'))
		self.assertFalse(sy.is_short_vowel('AY'))

	def test_has_same_double_consonant(self):
		self.assertEqual(sy.has_same_double_consonant('suffer'), 'f')
		self.assertFalse(sy.has_same_double_consonant('pilgrim'))

	def test_syllabifier(self):
		#dividing along double consonants
		self.assertEqual(sy.syllabifier('kitten'), [[u'K', u'IH1', u'T'], [u'T', u'AH0', u'N']])
		self.assertEqual(sy.syllabifier('pilgrim'), [[u'P', u'IH1', u'L'], [u'G', u'R', u'AH0', u'M']])
		#dividing when consonant surrounded by vowels, first vowel is short
		self.assertEqual(sy.syllabifier('metal'), [[u'M', u'EH1', u'T'], [u'AH0', u'L']])
		#dividing when consonant surrounded by vowels, first vowel is long
		self.assertEqual(sy.syllabifier('bacon'), [[u'B', u'EY1'], [u'K', u'AH0', u'N']])
		#dividing before the 'le' for words ending with 'ckle'
		self.assertEqual(sy.syllabifier('fickle'), [[u'F', u'IH1', u'K'], [u'AH0', u'L']])
		#not dividing when words end with 'le', vowel before le
		self.assertEqual(sy.syllabifier('ale'), [[u'EY1', u'L']])
		#dividing when words end with 'le', consonant before le
		self.assertEqual(sy.syllabifier('fable'), [[u'F', u'EY1', u'B'], [u'AH0', u'L']])
		#testing for longer words
		self.assertEqual(sy.syllabifier('assassin'), [[u'AH0', u'S'], [u'S', u'AE1', u'S'], [u'S', u'AH0', u'N']])
		self.assertEqual(sy.syllabifier('combination'), [[u'K', u'AA2', u'M'], [u'B', u'AH0', u'N'], [u'EY1'], [u'SH', u'AH0', u'N']])

if __name__ == '__main__':
	unittest.main()
