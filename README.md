![Supported OS](https://img.shields.io/badge/Supported%20OS-All-blue.svg)
![Supported Python versions](https://img.shields.io/badge/Python-3.4-brightgreen.svg)
![License](https://img.shields.io/hexpm/l/plug.svg)
# Py-uncompress
A program that can uncompress files use Python3<br>
<br>

## Installation
Because this is a Python3 Program, so first you need to install Python3.<br>
<br>
## Basic Usage
**Extract file(s)**: Py-uncompress.py -c [character set] -f [file1 file2 ...]<br>
<br>
To get more up-to-date information, you can use the command: *Py-uncompress.py --help*
<br>
## New Features
**Add**: Multi-file processing<br>
**Add**: Extract files to their original paths<br>
**Add**: Try to solve character set problem (**support is experimental, and zip file is not supposed**)<br>
**Fix**: Some bugs<br>
<br>
## Value of process's exit status
0: Success<br>
1: Python version is not suitable<br>
2: No arguments<br>
3: Lack of some arguments<br>
4: Imcomplete success because some files do not exist<br>
5: Imcomplete success because some files are not supported<br>
6: Imcomplete success because some files do not exist or are not supported
