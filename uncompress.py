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
import bz2
import gzip as gz
from zipfile import ZipFile
from tarfile import TarFile
from rarfile import RarFile

is_posix = False

def getpath(file):
    """\
    Get file's path, if the platform is not POSIX-compliant then return current working directory's path
    
    file: the name of the file which needs to process
    """
    
    if is_posix:
        name_list = file.split('/')
        return '/'.join( name_list[ :len(name_list)-1] )
    else:
        return '.'
    
def zip(file):
    f = ZipFile(file)
    f.extractall(path = getpath(file))
    f.close()
    
def rar(file):
    f = RarFile(file)
    f.extractall(path = getpath(file))
    f.close()

def tar(file):
    f = TarFile(file)
    f.extractall(path = getpath(file))
    f.close()

def bzip2(file):
    with bz2.open(file, 'rb') as zip_file:
        with open(file+'.finish', 'wb') as plain_file:
            while True:
                content = zip_file.read(1024)
                if content != b'':
                    plain_file.write(content)
                else:
                    break

def gzip(file):
    with gz.open(file, 'rb') as zip_file:
        with open(file+'.finish', 'wb') as plain_file:
            while True:
                content = zip_file.read(1024)
                if content != b'':
                    plain_file.write(content)
                else:
                    break
