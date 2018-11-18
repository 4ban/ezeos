#!/usr/bin/env python
# coding: utf-8

from tkinter import *
from tkinter import ttk
from ezeos import MAIN_PRODUCERS
from ezeos import TEST_PRODUCERS
from ezeos import PRODUCER


class TabPanel(object):
    def __init__(self, parent):
        self.parent = parent
        # Variables
        self.netState = IntVar()
        self.producer = StringVar()

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

        style.configure('TRadiobutton',
                    background="#ff0000",
                    foreground='#dfdfdf',
                    highlightbackground="#232323",
                    highlightcolor="#0000ff",
                    selectcolor="#232323",
                    )

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
        self.producer.set(TEST_PRODUCERS[0])

        mainNet = Radiobutton(self.tab1, text='Main Net', value=1, variable=self.netState,
                              background="#4E4E7B",
                              foreground='#dfdfdf',
                              highlightbackground="#4E4E7B",
                              highlightcolor="#4E4E7B",
                              selectcolor="#27a768",
                              indicatoron=0,
                              command=self.update_tab1)
        testNet = Radiobutton(self.tab1, text='Test Net', value=2, variable=self.netState,
                              background="#4E4E7B",
                              foreground='#dfdfdf',
                              highlightbackground="#4E4E7B",
                              highlightcolor="#4E4E7B",
                              selectcolor="#27a768",
                              indicatoron=0,
                              command=self.update_tab1)

        self.mainNetList = OptionMenu(self.tab1, self.producer, *MAIN_PRODUCERS)
        self.testNetList = OptionMenu(self.tab1, self.producer, *TEST_PRODUCERS)

        mainNet.pack(side=LEFT, padx=5, pady=3, anchor=NW)
        self.mainNetList.pack(side=LEFT, padx=5, pady=3, anchor=NW)
        testNet.pack(side=LEFT, padx=5, pady=3, anchor=NW)
        self.testNetList.pack(side=LEFT, padx=5, pady=3, anchor=NW)
        self.testNetList.configure(state="disabled")
        self.mainNetList.configure(state="disabled")

        # delete
        btn = Button(self.tab1, text="Click Me", command=self.clicked)
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

    def update_tab1(self):
        if self.netState.get() == 1:
            self.testNetList.configure(state="disabled")
            self.mainNetList.configure(state="normal")
        elif self.netState.get() == 2:
            self.testNetList.configure(state="normal")
            self.mainNetList.configure(state="disabled")

    # delete
    def clicked(self):
        mes = self.producer.get()
        self.parent.log(mes)
