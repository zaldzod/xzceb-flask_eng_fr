'''Test cases for function units'''
from unittest import TestCase
import machinetranslation
from machinetranslation import translator


class translator(TestCase):
    '''Class test cases'''

    def null_input_french(self):
        '''Test to determine that function parameter is not null'''
        self.assertNotEqual(None, type(self.french_to_english()))

    def null_input_english(self):
        '''Test to determine that function parameter is not null'''
        self.assertNotEqual(None, type(self.english_to_french()))

    def test_word_translation(self):
        '''Test to translate from English to French'''
        self.assertEqual(self.french_to_english('Bonjour'), 'Hello')

    def test_word_translation(self):
        '''Test to translate from French to English'''
        self.assertEqual(self.english_to_french('Hello'), 'Bonjour')


