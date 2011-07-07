#!/usr/bin/env python

__author__ = "SwiftRiver Team"
__copyright__ = "Copyright 2011, Ushahidi Inc."
__credits__ = ["Pete Warden", "David Kobia"]
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "SwiftRiver Team"
__email__ = "swiftdev@ushahidi.com"
__status__ = "Development"

import csv, os, os.path
from resources import *
from geodict_lib import *

def load_countries(cursor):
    reader = csv.reader(open(geodict_config.source_folder+'countrypositions.csv', 'rb'))
    country_positions = {}

    for row in reader:
        row = [field.decode('ISO-8859-1') for field in row]
        try:
            country_code = row[0]
            lat = row[1]
            lon = row[2]
        except:
            continue

        country_positions[country_code] = { 'lat': lat, 'lon': lon }
        
    reader = csv.reader(open(geodict_config.source_folder+'countrynames.csv', 'rb'))

    for row in reader:
        row = [field.decode('ISO-8859-1') for field in row]
        try:
            country_code = row[0]
            country_names = row[1]
        except:
            continue    

        country_names_list = country_names.split(' | ')
        
        lat = country_positions[country_code]['lat']
        lon = country_positions[country_code]['lon']
        
        for country_name in country_names_list:
            country_name = country_name.strip()
            
            last_word, index, skipped = pull_word_from_end(country_name, len(country_name)-1, False)
            
            # Finally save the country
            print "Country Name:%s, Country Code:%s, Lat:%s, Lon:%s, Last Word:%s" % (country_name, country_code, lat, lon, last_word)
            country = Country(country=country_name)
            country.country_code = country_code
            country.lat = float(lat)
            country.lon = float(lon)
            country.last_word = last_word
            country.save()


def load_regions(cursor):
    reader = csv.reader(open(geodict_config.source_folder+'us_statepositions.csv', 'rb'))
    us_state_positions = {}

    for row in reader:
        row = [field.decode('ISO-8859-1') for field in row]
        try:
            region_code = row[0]
            lat = row[1]
            lon = row[2]
        except:
            continue

        us_state_positions[region_code] = { 'lat': lat, 'lon': lon }

    reader = csv.reader(open(geodict_config.source_folder+'us_statenames.csv', 'rb'))

    country_code = 'US'

    for row in reader:
        row = [field.decode('ISO-8859-1') for field in row]
        try:
            region_code = row[0]
            state_names = row[2]
        except:
            continue    

        state_names_list = state_names.split('|')

        lat = us_state_positions[region_code]['lat']
        lon = us_state_positions[region_code]['lon']

        for state_name in state_names_list:

            state_name = state_name.strip()

            last_word, index, skipped = pull_word_from_end(state_name, len(state_name)-1, False)
            
            # First, lets look for associated country in the system
            country = Country.objects(country_code=country_code).first()

            # Finally save the region
            print "Region Name:%r, Region Code:%r, Lat:%r, Lon:%r, Last Word:%r" % (state_name, region_code, lat, lon, last_word)
            region = Region(region=state_name)
            region.country = country
            region.region_code = region_code
            region.lat = float(lat)
            region.lon = float(lon)
            region.last_word = last_word
            region.save()


def load_cities(cursor):
    reader = csv.reader(open(geodict_config.source_folder+'worldcitiespop.csv', 'rb'))
    for row in reader:
        row = [field.decode('ISO-8859-1') for field in row]
        #row = [field.decode('utf8') for field in row]
        #row = [unicode(field, 'utf8') for field in row]
        try:
            country = row[0]
            city = row[1]
            region_code = row[3]
            population = row[4]
            lat = row[5]
            lon = row[6]
        except:
            continue

        if population is '':
            population = 0

        city = city.strip()

        last_word, index, skipped = pull_word_from_end(city, len(city)-1, False)
        
        # First, lets look for associated country in the system
        country = Country.objects(country_code=country).first()
        
        # Next, lets look for associated region in the system
        region = Region.objects(region_code=region_code).first()
        
        # Finally save the city
        print "City Name:%r, Lat:%r, Lon:%r, Last Word:%r" % (city, lat, lon, last_word)
        city = City(city=city)
        city.country = country
        city.region = region
        city.lat = float(lat)
        city.lon = float(lon)
        city.last_word = last_word
        city.save()

        
# Load Countries First So that we can
# associate the Regions and Cities Objects in MongoDB
load_countries({})
load_regions({})
load_cities({})