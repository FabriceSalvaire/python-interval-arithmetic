####################################################################################################
#
# ArithmeticInterval - A Python Arithmetic Interval Module
# Copyright (C) 2015 Fabrice Salvaire
#
# This program is free software: you can redistribute it and/or modify it under the terms
# of the GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.
#
####################################################################################################

####################################################################################################

import os
import sys

####################################################################################################

# Utility function to read the README file.
# Used for the long_description.
def read(file_name):

    path = os.path.dirname(__file__)
    if os.path.basename(path) == 'tools':
        path = os.path.dirname(path)
    absolut_file_name = os.path.join(path, file_name)

    if os.path.exists(absolut_file_name):
        return open(absolut_file_name).read()
    else:
        sys.stderr.write("WARNING: README {} not found\n".format(absolut_file_name))
        return ''

####################################################################################################

long_description = read('README.rst')

setup_dict = dict(
    name='ArithmeticInterval',
    version='0.2.0',
    author='Fabrice Salvaire',
    author_email='fabrice.salvaire@orange.fr',
    description='A Python Arithmetic Interval Module',
    license = "GPLv3+",
    keywords = "arithmetic interval",
    url='https://github.com/FabriceSalvaire/python-arithmetic-interval',
    packages=['ArithmeticInterval'],
    long_description=long_description,
    # cf. http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Topic :: Scientific/Engineering :: Mathematics",
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        ],
    )
