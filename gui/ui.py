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
        # Add menubar
        self.menubar()
        # Add status bar
        self.status = StatusBar(self.root)
        self.status.pack(side=TOP, fill=X)
        # Add tab panel
        self.tabpanel()
        # Add output panel
        self.outputpanel()

    def menubar(self):
        menubar = Menu(self.root)
        # Set logo
        logo = Image.open("../resources/icon.png")
        logo = logo.resize((20, 20), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(logo)

        # File menu
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.root.quit)
        # Help menu
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=about)
        # Add menus to menubar
        menubar.add_cascade(label="Ezeos", image=self.logo, menu=filemenu)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # Attach menu
        self.root.config(menu=menubar)

    def tabpanel(self):
        style = ttk.Style(self.root)
        # style.configure('lefttab.TNotebook', tabposition='wn')
        self.notebook = ttk.Notebook(self.root, style='lefttab.TNotebook')

        tab1 = Frame(self.notebook)
        tab2 = Frame(self.notebook)
        tab3 = Frame(self.notebook)
        tab4 = Frame(self.notebook)
        tab5 = Frame(self.notebook)
        tab6 = Frame(self.notebook)
        tab7 = Frame(self.notebook)
        tab8 = Frame(self.notebook)
        tab9 = Frame(self.notebook)
        tab10 = Frame(self.notebook)
        tab11 = Frame(self.notebook)
        tab12 = Frame(self.notebook)

        self.notebook.add(tab1, text='Block Chain')
        self.notebook.add(tab2, text='Wallets')
        self.notebook.add(tab3, text='Accounts')
        self.notebook.add(tab4, text='Contracts')

        self.notebook.pack(expand=1, fill='both')

    def outputpanel(self):
        # make a text box to put the serial output
        self.log = Text(self.root, takefocus=0)
        self.log.pack(fill=X)

        # make a scrollbar
        scrollbar = Scrollbar(self.log)
        scrollbar.pack(side=RIGHT, fill=Y)
        # attach text box to scrollbar
        self.log.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.log.yview)


class StatusBar(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)

    def set(self, format, *args):
        self.label.config(text="> "+format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()


# Additional functions
def about():
    print("about")
