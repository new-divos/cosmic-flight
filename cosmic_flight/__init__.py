#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


def draw(canvas):
    row, column = (5, 20)
    canvas.addstr(row, column, 'Hello, World!')
    canvas.border()
    canvas.refresh()
    time.sleep(1)
