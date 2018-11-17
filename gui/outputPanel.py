#!/usr/bin/env python
# coding: utf-8

from tkinter import *


class OutputPanel(object):
    def __init__(self, parent):
        self.parent = parent
        print("hello output")
        self.outputPanel()

    def outputPanel(self):
        # make a text box to put the serial output
        self.log = Text(self.parent.root, takefocus=0,
                        bg="#4E4E7B",
                        fg="#dfdfdf",
                        bd=0,
                        highlightbackground="#4E4E7B",
                        highlightcolor="#4E4E7B",
                        highlightthickness=4,
                        insertbackground="#dfdfdf",
                        selectbackground="#2D2D46",
                        selectforeground="#dfdfdf")

        # make a scrollbar
        scrollbar = Scrollbar(self.log, bg="#2D2D46")
        scrollbar.pack(side=RIGHT, fill=Y)
        # attach text box to scrollbar
        self.log.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.log.yview)
        self.log.pack(expand=True, fill='both', side=BOTTOM)

    def logger(self, message):
        self.log.delete('0.0', END)
        self.log.insert('0.0', message)
