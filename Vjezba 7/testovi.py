import unittest
import cap

class TestCap(unittest.TestCase):
    def test_one_word(self):
        self.assertEqual(cap.cap_text('python'), 'Python')
    def test_multiple_words(self):
        self.assertEqual(cap.cap_text('monty python'), 'Monty python')
    
    def test_sabiranje(self):
        self.assertEqual(cap.cap_saberi(5,4), 9)

if __name__ == '__main__':
    unittest.main()