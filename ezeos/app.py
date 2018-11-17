#!/usr/bin/env python
# coding: utf-8

from tkinter import Tk
from gui.ui import UI

def run():
    root = Tk()
    app = UI(root)
    app.status.set("App is running")
    # app.status.clear()
    app.log.insert('0.0', "hello")
    root.mainloop()

