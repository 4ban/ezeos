#!/usr/bin/env python
# coding: utf-8

from tkinter import *
from tkinter import ttk


class TabPanel(object):
    def __init__(self, parent):
        self.parent = parent
        print("hello tab")
        self.tabPanel()
        lbl = ttk.Label(self.tab1, text='ddfdfdf')
        lbl.pack()

    def tabPanel(self):
        style = ttk.Style(self.parent.root)
        style.configure("TNotebook",
                        background="#2D2D46",
                        foreground="#dfdfdf",
                        borderwidth=0,
                        highlightbackground="#2D2D46",
                        highlightcolor="#2D2D46",
                        highlightthickness=0)

        style.map("TNotebook.Tab",
                  background=[("selected", "#4E4E7B"),
                              ("active", "#4E4E7B")],
                  foreground=[("selected", "#dfdfdf"),
                              ("active", "#dfdfdf")]
                  )

        style.configure("TNotebook.Tab",
                        background="#2D2D46",
                        foreground="#dfdfdf",
                        borderwidth=0,
                        highlightbackground="#2D2D46",
                        highlightcolor="#2D2D46",
                        highlightthickness=0)

        style.configure("TFrame",
                        background="#2D2D46",
                        foreground="#dfdfdf",
                        highlightbackground="#2D2D46",
                        highlightcolor="#2D2D46",
                        highlightthickness=0,
                        borderwidth=0)

        self.notebook = ttk.Notebook(self.parent.root, style='TNotebook')

        self.tab1 = ttk.Frame(self.notebook, style='TFrame')
        self.tab2 = ttk.Frame(self.notebook, style='TFrame')
        self.tab3 = ttk.Frame(self.notebook, style='TFrame')
        self.tab4 = ttk.Frame(self.notebook, style='TFrame')
        self.tab5 = ttk.Frame(self.notebook, style='TFrame')
        self.tab6 = ttk.Frame(self.notebook, style='TFrame')
        self.tab7 = ttk.Frame(self.notebook, style='TFrame')
        self.tab8 = ttk.Frame(self.notebook, style='TFrame')
        self.tab9 = ttk.Frame(self.notebook, style='TFrame')
        self.tab10 = ttk.Frame(self.notebook, style='TFrame')
        self.tab11 = ttk.Frame(self.notebook, style='TFrame')
        self.tab12 = ttk.Frame(self.notebook, style='TFrame')

        self.notebook.add(self.tab1, text='Block Chain')
        self.notebook.add(self.tab2, text='Wallets')
        self.notebook.add(self.tab3, text='Accounts')
        self.notebook.add(self.tab4, text='Contracts')

        self.notebook.pack(expand=True, fill='both')
