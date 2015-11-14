# -*- coding: utf-8 -*-
"""Excel Filelist.

Created 2015 Caleb Ely
<http://CodeTriangle.me/>


Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""


from os.path import splitext


__all__ = ("StringBuilder")


class StringBuilder:

    def __init__(self):
        self.final = []
        self.depth = None

    def setRoot(self, fol):
        self.final.insert(0, fol)

    def setDepth(self, depth):
        self.depth = depth
        self.final = [""] * (depth + 2)

    def setFile(self, fName):
        name, ext = splitext(fName)
        self.final[-1] = ext[1:]
        self.final[-2] = name

    def setFolders(self, fols):
        # Pad folders to the max depth
        if len(fols) < self.depth:
            diff = self.depth - len(fols)
            for _ in range(0, diff):
                fols.append("")

        # Add the folders to their respective cells
        for i in range(0, len(fols)):
            fol = fols[i]
            self.final[i + 1] = fol

    def get(self):
        return self.final
