#!/usr/bin/env python

import os


def write_include_file(root, directory_name, base_name):
    md_file = os.path.join(root, base_name + '.include.md')
    if os.path.exists(md_file):
        return
    with open(md_file, 'w') as output:
        content = f"""
##### Context

##### Steps to improve the code

##### UML before and after

![{base_name} - Before](uml/Before/{directory_name}/{base_name}.svg?raw=true)

becomes

![{base_name} - After](uml/After/{directory_name}/{base_name}.svg?raw=true)

##### Code before and after

snippet: RefactoringSamples/Before/{directory_name}/{base_name}.cs

becomes

snippet: RefactoringSamples/After/{directory_name}/{base_name}.cs
"""
        output.write(content)

def generate_missing_include_md_files():
    for root, dirs, files in os.walk("RefactoringSamples/Before"):
        path = root.split(os.sep)
        directory_name = os.path.basename(root)
        print((len(path) - 1) * '---', directory_name)
        for file in files:
            base_name, extension = os.path.splitext(file)
            if extension != '.cs':
                continue
            print(len(path) * '---', file, base_name, extension)
            write_include_file(root, directory_name, base_name)


if __name__ == '__main__':
    generate_missing_include_md_files()
