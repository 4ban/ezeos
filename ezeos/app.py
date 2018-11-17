#!/usr/bin/env python
# coding: utf-8

from tkinter import Tk
from gui.ui import UI

def run():
    root = Tk()
    app = UI(root)
    app.setstatus("App is running")
    app.logger("Hello world")
    root.mainloop()
