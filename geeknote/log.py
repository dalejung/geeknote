# -*- coding: utf-8 -*-

import os, sys
import logging
import config

if config.DEBUG:
    logging.basicConfig(format="%(filename)s %(funcName)s %(lineno)d : %(message)s", level=logging.DEBUG)
else:
    logging.basicConfig(format="%(asctime)-15s %(module)s %(funcName)s %(lineno)d : %(message)s", filename=config.ERROR_LOG)


if False:
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)
