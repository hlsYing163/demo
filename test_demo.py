'''
Author: your name
Date: 2020-09-06 10:34:08
LastEditTime: 2020-09-06 10:47:33
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \demo\test_demo.py
'''
import unittest
from demo import  user

class Tests(unittest.TestCase):
    def test_d(self):
        self.assertEqual(user(1,2,3),5)
        self.assertEqual(user(1,-2,3),1)        
        self.assertEqual(user(3,-1,3),0)


if __name__ == '__main__':
    unittest.main()