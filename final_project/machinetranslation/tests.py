import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):

    def test_null_e2f(self):
        return self.assertEqual(englishToFrench(''), 'Please insert a text')

    def test_null_f2e(self):
        return self.assertEqual(frenchToEnglish(''), 'Please insert a text')
    
    def test_hello_e2f(self):
        return self.assertEqual(englishToFrench('Hello'), 'Bonjour')
    
    def test_bonjour_f2e(self):
        return self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
    
if __name__ == "__main__":
    unittest.main()