import unittest
from MagicData import *

class dataTests(unittest.TestCase):

	def setUp(self):
		self.md = MagicData('common/AllSets-x.json')
	def testCreateMDObject(self):
		self.assertTrue(self.md.json_path == 'common/AllSets-x.json')

	def testLoadJSONData(self):
		self.md.load_json()
		self.assertTrue(self.md.data != None)

	def testLoadKeywords(self):
		self.md.load_keywords('keyword-density/keywords.txt')
		self.assertTrue(self.md.keywords != None)

	def testLoadSets(self):
		self.md.load_sets('common/core_sets.txt')
		self.assertTrue(self.md.sets != [])

	def testRemoveReminderText(self):
		s = 'Hello (World)'
		s_clean = self.md.remove_reminder_text(s)
		self.assertTrue(s_clean == 'Hello ')

	def testRemoveUnicodeChars(self):
		s = u'Hello\u2014 World'
		s_clean = self.md.remove_unicode_chars(s)
		self.assertTrue(s_clean == 'Hello World')

	def testRemoveNumericChars(self):
		s = 'Hello  1234World'
		s_clean = self.md.remove_numeric_chars(s)
		self.assertTrue(s_clean == 'Hello World')

def main():
	unittest.main()

if __name__ == '__main__':
	main()