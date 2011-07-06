__author__ = "SwiftRiver Team"
__copyright__ = "Copyright 2011, Ushahidi Inc."
__credits__ = ["Pete Warden", "David Kobia"]
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "SwiftRiver Team"
__email__ = "swiftdev@ushahidi.com"
__status__ = "Development"

from mongoengine import *
import geodict_config

# Connect to MongoDB Database
connect(geodict_config.database)

# Country Model
class Country(Document):
    country = StringField(required=True, max_length=64)
    country_code = StringField(max_length=2)
    lat = FloatField()
    lon = FloatField()
    last_word = StringField(max_length=32)

# Region Model
class Region(Document):
    region = StringField(required=True)
    country = ReferenceField(Country)
    region_code = StringField()
    lat = FloatField()
    lon = FloatField()
    last_word = StringField()

# City Model
class City(Document):
    city = StringField(required=True)
    country = ReferenceField(Country)
    region = ReferenceField(Region)
    population = IntField()
    lat = FloatField()
    lon = FloatField()
    last_word = StringField()
    
    meta = {
        'ordering': ['-population']
    }

