'''
Author: your name
Date: 2020-09-06 10:20:13
LastEditTime: 2020-09-06 10:30:03
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \demo\demo.py
'''


def user(x, w, b):
    y = x*w + b
    y = max(0, y)
    return y


if __name__ == '__main__':
    print(f"user(4,1,4):{user(4,1,3)}")
