# -*- coding: utf-8 -*-
"""Excel Filelist.

Created 2015 Caleb Ely
<http://CodeTriangle.me/>


Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""


import os
import sys
from src.stringbuilder import StringBuilder


class FileList:
    def __init__(self, path):
        self.sb = StringBuilder()
        self.__path = path
        self.__blacklist = self.__getBlacklist()

        # First, generate a list of all the files
        self.allFiles = [f for f in self.__listFiles()]

        # Get the depth of the folders and
        # assign the root folder
        self.sb.setDepth(self.__getFolderDepth())
        self.sb.setRoot(os.path.basename(self.__path))

    def __listFiles(self):
        for root, dir, files in os.walk(self.__path):
            # Filter out any blocked folders
            # TODO Does not filter out subfolders
            if (
                self.__blacklist and
                os.path.basename(root).lower() in self.__blacklist["folders"]
            ):
                continue

            # Cut off all path before the root
            thisDir = root[root.index(
                           os.path.basename(self.__path)):].replace("\\", "/")

            for file in files:
                f = os.path.join(thisDir, file).replace("\\", "/")

                # Filter out any blocked files
                if (
                    self.__blacklist and
                    file.lower() in self.__blacklist["files"]
                ):
                    continue
                yield f

    def __getFolderDepth(self):
        maxDepth = 0

        for f in self.allFiles:
            # Get the largest folder depth
            curDepth = f.count("/")
            if curDepth > maxDepth:
                maxDepth = curDepth

        return maxDepth - 1

    def __getFiles(self):
        for file in self.allFiles:
            # Break up the path and remove the root folder
            parts = file.split("/")
            del parts[0]

            # Set the file name sections then remove it
            # so it does not get in our way
            self.sb.setFile(parts[-1])
            del parts[-1]

            # Now set the folders and yield each final string
            self.sb.setFolders(parts)
            yield self.sb.get()

    def __getBlacklist(self):
        blFile = os.path.join(os.path.dirname(sys.argv[0]), "blacklist.cfg")
        # The blacklist does not exist, silently fail
        if not os.path.exists(blFile):
            return None

        # Read the blacklist
        with open(blFile, "rt", encoding="utf-8") as f:
            lines = f.readlines()

        parts = {
            "files": [],
            "folders": []
        }

        # Seperate each item into files/folders
        for line in lines:
            line = line.strip()
            if line:
                if line.startswith(":dir:"):
                    parts["folders"].append(line.lstrip(":dir:"))
                else:
                    parts["files"].append(line)

        return parts

    def get(self):
        # Return the final strings
        return self.__getFiles()
