__author__ = "SwiftRiver Team"
__copyright__ = "Copyright 2011, Ushahidi Inc."
__credits__ = ["Pete Warden", "David Kobia", "Edmar Ferreira"]
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "SwiftRiver Team"
__email__ = "swiftdev@ushahidi.com"
__status__ = "Development"

"""Miscellaneous functions and classes"""
import re
import csv
import geodict_config

class CIList(list):
    '''
    Case Insensitive list
    A simple derivation of standard list with the
    in operator overridden to make comparisons
    case insensitive.
    '''
    def __contains__(self, key):
        for t in self:
            if key.lower() == t.lower():
                return True
        return False


reader = csv.reader(open(geodict_config.data_folder+'stopwords.csv', 'rb'))
stop_words = CIList()
for line in reader:
    stop_words += line