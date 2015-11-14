#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Excel Filelist.

Created 2015 Caleb Ely
<http://CodeTriangle.me/>


Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""


import os
import sys
import zipfile
from cx_Freeze import (setup, Executable)


# Output folder
destfolder = "bin"

# Create the freeze path if it doesn't exist
if not os.path.exists(destfolder):
    os.makedirs(destfolder)

build_exe_options = {
    "build_exe": destfolder,
    "create_shared_zip": True,
    "optimize": 2,
    "compressed": True
}

setup(
    name="Excel Filelist",
    version="1.0.0",
    author="Caleb Ely",
    description="Excel Filelist v1.0.0",
    license="MIT",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", targetName="ExcelFilelist.exe")]
)
