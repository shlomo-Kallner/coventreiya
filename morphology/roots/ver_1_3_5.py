#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  ver_1_3_5.py
#  
#  Copyright 2017 shlomo <shlomo.kallner@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

##################################################################
#
# Imports
#

from coventreiya.phonotactics.onsets.ver_1_5_7 import ver_1_5_7 as __onset_mat

from coventreiya.morphology.roots.abc import root_abc

##################################################################
#
# Morphology  - Roots - Abstract Base Class
#

class ver_1_3_5(root_abc):
	def __init__(self, root_, length=0):
		min_length = 1
		max_length = 6
		self.__matcher = __onset_mat()
		super().__init__(root_, length, min_length, max_length)
		
	def matcher(self):
		return self.__matcher

#
#
#
##################################################################

##################################################################
#
# Tests Main
#

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
