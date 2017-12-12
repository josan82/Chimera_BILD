#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import chimera
from chimera import runCommand

try:
	from cStringIO import StringIO
except ImportError:
	from StringIO import StringIO
from textwrap import dedent
from Bld2VRML import openFileObject as openBildFileObject

#import os
#import math

class BILD_element(object):

	SUPPORTED_SHAPES = set('arrow box cone cylinder sphere vector'.split())

	def __init__(self, shape, origin, color, name='BILD', transparency=0, 
				parent_id=100, end=None, r1=None, r2=None, rho=None, opened=False):
		if shape not in self.SUPPORTED_SHAPES:
			raise ValueError('`shape` should be one of: '
							 '{}'.format(', '.join(self.SUPPORTED_SHAPES)))
		self.shape = shape
		self.name = name
		self.radius1 = r1
		self.radius2 = r2
		self.rho = rho
		self.origin = origin
		self.end = end
		self.color = color
		self.transparency = transparency
		self.open = opened
		self._vrml_shape = None
		self._id = parent_id
		self._subid = 0

	def destroy(self):
		if self._vrml_shape is not None:
			chimera.openModels.close(self._vrml_shape)
			self._vrml_shape = None

	def draw(self):
		self._vrml_shape = getattr(self, '_draw_' + self.shape)()

	def _draw_box(self):
		x1, y1, z1 = self.origin
		x2, y2, z2 = self.end
		col = str(self.color).replace(",", " ")
		bild = """
		.color {}
		.transparency {}
		.box {} {} {} {} {} {} 
		""".format(col, self.transparency, x1, y1, z1, x2, y2, z2)
		return self._build_vrml(bild)

	def _draw_sphere(self):
		x, y, z = self.origin
		bild = """
		.color {}
		.transparency {}
		.sphere {} {} {} {}
		""".format(self.color, 0.3, x, y, z, self.size)
		return self._build_vrml(bild)

	def _draw_arrow(self):
		x1, y1, z1 = self.origin
		x2, y2, z2 = self.end
		col = str(self.color).replace(",", " ")
		bild = """
		.color {}
		.transparency {}
		.arrow {} {} {} {} {} {} {} {} {}
		""".format(col, self.transparency, x1, y1, z1, x2, y2, z2, self.radius1, self.radius2, self.rho)
		return self._build_vrml(bild)

	def _draw_cone(self):
		x1, y1, z1 = self.origin
		x2, y2, z2 = self.end
		col = str(self.color).replace(",", " ")
		op = 'open' if self.open else ""
		bild = """
		.color {}
		.transparency {}
		.cone {} {} {} {} {} {} {} {}
		""".format(col, self.transparency, x1, y1, z1, x2, y2, z2, self.radius1, op)
		return self._build_vrml(bild)

	def _build_vrml(self, bild, name=None):
		if name is None:
			name = self.name
		f = StringIO(dedent(bild))
		try:
			vrml = openBildFileObject(f, '<string>', name)
		except chimera.NotABug:
			print(bild)
		else:
			chimera.openModels.add(vrml, baseId=self._id, subid=self._subid)
			self._subid += 1
		return vrml

def arrow(x1, y1, z1, x2, y2, z2, c, transparency=0, r1=None, r2=None, rho=None, id=100):
	if not r1:
		r1 = 0.1
	if not r2:
		r2 = 4 * r1
	if not rho:
		rho = 0.75
	arrow_elem = BILD_element(shape="arrow", origin=(x1,y1,z1), end=(x2,y2,z2), 
					r1=r1, r2=r2, rho=rho, color=c, transparency=transparency, parent_id=id)
	arrow_elem.draw()

def box(x1, y1, z1, x2, y2, z2, c, transparency=0, id=100):
	box_elem = BILD_element(shape="box", origin=(x1,y1,z1), end=(x2,y2,z2), 
					color=c, transparency=transparency, parent_id=id)
	box_elem.draw()

def cone(x1, y1, z1, x2, y2, z2, r, c, transparency=0, open=False, id=100):
	cone_elem = BILD_element(shape="arrow", origin=(x1,y1,z1), end=(x2,y2,z2), 
					r1=r, color=c, transparency=transparency, parent_id=id, opened=open)
	cone_elem.draw()
"""
			p4_elem = p4_element(shape="sphere", size=(mergeTol/2), origin=chimera.Point(feat.GetPos()[0],feat.GetPos()[1],feat.GetPos()[2]), color=_featColors[feat.GetFamily()])
			p4_elem.draw()
		
		if feat.featDirs:
			ps, fType = feat.featDirs			
			for tail, head in ps:
				if fType == 'linear':
					p4_elem = p4_element(shape="arrow", origin=tail, end=head, color=_featColors[feat.GetFamily()])
				elif fType =='cone':
					p4_elem = p4_element(shape="cone", origin=head, end=tail, color=_featColors[feat.GetFamily()], size=(1.33))
				p4_elem.draw()
"""
