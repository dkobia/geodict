__author__ = "SwiftRiver Team"
__copyright__ = "Copyright 2011, Ushahidi Inc."
__credits__ = ["Pete Warden", "David Kobia"]
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "SwiftRiver Team"
__email__ = "swiftdev@ushahidi.com"
__status__ = "Development"

# The location of data like stop words
data_folder = '../data/'

# The location of the source data to be loaded into your database
source_folder = '../source_data/'

# Your MySQL user credentials
user = 'root'
password = ''

# The address and port number of your database server
host = 'localhost'
port = 0

# The name of the database to create
database = 'geodict'

# The maximum number of words in any name
word_max = 3

# Words that provide evidence that what follows them is a location
location_words = {
    'at': True,
    'in': True
}