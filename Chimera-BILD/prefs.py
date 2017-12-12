#!/usr/bin/env python
# encoding: utf-8

"""
This is the preferences file for the extension. All default values
should be listed here for reference and easy reuse.
"""


from __future__ import print_function, division
from distutils.spawn import find_executable
import os
# Chimera
from chimera.preferences import preferences, addCategory, HiddenCategory
#from core import SNFG

"""
def _defaults():
#	return dict(zip(SNFG.__init__.im_func.func_code.co_varnames[1:],
#					SNFG.__init__.im_func.func_defaults))
	pass

DEFAULTS = _defaults()
#DEFAULTS['icon_size'] = DEFAULTS['size'] / 2.5
#DEFAULTS['full_size'] = DEFAULTS['size']

prefs = addCategory("plume_p4", HiddenCategory, optDict=DEFAULTS.copy())
try:
	with open(preferences._filename) as f:
		d = eval(f.read())
	prefs.update(d.get('plume_p4', {}))
except Exception as e:
	print('Problem loading saved preferences:', e)
"""