"""Importing libraries/packages"""
# To do unit testing
import unittest
# To import program as a module
import program as script


class TestProgram(unittest.TestCase):
    def test_navigate_directory(self):
        self.assertEqual(script.navigate_directory("Downloads"), "C:\\Users\\User\\Downloads")
        self.assertEqual(script.navigate_directory("Screenshots"),
                         "C:\\Users\\User\\OneDrive\\Pictures\\Screenshots")
        self.assertEqual(script.navigate_directory("OneDrive - CSULB"), "C:\\Users\\User\\OneDrive - CSULB")
        self.assertEqual(script.navigate_directory("Samsung S21"),
                         "C:\\Users\\User\\OneDrive\\Pictures\\Phone Photos & Videos\\Samsung S21")

    def test_organizing_files(self):
        pass

    def test_removing_files(self):
        pass

    def test_copying_files(self):
        pass


if __name__ == '__main__':
    unittest.main()
