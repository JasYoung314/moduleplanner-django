from django.test import SimpleTestCase

# Create your tests here.

class simple_tests(SimpleTestCase):
    
    def test_math(self):
        self.assertEqual(1 + 1, 3)
