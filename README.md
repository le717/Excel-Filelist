# Excel Filelist #
> Generate a filelist of a given folder's content, exported to an Excel spreadsheet.

## Features ##
Simply drop the packaged exe into the desired folder and a filelist will be saved to `<folder name> file index.xlsx`.
If you are directly running the frozen exe or `main.py`, you can also specify a file path to scan (`ExcelFilelist.exe <path/to/folder>`).
Passing the path as an argument will still save the spreadsheet in the given directory.
Further, running the frozen exe/py script gives you access to a configurable blacklist `blacklist.cfg` to filter out any unwanted files or folders.

## Requirements ##
* Python 3.3+
* [`openpyxl`](https://openpyxl.readthedocs.org)
* [Inno Setup (Unicode)](http://www.jrsoftware.org/isinfo.php)


## License ##
[MIT](LICENSE)

2015 Caleb Ely
