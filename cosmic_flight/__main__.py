#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses

from . import draw


curses.update_lines_cols()
curses.wrapper(draw)
