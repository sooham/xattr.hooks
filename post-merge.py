#!/usr/local/bin/python
# post-merge hook

import re
import subprocess

pattern_header = re.compile('([\S]+): ([\S]+):')

with open('.metadata') as metadata:
    data, file_name, attribute_name = '', None, None

    for line in metadata:
        header_match = pattern_header.match(line)
        if header_match and data:
            # we have reached a new file
            # store old data and start collecting for new file
            subprocess.call(["xattr", "-wx", attribute_name, data, file_name])
            data = ''
            file_name, attribute_name = header_match.group(1, 2)

        elif header_match:
            file_name, attribute_name = header_match.group(1, 2)
        else:
            # still collecting data for previous file
            data += line

    subprocess.call(["xattr", "-wx", attribute_name, data, file_name])
