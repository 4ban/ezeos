#!/usr/bin/env python
# coding: utf-8

from tkinter import *
from tkinter import ttk


class TabPanel(object):
    def __init__(self, parent):
        self.parent = parent
        self.tabPanel()
        self.fillTab1()
        self.fillTab2()
        self.fillTab3()
        self.fillTab4()

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

        self.notebook.add(self.tab1, text='Block Chain')
        self.notebook.add(self.tab2, text='Wallets')
        self.notebook.add(self.tab3, text='Accounts')
        self.notebook.add(self.tab4, text='Contracts')

        self.notebook.pack(expand=True, fill='both', )

    def fillTab1(self):
        self.netState = IntVar()

        mainNet = Radiobutton(self.tab1, text='Main Net', value=1, variable=self.netState)
        testNet = Radiobutton(self.tab1, text='Test Net', value=2, variable=self.netState)
        btn = Button(self.tab1, text="Click Me", command=self.clicked)

        mainNet.pack(anchor=NW, padx=0, pady=3)
        testNet.pack(anchor=NW, padx=0, pady=3)
        btn.pack(anchor=NW, padx=0, pady=3)

    def fillTab2(self):
        lbl = Label(self.tab2, text="Hello")
        lbl.pack()

        btn = Button(self.tab2, text="Click Me", command=self.parent.about)
        btn.pack()

        txt = Entry(self.tab2, width=10)
        txt.pack()
        # in func
        # res = "Welcome to " + txt.get()
        #
        # lbl.configure(text=res)

    def fillTab3(self):
        pass

    def fillTab4(self):
        pass

    def clicked(self):
        self.parent.log(self.netState.get())