#!/usr/bin/env python
# coding: utf-8

from tkinter import Tk
from gui.ui import UI


def run():
    root = Tk()
    app = UI(root)
    # Application
    root.mainloop()

