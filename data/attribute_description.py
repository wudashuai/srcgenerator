#!/usr/bin/python
# -*- coding: UTF-8 -*-

class AttributeDescription:
    def __init__(self, attr_name=None, attr_type=None, is_base_type=False, is_vector=False):
        self.attr_name = attr_name
        self.attr_type = attr_type
        self.is_base_type = is_base_type
        self.is_vector = is_vector

    def set_attr_name(self, attr_name):
        self.attr_name = attr_name

    def get_attr_name(self):
        return self.attr_name

    def set_attr_type(self, attr_type):
        self.attr_type = attr_type

    def get_attr_type(self):
        return self.attr_type

    def set_is_base_type(self, is_base_type):
        self.is_base_type = is_base_type

    def get_is_base_type(self):
        return self.is_base_type

    def set_is_vector(self, is_vector):
        self.is_vector = is_vector

    def get_is_vector(self):
        return self.is_vector

'''
if __name__ == '__main__':
    attr_name = 'attr_name'
    attr_type = 'string'
    is_base_type = True

    attribute_description = AttributeDescription(attr_name, attr_type, is_base_type)
    attribute_description.set_is_vector(True)

    print(attribute_description.get_attr_name())
    print(attribute_description.get_attr_type())
    print(attribute_description.get_is_base_type())
    print(attribute_description.get_is_vector())
'''