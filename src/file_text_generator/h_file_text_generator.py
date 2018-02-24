#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
// H_FILE_PART1
#ifndef SRC_FILETEXTGENERATOR_HFILEGENERATOR_H_
#define SRC_FILETEXTGENERATOR_HFILEGENERATOR_H_

#include <string>
#include "h_file_text_generator.h"

using namespace std;

class HFileTextGenerator
{
// H_FILE_PART2
private:
    int _size;
    string _fileText;

public:
    HFileTextGenerator();
    HFileTextGenerator(const HFileTextGenerator& rhs);
    HFileTextGenerator& operator=(const HFileTextGenerator& rhs);
    ~HFileTextGenerator();

    void setSize(int size);
    int getSize() const;

    void setFileText(const string& fileText);
    string& getFileText();
    const string& getFileText() const;

// H_FILE_PART3
};

#endif

'''
NEW_LINE = '\n'

class HFileTextGenerator:
    def __init(self, class_description=None):
        self.class_description = class_description

    def generate_h_file_text(self):
        h_file_text = ''

        h_file_text = self.generate_h_file_part1()
        h_file_text += self.generate_h_file_part2()
        h_file_text += self.generate_h_file_part3()

        return h_file_text

    def generate_h_file_part1(self):
        h_file_part1 = ''

        return h_file_part1

    def generate_h_file_part2(self):
        h_file_part2 = ''

        return h_file_part2

    def generate_h_file_part3(self):
        h_file_part3 = ''

        h_file_part3 += '};'
        h_file_part3 += NEW_LINE + NEW_LINE
        h_file_part3 += '#endif'
        h_file_part3 += NEW_LINE

        return h_file_part3


if __name__ == '__main__':
    h_file_text_generator = HFileTextGenerator()
    print(h_file_text_generator.generate_h_file_part3())
