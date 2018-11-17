#!/usr/bin/env python
# coding: utf-8

from tkinter import *
from gui.tabPanel import TabPanel
from gui.menuBar import MenuBar
from gui.outputPanel import OutputPanel


class UI(object):
    def __init__(self, root):
        self.root = root
        self.root.title("EZEOS")
        self.root.geometry('1200x600')
        self.root.config(bg="#2D2D46",
                         bd=0,
                         highlightbackground="#2D2D46",
                         highlightcolor="#2D2D46",
                         highlightthickness=7)
        # Add menubar
        self.menuBar = MenuBar(self)
        # Add status bar
        self.status = StatusBar(self.root)
        self.status.pack(side=TOP, fill=X)
        # Add Tab panel
        self.tabPanel = TabPanel(self)
        # Add output panel
        self.outputPanel = OutputPanel(self)

    def logger(self, message):
        self.outputPanel.log.delete('0.0', END)
        self.outputPanel.log.insert('0.0', message)

    def setstatus(self, message):
        self.status.clear()
        self.status.set(message)

    def about(self):
        self.logger("Volentix Labs, Inc")


class StatusBar(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.label = Label(self, bd=0,
                           height=1,
                           relief=SUNKEN,
                           highlightthickness=2,
                           highlightbackground="#2D2D46",
                           highlightcolor="#2D2D46",
                           anchor=W,
                           bg="#4E4E7B",
                           fg="#dfdfdf")
        self.label.pack(fill=X)

    def set(self, format, *args):
        self.label.config(text="> "+format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()
