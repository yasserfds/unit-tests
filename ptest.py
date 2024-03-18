import unittest

def sum(a, b):  # Corrected function name
    return a + b

class SumTest(unittest.TestCase):  # Changed class name to follow naming convention
    def setUp(self):
        print("SETUP Called....")
        self.a = 10
        self.b = 20
    
    def tearDown(self):
        self.a = 0
        self.b = 0
        print("TEARDOWN CALLED....")

    def test_sum(self): 
        print("TEST - 1 Called....")       
        # Act
        result = sum(self.a, self.b)
        # Assert
        self.assertEqual(result, self.a + self.b)
    
    def test_sum_2(self):
        print("TEST - 2 Called....")
        # Act
        result = sum(self.b, self.a)
        # Assert
        self.assertEqual(result, self.a + self.b)
    
if __name__ == "__main__":
    unittest.main()
