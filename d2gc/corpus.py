

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
        self.paths = {}


    def index_librettists(self):

        """
        Index librettist -> paths.
        """

        # Glob .xml files.
        path = os.path.join(self.path, '*.xml')

        for path in glob.glob(path):

            person = Person(path)

            # Map librettists -> path.
            for lib in person.librettists:
                paths = self.paths.setdefault(lib, [])
                paths.append(path)


    def index_composers(self):

        """
        Index composer -> paths.
        """

        # Glob .xml files.
        path = os.path.join(self.path, '*.xml')

        for path in glob.glob(path):

            person = Person(path)

            # Map librettists -> path.
            for lib in person.composers:
                paths = self.paths.setdefault(lib, [])
                paths.append(path)


    def correct_librettists(self, original, corrected, alphabetized):

        """
        For all files with a name, replace librettists.
        """

        paths = self.paths.get(original)
        if not paths: return

        for path in paths:

            try:
                person = Person(path)
                person.correct_librettist(original, corrected, alphabetized)
                person.save()

            except: pass


    def correct_composers(self, original, corrected, alphabetized):

        """
        For all files with a name, replace composers.
        """

        paths = self.paths.get(original)
        if not paths: return

        for path in paths:

            try:
                person = Person(path)
                person.correct_composer(original, corrected, alphabetized)
                person.save()

            except: pass
