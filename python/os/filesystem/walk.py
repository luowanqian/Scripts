# -*- coding: UTF-8 -*-

"""
遍历目录，输出目录下所有子目录以及文件
"""

import os


if __name__ == '__main__':
    root_dir = '/tmp/test'
    for root, dirs, files in os.walk(root_dir, topdown=True):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
