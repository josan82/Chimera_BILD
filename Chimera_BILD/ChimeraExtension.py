#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division
import chimera.extension
from Midas.midas_text import addCommand
import Tkinter as tk
import Tix
Tix._default_root = tk._default_root

def cmd_arrow(cmdName, args):
	from Midas.midas_text import doExtensionFunc
	from Chimera_BILD import arrow
	doExtensionFunc(arrow, args)

def cmd_box(cmdName, args):
	from Midas.midas_text import doExtensionFunc
	from Chimera_BILD import box
	doExtensionFunc(box, args)

def cmd_cone(cmdName, args):
	from Midas.midas_text import doExtensionFunc
	from Chimera_BILD import cone
	doExtensionFunc(cone, args)

def cmd_cylinder(cmdName, args):
	from Midas.midas_text import doExtensionFunc
	from Chimera_BILD import cylinder
	doExtensionFunc(cylinder, args)

addCommand("arrow", cmd_arrow)
addCommand("box", cmd_box)
addCommand("cone", cmd_cone)
addCommand("cylinder", cmd_cylinder)
"""
addCommand("sphere", cmd_sphere)
addCommand("vector", cmd_vector)
"""
