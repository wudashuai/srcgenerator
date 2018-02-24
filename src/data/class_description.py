#!/usr/bin/python
# -*- coding: UTF-8 -*-

class ClassDescription:
    def __init__(self, project_path=None, class_name=None,
                 include_files=[], declare_vars=[], attributes=[]):
        self.project_path = project_path
        self.class_name = class_name
        self.include_files = include_files
        self.declare_vars = declare_vars
        self.attributes = attributes

    def set_project_path(self, project_path):
        self.project_path = project_path

    def get_project_path(self):
        return self.project_path

    def set_class_name(self, class_name):
        self.class_name = class_name

    def get_class_name(self):
        return self.class_name

    def set_include_files(self, include_files):
        self.include_files = include_files

    def get_include_files(self):
        return self.include_files

    def set_declare_vars(self, declare_vars):
        self.declare_vars = declare_vars

    def get_declares_vars(self):
        return self.declare_vars

    def set_attributes(self, attributes):
        self.attributes = attributes

    def get_attributes(self):
        return self.attributes


'''
if __name__ == '__main__':
    project_path = 'src'
    class_name = 'ClassDescription'
    include_files = ['vector', 'string', 'class_description.h']
    declare_vars = ['AttributeDescription']
    attributes = ['project_path', 'class_name', 'include_files', 'declare_files', 'attributes']

    class_description = ClassDescription(project_path, class_name, include_files, declare_vars, attributes)

    print(class_description.get_attributes())
    print(class_description.get_class_name())
    print(class_description.get_include_files())
    print(class_description.get_declares_vars())
    print(class_description.get_project_path())
'''