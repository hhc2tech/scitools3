import sys

import scitools

try:
    from setuptools import setup
except:
    from distutils.core import setup

if __name__ == '__main__':
    setup(
        name=         "scitools3",
        version=      '1.0',
        author=       ', '.join(scitools.author),
        author_email= "onnoeberhard@gmail.com",
        description=  scitools.__doc__,
        license=      "BSD",
        url=          "https://github.com/onnoeberhard/scitools3",
        packages=     ['scitools'],
        package_dir=  {'scitools': 'scitools'},
    )
