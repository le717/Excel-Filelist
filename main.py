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
import time

from openpyxl import Workbook
from src.filelist import FileList


def main():
    # Get the location to scan
    try:
        path = sys.argv[1]
    except IndexError:
        path = os.getcwd()

    # Work in the scanned directory
    path = os.path.abspath(path)
    os.chdir(path)

    # Output file name
    fileName = "{0} file index.xlsx".format(os.path.basename(path))

    # Execution start time
    start = time.monotonic()

    # List the files
    fl = FileList(path)

    # Create a new workbook with parameters to optimize execution time
    wb = Workbook(optimized_write=True, write_only=True)
    ws = wb.create_sheet()

    # List each file
    for f in fl.get():
        ws.append(f)

    # Save the spreadsheet
    wb.save(fileName)

    # Execution end and total time
    # Round off the seconds for a prettier number
    end = time.monotonic()
    elapsed = round(end - start)

    print("All files in\n{0} listed and saved to\n{1} in {2} seconds.".format(
          os.path.normpath(path), fileName, elapsed))


if __name__ == "__main__":
    main()
