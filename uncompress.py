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

change_coding = 'utf-8'

def getpath(file):
    """\
    Get file's path, if failed it will return current working directory's path
    
    file: the name of the file which needs to process
    """
    try:
        return os.path.dirname(file)
    except:
        return '.'
    

def zip_with_coding(zf_file):
    name_list = zf_file.namelist()
    dir_set = set()
    
    name_tran_list = [ item.encode(change_coding).decode('utf-8') for item in name_list ]
    for name_temp in name_tran_list:
        dir_set.add( os.path.dirname(name_temp) )
    
    for dirname in dir_set:
        try:
            os.makedirs(dirname)
        except:
            pass
        
    for number in list( range(len(name_list)) ):
        content = zf_file.read( name_list[number] )
        try:
            with open( name_tran_list[number], 'wb' ) as f:
                f.write(content)
        except:
            pass
    
def zip(file):
    f = ZipFile(file)
    if True:
        f.extractall(path = getpath(file))
        f.close()
    else:
        zip_with_coding(f)
    
def rar(file):
    f = RarFile(file, charset = change_coding)
    f.extractall(path = getpath(file))
    f.close()

def tar(file):
    f = TarFile(file, encoding = change_coding)
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
