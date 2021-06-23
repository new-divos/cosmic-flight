#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

import curses

from .stars import SchemaEntry, blink


def draw(canvas):
    row, column = (5, 20)
    canvas.addstr(row, column, 'Hello, World!')
    canvas.border()
    curses.curs_set(False)
    canvas.refresh()

    star_row, star_col = (8, 8)
    schema = (
        SchemaEntry(symbol='✶', duration=2.0, flags=curses.A_DIM),
        SchemaEntry(symbol='✷', duration=0.3),
        SchemaEntry(symbol='✹', duration=0.5),
        SchemaEntry(symbol='✷', duration=0.3)
    )

    coroutine = blink(canvas, star_row, star_col, schema)
    coroutine.send(None)
    time.sleep(1.0)
    coroutine.send(None)
    time.sleep(1.0)
    coroutine.send(None)
    time.sleep(1.0)
    coroutine.send(None)
    time.sleep(5.0)
