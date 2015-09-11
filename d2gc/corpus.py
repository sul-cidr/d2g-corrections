

import codecs
import os
import glob

from lxml import etree
from .person import Person


class Corpus:


    @classmethod
    def from_env(cls):

        """
        Make an instance from the ENV-defined location.
        """

        return cls(os.environ.get('D2G_CORPUS'))


    def __init__(self, path):

        """
        Set corpus path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)
        self.index()


    def index(self):

        """
        Map name -> file paths.
        """

        self.paths = {}

        # Glob .xml files.
        path = os.path.join(self.path, '*.xml')

        for path in glob.glob(path):

            person = Person(path)

            # Map librettists -> path.
            for lib in person.librettists:
                paths = self.paths.setdefault(lib, [])
                paths.append(path)


    def correct(self, original, corrected, alphabetized):

        """
        For all files with a name, replace librettists.
        """

        paths = self.names[original]
        print(paths)
