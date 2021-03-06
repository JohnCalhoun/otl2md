#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
""" convert vim outliner files to markdown """

import sys

def count_indent(line):
    """count indentation level
    
    will be used later to create headings/sections"""
    count = 0
    for character in line:
        if character == "\t":
            count += 1
        else:
            return count

def main(argv):
    """convert indentation to heading levels

    body text (i.e. lines starting with ":") are ignored"""
    otl_file = open(argv[1], 'r').readlines()
    output_lines = []
    for line in otl_file:
        if line.strip().startswith(':'):
            output_lines.append(line.strip()[2:])
        else:
            heading = (count_indent(line) + 1) * '#'
            output_lines.append("%s %s" % (
                    heading,
                    line.strip()
                )
            )
    return "\n".join(output_lines)

if __name__ == '__main__':
    print '''<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
<body>'''
    print(main(sys.argv))
    print '''</body>
</html>'''