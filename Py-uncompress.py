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
import os
import sys
import howto
import filetype
import uncompress

        
if len(sys.argv) == 1:
    howto.help()
    sys.exit(1)

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
    sys.exit(1)


file = sys.argv[select + 1]

if os.path.isfile(file) == False:
    print('Error: No such file or it is a directory.')
    sys.exit(1)


try:
    exec("uncompress."+filetype.filetype_detect(file)+"('"+file+"')"
except:
    print('Error: This type doesn\'t supported.')
