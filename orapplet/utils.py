#!/usr/bin/env python2

# This file is part of or-applet.
#
# or-applet is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# or-applet is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with or-applet.  If not, see <http://www.gnu.org/licenses/>.

import os

LEEK_ICON = 'assets/Leek-icon.png'
LEEK_NOT_READY_ICON = 'assets/Leek-not-ready-icon.png'

def get_leek_icon(ready=True):
    if ready:
        return get_asset_path(LEEK_ICON)
    else:
        return get_asset_path(LEEK_NOT_READY_ICON)

def get_asset_path(relative):
    prefix = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(prefix, relative)

