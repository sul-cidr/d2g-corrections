

import codecs
import os

from lxml import etree
from bs4 import UnicodeDammit


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


    @property
    def composers(self):

        """
        Query for composer names.

        Returns: str
        """

        comps = self.tree.xpath('//field[@name="composer"]')
        return [comp.text for comp in comps]


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


    def find_composer(self, name):

        """
        Given a name, find a `composer` field.

        Args:
            name (str)
        """

        query = '//field[@name="composer"][.="%s"]'
        return self.tree.xpath(query % name)[0]


    def find_composer_sort(self, name):

        """
        Given a name, find a `composerSort` field.

        Args:
            name (str)
        """

        query = '//field[@name="composer"][.="%s"]/following-sibling::field'
        return self.tree.xpath(query % name)[0]


    def correct_librettist(self, original, corrected, alphabetized):

        """
        Replace librettist names.

        Args:
            original (str)
            corrected (str)
            alphabetized (str)
        """

        librettist = self.find_librettist(original)
        librettist_sort = self.find_librettist_sort(original)

        librettist.text = corrected
        librettist_sort.text = alphabetized


    def correct_composer(self, original, corrected, alphabetized):

        """
        Replace composer names.

        Args:
            original (str)
            corrected (str)
            alphabetized (str)
        """

        composer = self.find_composer(original)
        composer_sort = self.find_composer_sort(original)

        composer.text = corrected
        composer_sort.text = alphabetized


    def save(self):

        """
        Write changes to the file.
        """

        self.tree.write(self.path, encoding='utf8', xml_declaration=True)
