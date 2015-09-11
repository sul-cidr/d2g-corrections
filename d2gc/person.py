

import codecs
import os

from lxml import etree


class Person:


    def __init__(self, path):

        """
        Set the document path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)


    @property
    def tree(self):

        """
        Open and parse the file.

        Returns: etree
        """

        with open(self.path, 'rb') as fh:
            reader = codecs.EncodedFile(fh, 'utf8', 'utf8', 'replace')
            return etree.parse(reader)


    @property
    def librettists(self):

        """
        Query for librettist names.

        Returns: str
        """

        libs = self.tree.xpath('//field[@name="librettist"]')
        return [lib.text for lib in libs]
