#!/usr/bin/env python3
#
# Copyright 2015 Guanrenfu
#
# Licensed under the Apache License, Version 2.0 (the License); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at 
# 
#     http://www.apache.org/licenses/LICENSE-2.0 
# 
# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an AS IS BASIS, 
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
# See the License for the specific language governing permissions and 
# limitations under the License. 

def help():

    print('''
Py-uncompress 1.3.0

Usage: Py-uncompress [options] [file]
uncompress files using Python

Supported file types:
Type: rar, tar, zip, bzip2, gzip


Options:
 
 --help                     show this message
 --version                  show the version
 -f [file1 file2...]        seclect the file(s) to uncompress


Please report bugs to <https://www.github.com/Guanrenfu/Py-uncompress>
''')
