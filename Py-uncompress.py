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
import sys

#Python version check
if sys.version_info.major < 3:
    print('Please use Python 3(at least) to run the program.')
    sys.exit(1)

import os
import howto
import filetype
import uncompress

return_value = 0
        
if len(sys.argv) == 1:
    howto.help()
    sys.exit(2)

if sys.argv[1] == '--help':
    howto.help()
    sys.exit(0)

if sys.argv[1] == '--version':
    print('Py-compress: version: 1.3.0')
    sys.exit(0)


try:
    select = sys.argv.index('-f')

except ValueError:
    print('Error: Missing -f options')
    sys.exit(3)


files = sys.argv[select + 1: ]

if os.name == 'posix':
    uncompress.is_posix = True

for file in files:
    if os.path.isfile(file) == False:
        print('Error: No such file or it is a directory.')
        sys.exit(4)


    try:
        exec("uncompress."+filetype.filetype_detect(file)+"('"+file+"')")
    except:
        print('Error: The type of the file '+file+' doesn\'t supported.')
        return_value = 5

sys.exit(return_value)
