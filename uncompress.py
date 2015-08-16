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
import gzip
from zipfile import ZipFile
from tarfile import TarFile
from rarfile import RarFile

def zip():
    f = ZipFile(file)
    f.extractall()
    f.close
    
def rar():
    f = RarFile(file)
    f.extractall()
    f.close

def tar():
    f = TarFile(file)
    f.extractall()
    f.close

def bzip():
    zip_file = open(file, 'rb')
    plain_file = bz2.open(finish, 'wb')

    zip_file.writelines(plain_file)

def gzip():
    zip_file = open(file, 'rb')
    plain_file = gzip.open(finish, 'wb')

    zip_file.writelines(plain_file)
