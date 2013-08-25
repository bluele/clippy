from setuptools import setup, find_packages
from os.path import dirname, abspath, join, isfile

cwd = abspath(dirname(__file__))

version = '1.0'

setup(name='clippy',
      version=version,
      description="A Cross-platform clipboard command for Linux, MacOSX, etc...",
      long_description="""\
      A Cross-platform clipboard command for Linux, MacOSX, etc...
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='clipboard command',
      author='bluele',
      author_email='junkxdev@gmail.com',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      scripts=[
          join(cwd, 'scripts', 'clippy'),
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
