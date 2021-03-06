#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
# Python AI Battle
#
# Copyright 2011 Matthew Thompson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################

'''
Phil's Brain

See the wander.py file for brain docs (too hard to keep two up to date)
'''

import random


def turn_around():
    '''Turn 180 degress around. New by Phil.'''
    if facing is UP:
        face(DOWN)
    elif facing is DOWN:
        face(UP)
    elif facing is LEFT:
        face(RIGHT)
    elif facing is RIGHT:
        face(LEFT)


def think():

    x, y = position
    dx, dy = direction

    tile, item = radar(x + dx, y +dy)

    print "Tank: ", color, " Tile: ",tile, " Item: ", item

    if tile is None or tile is WATER or item is not None:
        print memory
        turn_around()
    else:
        forward()

