#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

import curses


def draw(canvas):
    row, column = (5, 20)
    canvas.addstr(row, column, 'Hello, World!')
    canvas.border()
    curses.curs_set(False)
    canvas.refresh()

    star_row, star_col = (8, 8)
    while True:
        canvas.addstr(star_row, star_col, '✶', curses.A_DIM)
        canvas.refresh()
        time.sleep(2.0)

        canvas.addstr(star_row, star_col, '✷')
        canvas.refresh()
        time.sleep(0.3)

        canvas.addstr(star_row, star_col, '✹')
        canvas.refresh()
        time.sleep(0.5)

        canvas.addstr(star_row, star_col, '✷')
        canvas.refresh()
        time.sleep(0.3)
