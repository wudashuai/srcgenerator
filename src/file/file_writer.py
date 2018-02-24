#!/usr/bin/python
# -*- coding: UTF-8 -*-

class FileWrite:
    def __init__(self, src_file=None):
        self.src_file = src_file

    def write_file_text(self, file_text):
        fp = open(self.src_file, 'a+')
        fp.write(file_text)




'''
from file_reader import *

if __name__ == '__main__':
    file_reader = FileReader('E:/srcgenerator/file/file_writer.py')
    file_text = file_reader.read_file_text()
    file_write = FileWrite('E:/srcgenerator/file/file_writer.py.bak')
    file_write.write_file_text(file_text)
'''