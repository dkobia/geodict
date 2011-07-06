try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'GeoDict',
    'author': 'David Kobia',
    'url': 'http://github.com/dkobia/geodict',
    'download_url': 'http://github.com/dkobia/geodict',
    'author_email': 'david@ushahidi.com',
    'version': '0.1',
    'install_requires': ['mongodb','mongoengine','nose'],
    'packages': ['geodict'],
    'scripts': [],
    'name': 'geodict'
}

setup(**config)