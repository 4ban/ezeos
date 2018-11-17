#!/usr/bin/env python
# coding: utf-8

from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk


class UI:
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
        self.menubar()
        # Add status bar
        self.status = StatusBar(self.root)
        self.status.pack(side=TOP, fill=X)
        # Add tab panel
        self.tabpanel()
        # Add output panel
        self.outputpanel()
        # Fill the tabs
        self.tabFill = TabFill()

    def menubar(self):
        menubar = Menu(self.root,
                       bg="#2D2D46",
                       fg="#dfdfdf",
                       activebackground='#4E4E7B',
                       activeforeground='#dfdfdf',
                       bd=0)
        # Set logo
        logo = Image.open("../resources/icon.png")
        logo = logo.resize((20, 20), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(logo)

        # File menu
        filemenu = Menu(menubar,
                        tearoff=0,
                        bg="#2D2D46",
                        fg="#dfdfdf",
                        activebackground='#4E4E7B',
                        activeforeground='#dfdfdf',
                        bd=0)
        filemenu.add_command(label="Exit", command=self.root.quit)
        # Help menu
        helpmenu = Menu(menubar,
                        tearoff=0,
                        bg="#2D2D46",
                        fg="#dfdfdf",
                        activebackground='#4E4E7B',
                        activeforeground='#dfdfdf',
                        bd=0)
        helpmenu.add_command(label="About", command=self.about)
        # Add menus to menubar
        menubar.add_cascade(label="Ezeos", image=self.logo, menu=filemenu)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # Attach menu
        self.root.config(menu=menubar)

    def tabpanel(self):
        style = ttk.Style(self.root)
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

        self.notebook = ttk.Notebook(self.root, style='TNotebook')

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

    def outputpanel(self):
        # make a text box to put the serial output
        self.log = Text(self.root, takefocus=0,
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
        self.log.pack(expand=True, fill='both')

    def logger(self, message):
        self.log.delete('0.0', END)
        self.log.insert('0.0', message)

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
