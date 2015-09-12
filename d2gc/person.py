

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

        with open(self.path, 'rb') as fh:
            reader = codecs.EncodedFile(fh, 'utf8', 'utf8', 'replace')
            self.tree = etree.parse(reader)


    @property
    def librettists(self):

        """
        Query for librettist names.

        Returns: str
        """

        libs = self.tree.xpath('//field[@name="librettist"]')
        return [lib.text for lib in libs]


    def find_librettist(self, name):

        """
        Given a name, find a `librettist` field.

        Args:
            name (str)
        """

        query = '//field[@name="librettist"][.="%s"]'
        return self.tree.xpath(query % name)[0]


    def find_librettist_sort(self, name):

        """
        Given a name, find a `librettistSort` field.

        Args:
            name (str)
        """

        query = '//field[@name="librettist"][.="%s"]/following-sibling::field'
        return self.tree.xpath(query % name)[0]


    def correct(self, original, corrected, alphabetized):

        """
        For all files with a name, replace librettists.

        Args:
            original (str)
            corrected (str)
            alphabetized (str)
        """

        librettist = self.find_librettist(original)
        librettist_sort = self.find_librettist_sort(original)

        librettist.text = corrected
        librettist_sort.text = alphabetized


    def save(self):

        """
        Write changes to the file.
        """

        self.tree.write(self.path)
