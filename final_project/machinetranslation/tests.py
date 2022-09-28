import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_null_e2f(self):
        return self.assertEqual(english_to_french(''), 'Please insert a text')

    def test_null_f2e(self):
        return self.assertEqual(french_to_english(''), 'Please insert a text')
    
    def test_hello_e2f(self):
        return self.assertEqual(english_to_french('Hello'), 'Bonjour')
    
    def test_bonjour_f2e(self):
        return self.assertEqual(french_to_english('Bonjour'), 'Hello')
    
if __name__ == "__main__":
    unittest.main()