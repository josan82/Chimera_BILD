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
	from chimera-BILD import chimera-BILD
	doExtensionFunc(arrow, args)

def cmd_box(cmdName, args):
	from Midas.midas_text import doExtensionFunc
	from chimera-BILD import chimera-BILD
	doExtensionFunc(box, args)

def cmd_cone(cmdName, args):
	from Midas.midas_text import doExtensionFunc
	from chimera-BILD import chimera-BILD
	doExtensionFunc(cone, args)

def cmd_cylinder(cmdName, args):
	from Midas.midas_text import doExtensionFunc
	from chimera-BILD import chimera-BILD
	doExtensionFunc(cylinder, args)

def cmd_sphere(cmdName, args):
	from Midas.midas_text import doExtensionFunc
	from chimera-BILD import chimera-BILD
	doExtensionFunc(sphere, args)

def cmd_vector(cmdName, args):
	from Midas.midas_text import doExtensionFunc
	from chimera-BILD import chimera-BILD
	doExtensionFunc(vector, args)

addCommand("arrow", cmd_arrow)
addCommand("box", cmd_box)
addCommand("cone", cmd_cone)
addCommand("cylinder", cmd_cylinder)
addCommand("sphere", cmd_sphere)
addCommand("vector", cmd_vector)