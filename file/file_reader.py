#!/usr/bin/python
# -*- coding: UTF-8 -*-

class FileReader:
    def __init__(self, src_file=None):
        self.src_file = src_file

    def read_file_text(self):
        fp = open(self.src_file, 'r')
        file_text = fp.read()
        return file_text





'''
if __name__ == '__main__':
    file_reader = FileReader('E:/srcgenerator/file/file_reader.py')
    print(file_reader.read_file_text())
'''