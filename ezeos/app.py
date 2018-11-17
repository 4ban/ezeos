#!/usr/bin/env python
# coding: utf-8

from tkinter import Tk
from gui.ui import UI
from ezeos import EZEOS
from ezeos import VERSION


def run():
    root = Tk()
    app = UI(root)
    app.setstatus(VERSION)
    app.logger(EZEOS)
    # Application

    root.mainloop()
