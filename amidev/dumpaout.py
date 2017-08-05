#!/usr/bin/env python

from __future__ import print_function, unicode_literals

import logging
import sys

from amidev.binfmt import aout


if __name__ == '__main__':
    logging.basicConfig()

    for path in sys.argv[1:]:
        obj = aout.Aout()
        obj.read(path)
        obj.dump()
