#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
from typing import Iterable

import curses


class SchemaEntry:
    __slots__ = 'symbol', 'duration', 'flags'

    def __init__(self, symbol, duration=0.5, flags=curses.A_NORMAL):
        self.symbol = symbol
        self.duration = duration
        self.flags = flags


async def blink(canvas, row, column, schema: Iterable[SchemaEntry]):
    for entry in schema:
        canvas.addstr(row, column, entry.symbol, entry.flags)
        canvas.refresh()
        await asyncio.sleep(0)
