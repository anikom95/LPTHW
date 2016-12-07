try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'Aniko Milz': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it',
    'aniko.milz@web.de': 'My Email.'
    'version': '0,1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
