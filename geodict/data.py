__author__ = "SwiftRiver Team"
__copyright__ = "Copyright 2011, Ushahidi Inc."
__credits__ = ["Pete Warden", "David Kobia"]
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "SwiftRiver Team"
__email__ = "swiftdev@ushahidi.com"
__status__ = "Development"

from resources import *
import string, StringIO

def get_cities(pulled_word,current_word,country_code,region_code):
    search = {}
    search["last_word"] = current_word
    if country_code:
        search["country"] = country_code
    if region_code:
        search["region"] = region_code
    
    name_map = {}
    for candidate in City.objects(__raw__=search):
        name = candidate.city.lower()
        name_map[name] = candidate
    return name_map


def setup_countries_cache():
    countries_cache = {}
    for candidate in Country.objects:
        last_word = candidate.last_word.lower()
        if last_word not in countries_cache:
            countries_cache[last_word] = []
        countries_cache[last_word].append(candidate)
    return countries_cache


def setup_regions_cache():
    regions_cache = {}
    for candidate in Region.objects:
        last_word = candidate.last_word.lower()
        if last_word not in regions_cache:
            regions_cache[last_word] = []
        regions_cache[last_word].append(candidate)
    return regions_cache
