import unittest
from  selenium import webdriver

class TestOp(unittest.TestCase):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def setUp(self):
        pass

    def test_opera(self):
        pass



    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()