'''
constants: global constants for Handprint.

Authors
-------

Michael Hucka <mhucka@caltech.edu> -- Caltech Library

Copyright
---------

Copyright (c) 2018-2019 by the California Institute of Technology.  This code
is open-source software released under a 3-clause BSD license.  Please see the
file "LICENSE" for more information.
'''

import sys

import handprint
from handprint.services import AmazonTR
from handprint.services import GoogleTR
from handprint.services import MicrosoftTR

ON_WINDOWS = sys.platform.startswith('win')

ACCEPTED_FORMATS = ('jpg', 'jpeg', 'jp2', 'png', 'gif', 'bmp', 'tif', 'tiff')

KNOWN_SERVICES = {
    'amazon': AmazonTR,
    'google': GoogleTR,
    'microsoft': MicrosoftTR,
}
