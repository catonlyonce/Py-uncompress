#!/usr/bin/env python3
# written by @天猫__ 

def filetype_detect(file):

    file_types = {
            "zip": [80, 75, 3, 4],
            "gzip": [31, 139, 8],
            "bzip2": [66, 90, 104],
            "rar": [82, 97, 114, 33, 26, 7, 0]
            }

    """    Detect the type of the file which is compressed.

    file: file's path
    """

    
    try:
        with open(file, 'rb') as dest_file:
            header = [ x for x in list( dest_file.read(7)) ]

            for filetype in file_types:
                if header[ :len( file_types[filetype] )] == file_types[filetype]:
                    return filetype

            #file may be tar
            dest_file.seek(257, 0)
            if dest_file.read(5) == 'ustar':
                return 'tar'
    except:
        pass
    
    return None
