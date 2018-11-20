#!/usr/bin/env python
# coding: utf-8

import os
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import filedialog
from ezeos import MAIN_PRODUCERS
from ezeos import TEST_PRODUCERS
import ezeos.app as ezeos


class TabPanel(object):
    def __init__(self, parent):
        self.parent = parent
        # Variables tab 1
        self.netState = IntVar()
        self.producer = StringVar()
        self.blockNumber = StringVar()
        # Variables tab 2
        self.toConsole = StringVar()
        self.walletName = StringVar()
        self.openWalletName = StringVar()

        # Variables tab 3
        # Variables tab 4
        self.contractFileCPP = StringVar()
        self.contractFileWASM = StringVar()
        self.contractFileWAST = StringVar()
        self.contractFileABI = StringVar()

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
                              ("active", "#dfdfdf")])

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
                        foreground="#dfdfdf",
                        highlightbackground="#232323",
                        highlightcolor="#0000ff",
                        selectcolor="#232323")

        style.configure('TSeparator',
                        background="#2D2D46")

        self.notebook = ttk.Notebook(self.parent.root, style='TNotebook')

        self.tab1 = ttk.Frame(self.notebook, style='TFrame')
        self.tab2 = ttk.Frame(self.notebook, style='TFrame')
        self.tab3 = ttk.Frame(self.notebook, style='TFrame')
        self.tab4 = ttk.Frame(self.notebook, style='TFrame')

        self.notebook.add(self.tab1, text='Block Chain')
        self.notebook.add(self.tab2, text='Wallets')
        self.notebook.add(self.tab3, text='Accounts')
        self.notebook.add(self.tab4, text='Contracts')

        self.notebook.pack(expand=True, fill='both')
        self.notebook.select(self.tab3)

    def fillTab1(self):
        self.netState.set(2)
        self.producer.set(TEST_PRODUCERS[0])
        # TODO move everything to the label frames
        # network
        networkFrame = LabelFrame(self.tab1,
                                  text="Network",
                                  background="#2D2D46",
                                  foreground='#dfdfdf',
                                  borderwidth=2)
        networkFrame.grid(row=0, column=0, sticky=NSEW, pady=5, ipady=5, ipadx=5)

        mainNet = Radiobutton(networkFrame, text='Main Net', value=1, variable=self.netState,
                              background="#4E4E7B",
                              foreground='#dfdfdf',
                              activebackground="#c9c9d7",
                              highlightbackground="#4E4E7B",
                              highlightcolor="#4E4E7B",
                              selectcolor="#27a768",
                              indicatoron=0,
                              height=2,
                              width=10,
                              highlightthickness=0,
                              borderwidth=0,
                              command=self.update_tab1)
        testNet = Radiobutton(networkFrame, text='Test Net', value=2, variable=self.netState,
                              background="#4E4E7B",
                              foreground='#dfdfdf',
                              activebackground="#c9c9d7",
                              highlightbackground="#4E4E7B",
                              highlightcolor="#4E4E7B",
                              selectcolor="#27a768",
                              indicatoron=0,
                              height=2,
                              width=10,
                              highlightthickness=0,
                              borderwidth=0,
                              command=self.update_tab1)

        self.mainNetList = OptionMenu(networkFrame, self.producer, *MAIN_PRODUCERS)
        self.mainNetList.configure(state="disabled",
                                   background="#4E4E7B",
                                   foreground="#dfdfdf",
                                   highlightbackground="#2D2D46",
                                   highlightcolor="#2D2D46",
                                   highlightthickness=0,
                                   borderwidth=0,
                                   width=25,
                                   indicatoron=0,
                                   activebackground="#c9c9d7",
                                   activeforeground="#232323",
                                   disabledforeground="#4E4E7B",
                                   relief="flat")
        self.mainNetList["menu"].configure(background="#4E4E7B",
                                           foreground="#dfdfdf",
                                           borderwidth=0,
                                           activebackground="#c9c9d7",
                                           activeforeground="#232323")

        self.testNetList = OptionMenu(networkFrame, self.producer, *TEST_PRODUCERS)
        self.testNetList.configure(state="normal",
                                   background="#4E4E7B",
                                   foreground="#dfdfdf",
                                   highlightbackground="#2D2D46",
                                   highlightcolor="#2D2D46",
                                   highlightthickness=0,
                                   borderwidth=0,
                                   width=25,
                                   indicatoron=0,
                                   activebackground="#c9c9d7",
                                   activeforeground="#232323",
                                   disabledforeground="#4E4E7B",
                                   relief="flat")
        self.testNetList["menu"].configure(background="#4E4E7B",
                                           foreground="#dfdfdf",
                                           borderwidth=0,
                                           activebackground="#c9c9d7",
                                           activeforeground="#232323")

        mainNet.grid(row=0, column=0, padx=5, pady=5)
        self.mainNetList.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        testNet.grid(row=1, column=0, padx=5, pady=5)
        self.testNetList.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        currentProducer = Button(networkFrame,
                                 text="Show current producer",
                                 command=self.show_current_producer,
                                 background="#4E4E7B",
                                 foreground="#dfdfdf",
                                 highlightbackground="#2D2D46",
                                 highlightcolor="#2D2D46",
                                 highlightthickness=0,
                                 borderwidth=0,
                                 height=1,
                                 activebackground="#c9c9d7",
                                 activeforeground="#232323",
                                 disabledforeground="#4E4E7B",
                                 relief="flat")
        currentProducer.grid(row=0, column=3, rowspan=2, padx=5, pady=5, ipady=5)

        # Block
        blockFrame = LabelFrame(self.tab1,
                                text="Block",
                                background="#2D2D46",
                                foreground='#dfdfdf',
                                borderwidth=2)
        blockFrame.grid(row=0, column=1, sticky=NSEW, padx=5, pady=5, ipady=5, ipadx=5)

        # setBlockNumber
        blockNumberLabel = Label(blockFrame, text="Enter block number:",
                                 background="#2D2D46",
                                 foreground="#dfdfdf")
        blockNumberLabel.grid(row=0, column=0)
        self.blockNumber = Entry(blockFrame, width=12,
                                 background="#dfdfdf",
                                 foreground="#232323",
                                 highlightthickness=0,
                                 borderwidth=0)
        self.blockNumber.insert(END, '1')
        self.blockNumber.grid(row=0, column=1, ipadx=3, padx=5, ipady=3, sticky=EW)

        # getBlockInfo
        blockInfo = Button(blockFrame,
                           text="Block info",
                           command=ezeos.getBlockInfo,
                           background="#4E4E7B",
                           foreground="#dfdfdf",
                           highlightbackground="#2D2D46",
                           highlightcolor="#2D2D46",
                           highlightthickness=0,
                           borderwidth=0,
                           height=1,
                           activebackground="#c9c9d7",
                           activeforeground="#232323",
                           disabledforeground="#4E4E7B",
                           relief="flat")
        blockInfo.grid(row=0, column=2, ipady=5, sticky=EW)

        # getProducerInfo
        info = Button(blockFrame,
                      text="Get producer info",
                      command=ezeos.getProducerInfo,
                      background="#4E4E7B",
                      foreground="#dfdfdf",
                      highlightbackground="#2D2D46",
                      highlightcolor="#2D2D46",
                      highlightthickness=0,
                      borderwidth=0,
                      height=1,
                      activebackground="#c9c9d7",
                      activeforeground="#232323",
                      disabledforeground="#4E4E7B",
                      relief="flat")
        info.grid(row=1, column=0, padx=5, pady=5, ipady=5, sticky=EW)

        # get block Producers
        blockProducers = Button(blockFrame,
                                text="Get producers list",
                                command=ezeos.getBlockProducers,
                                background="#4E4E7B",
                                foreground="#dfdfdf",
                                highlightbackground="#2D2D46",
                                highlightcolor="#2D2D46",
                                highlightthickness=0,
                                borderwidth=0,
                                height=1,
                                activebackground="#c9c9d7",
                                activeforeground="#232323",
                                disabledforeground="#4E4E7B",
                                relief="flat")
        blockProducers.grid(row=1, column=1, padx=5, pady=5, ipady=5, sticky=EW)

    def fillTab2(self):
        self.toConsole.set('--to-console')
        # wallet creation
        createWalletFrame = LabelFrame(self.tab2,
                                       text="Create wallet",
                                       background="#2D2D46",
                                       foreground='#dfdfdf',
                                       borderwidth=2)
        createWalletFrame.grid(row=0, column=0, sticky=NSEW, pady=5, ipady=5, ipadx=5, columnspan=2)
        # set wallet name
        walletNameLabel = Label(createWalletFrame, text="Enter wallet name: ",
                                background="#2D2D46",
                                foreground="#dfdfdf")
        walletNameLabel.grid(row=0, column=0)
        self.walletName = Entry(createWalletFrame, width=20,
                                background="#dfdfdf",
                                foreground="#232323",
                                highlightthickness=0,
                                borderwidth=0)
        self.walletName.insert(END, 'default')
        self.walletName.grid(row=0, column=1, ipady=3, ipadx=3)

        toConsole = Radiobutton(createWalletFrame, text='To console', value='--to-console', variable=self.toConsole,
                                background="#4E4E7B",
                                foreground='#dfdfdf',
                                activebackground="#c9c9d7",
                                highlightbackground="#4E4E7B",
                                highlightcolor="#4E4E7B",
                                selectcolor="#27a768",
                                indicatoron=0,
                                height=2,
                                width=10,
                                highlightthickness=0,
                                borderwidth=0)
        toFile = Radiobutton(createWalletFrame, text='To file', value='--file', variable=self.toConsole,
                             background="#4E4E7B",
                             foreground='#dfdfdf',
                             activebackground="#c9c9d7",
                             highlightbackground="#4E4E7B",
                             highlightcolor="#4E4E7B",
                             selectcolor="#27a768",
                             indicatoron=0,
                             height=2,
                             width=10,
                             highlightthickness=0,
                             borderwidth=0)
        toConsole.grid(row=0, column=2, padx=5, pady=5)
        toFile.grid(row=0, column=3, padx=5, pady=5)

        # create wallet
        createWallet = Button(createWalletFrame,
                              text="Create wallet",
                              command=ezeos.createWallet,
                              background="#4E4E7B",
                              foreground="#dfdfdf",
                              highlightbackground="#2D2D46",
                              highlightcolor="#2D2D46",
                              highlightthickness=0,
                              borderwidth=0,
                              height=1,
                              activebackground="#c9c9d7",
                              activeforeground="#232323",
                              disabledforeground="#4E4E7B",
                              relief="flat")
        createWallet.grid(row=0, column=4, padx=5, ipady=5)

        # wallet operations
        walletFrame = LabelFrame(self.tab2,
                                 text="Wallet operations",
                                 background="#2D2D46",
                                 foreground='#dfdfdf',
                                 borderwidth=2)
        walletFrame.grid(row=1, column=0, sticky=NSEW, pady=5, ipady=5, ipadx=5)

        # get wallet list (filesystem)
        walletListFilesystem = Button(walletFrame,
                                      text="List wallets (filesystem)",
                                      command=ezeos.getWalletListFilesystem,
                                      background="#4E4E7B",
                                      foreground="#dfdfdf",
                                      highlightbackground="#2D2D46",
                                      highlightcolor="#2D2D46",
                                      highlightthickness=0,
                                      borderwidth=0,
                                      height=1,
                                      activebackground="#c9c9d7",
                                      activeforeground="#232323",
                                      disabledforeground="#4E4E7B",
                                      relief="flat")
        walletListFilesystem.grid(row=0, column=0, padx=5, ipady=5, sticky=EW)
        # get wallet list (cleos)
        walletList = Button(walletFrame,
                            text="List wallets",
                            command=ezeos.getWalletList,
                            background="#4E4E7B",
                            foreground="#dfdfdf",
                            highlightbackground="#2D2D46",
                            highlightcolor="#2D2D46",
                            highlightthickness=0,
                            borderwidth=0,
                            height=1,
                            activebackground="#c9c9d7",
                            activeforeground="#232323",
                            disabledforeground="#4E4E7B",
                            relief="flat")
        walletList.grid(row=0, column=1, padx=5, ipady=5, sticky=EW)

        currentWallet = Button(walletFrame,
                            text="Get current wallet",
                            command=self.currentWallet,
                            background="#4E4E7B",
                            foreground="#dfdfdf",
                            highlightbackground="#2D2D46",
                            highlightcolor="#2D2D46",
                            highlightthickness=0,
                            borderwidth=0,
                            height=1,
                            activebackground="#c9c9d7",
                            activeforeground="#232323",
                            disabledforeground="#4E4E7B",
                            relief="flat")
        currentWallet.grid(row=0, column=2, padx=5, ipady=5, sticky=EW)

        # Open wallet (filesystem)
        self.openWalletName = Entry(walletFrame, width=20,
                                background="#dfdfdf",
                                foreground="#232323",
                                highlightthickness=0,
                                borderwidth=0)
        self.openWalletName.grid(row=1, column=0, ipadx=3, ipady=3, padx=5, pady=5, sticky=EW)
        openWallet = Button(walletFrame,
                                      text="Open wallet",
                                      command=ezeos.openWallet,
                                      background="#4E4E7B",
                                      foreground="#dfdfdf",
                                      highlightbackground="#2D2D46",
                                      highlightcolor="#2D2D46",
                                      highlightthickness=0,
                                      borderwidth=0,
                                      height=1,
                                      activebackground="#c9c9d7",
                                      activeforeground="#232323",
                                      disabledforeground="#4E4E7B",
                                      relief="flat")
        openWallet.grid(row=1, column=1, padx=5, ipady=5, pady=5, sticky=EW)

        unlockWallet = Button(walletFrame,
                            text="Unlock wallet",
                            command=self.unlockWallet,
                            background="#4E4E7B",
                            foreground="#dfdfdf",
                            highlightbackground="#2D2D46",
                            highlightcolor="#2D2D46",
                            highlightthickness=0,
                            borderwidth=0,
                            height=1,
                            activebackground="#c9c9d7",
                            activeforeground="#232323",
                            disabledforeground="#4E4E7B",
                            relief="flat")
        unlockWallet.grid(row=1, column=2, padx=5, ipady=5, pady=5, sticky=EW)

        # wallet keys
        self.walletKeyFrame = LabelFrame(self.tab2,
                                 text="Keys operations",
                                 background="#2D2D46",
                                 foreground='#dfdfdf',
                                 borderwidth=2)
        self.walletKeyFrame.grid(row=1, column=1, sticky=NSEW, pady=5, padx=5, ipady=5, ipadx=5)
        # show keys
        showKeys = Button(self.walletKeyFrame,
                            text="Show public keys",
                            command=ezeos.showKeys,
                            background="#4E4E7B",
                            foreground="#dfdfdf",
                            highlightbackground="#2D2D46",
                            highlightcolor="#2D2D46",
                            highlightthickness=0,
                            borderwidth=0,
                            height=1,
                            activebackground="#c9c9d7",
                            activeforeground="#232323",
                            disabledforeground="#4E4E7B",
                            relief="flat")
        showKeys.grid(row=0, column=0, padx=5, ipady=5, pady=5, sticky=W)

        showPrivateKeys = Button(self.walletKeyFrame,
                          text="Show private keys",
                          command=self.showPrivateKeys,
                          background="#4E4E7B",
                          foreground="#dfdfdf",
                          highlightbackground="#2D2D46",
                          highlightcolor="#2D2D46",
                          highlightthickness=0,
                          borderwidth=0,
                          height=1,
                          activebackground="#c9c9d7",
                          activeforeground="#232323",
                          disabledforeground="#4E4E7B",
                          relief="flat")
        showPrivateKeys.grid(row=0, column=1, padx=5, ipady=5, pady=5, sticky=EW)

        createKeys = Button(self.walletKeyFrame,
                                   text="Create key pair",
                                   command=ezeos.createKeys,
                                   background="#4E4E7B",
                                   foreground="#dfdfdf",
                                   highlightbackground="#2D2D46",
                                   highlightcolor="#2D2D46",
                                   highlightthickness=0,
                                   borderwidth=0,
                                   height=1,
                                   activebackground="#c9c9d7",
                                   activeforeground="#232323",
                                   disabledforeground="#4E4E7B",
                                   relief="flat")
        createKeys.grid(row=1, column=0, padx=5, ipady=5, pady=5, sticky=EW)

        importPrivateKeys = Button(self.walletKeyFrame,
                                 text="Import key",
                                 command=self.importKey,
                                 background="#4E4E7B",
                                 foreground="#dfdfdf",
                                 highlightbackground="#2D2D46",
                                 highlightcolor="#2D2D46",
                                 highlightthickness=0,
                                 borderwidth=0,
                                 height=1,
                                 activebackground="#c9c9d7",
                                 activeforeground="#232323",
                                 disabledforeground="#4E4E7B",
                                 relief="flat")
        importPrivateKeys.grid(row=1, column=1, padx=5, ipady=5, pady=5, sticky=EW)




        #unlock wallet
        # import keys

        # # delete
        # testBtn2 = Button(self.tab2,
        #                   text="test",
        #                   command=self.test,
        #                   background="#232323",
        #                   foreground="#dfdfdf",
        #                   highlightbackground="#2D2D46",
        #                   highlightcolor="#2D2D46",
        #                   highlightthickness=0,
        #                   borderwidth=0,
        #                   height=1,
        #                   activebackground="#c9c9d7",
        #                   activeforeground="#232323",
        #                   disabledforeground="#4E4E7B",
        #                   relief="flat")
        # testBtn2.grid(row=4, column=3, padx=5, pady=5)

    def fillTab3(self):
        pass

    def fillTab4(self):
        # Contract operations
        self.contractFrame = LabelFrame(self.tab4,
                                 text="Contract operations",
                                 background="#2D2D46",
                                 foreground='#dfdfdf',
                                 borderwidth=2)
        self.contractFrame.grid(row=0, column=0, sticky=NSEW, pady=5, ipady=5, ipadx=5)

        # Open contract
        openContract = Button(self.contractFrame,
                                      text="Open contract",
                                      command=self.openContract,
                                      background="#4E4E7B",
                                      foreground="#dfdfdf",
                                      highlightbackground="#2D2D46",
                                      highlightcolor="#2D2D46",
                                      highlightthickness=0,
                                      borderwidth=0,
                                      height=1,
                                      activebackground="#c9c9d7",
                                      activeforeground="#232323",
                                      disabledforeground="#4E4E7B",
                                      relief="flat")
        openContract.grid(row=0, column=0, padx=5, ipady=5, sticky=EW)

        # Compile contract
        compileContract = Button(self.contractFrame,
                              text="Compile contract",
                              command=ezeos.compileContract,
                              background="#4E4E7B",
                              foreground="#dfdfdf",
                              highlightbackground="#2D2D46",
                              highlightcolor="#2D2D46",
                              highlightthickness=0,
                              borderwidth=0,
                              height=1,
                              activebackground="#c9c9d7",
                              activeforeground="#232323",
                              disabledforeground="#4E4E7B",
                              relief="flat")
        compileContract.grid(row=0, column=1, padx=5, ipady=5, sticky=EW)

        # Set contract
        setContract = Button(self.contractFrame,
                                 text="Set contract",
                                 command=ezeos.setContract,
                                 background="#4E4E7B",
                                 foreground="#dfdfdf",
                                 highlightbackground="#2D2D46",
                                 highlightcolor="#2D2D46",
                                 highlightthickness=0,
                                 borderwidth=0,
                                 height=1,
                                 activebackground="#c9c9d7",
                                 activeforeground="#232323",
                                 disabledforeground="#4E4E7B",
                                 relief="flat")
        setContract.grid(row=0, column=2, padx=5, ipady=5, sticky=EW)

    def update_tab1(self):
        if self.netState.get() == 1:
            self.testNetList.configure(state="disabled")
            self.mainNetList.configure(state="normal")
        elif self.netState.get() == 2:
            self.testNetList.configure(state="normal")
            self.mainNetList.configure(state="disabled")

    def show_current_producer(self):
        mes = self.producer.get()
        self.parent.log(mes)

    def currentWallet(self):
        mes = self.openWalletName.get()
        self.parent.log(mes)

    def showPrivateKeys(self):
        password = simpledialog.askstring("Password", "Password from wallet", parent=self.walletKeyFrame)
        if password is not None:
            ezeos.showPrivateKeys(password)
        else:
            self.parent.log("Something went wrong!")

    def unlockWallet(self):
        password = simpledialog.askstring("Password", "Password from wallet", parent=self.walletKeyFrame)
        if password is not None:
            ezeos.unlockWallet(password)
        else:
            self.parent.log("Something went wrong!")

    def importKey(self):
        key = simpledialog.askstring("Import key", "Put import key", parent=self.walletKeyFrame)
        if key is not None:
            ezeos.importKey(key)
        else:
            self.parent.log("Something went wrong!")

    def openContract(self):
        # self.parent.style.theme_use('ubuntu')
        filetypes = [('C++', '.cpp')]
        file = filedialog.askopenfilename(parent=self.contractFrame,
                                          initialdir=os.getenv("HOME"),
                                          title="Please select a contract:",
                                          filetypes=filetypes)
        if file is not None:
            # self.parent.style.theme_use('default')
            self.contractFileCPP.set(file)
            self.contractFileWASM.set(file.replace('.cpp', '.wasm'))
            self.contractFileWAST.set(file.replace('.cpp', '.wast'))
            self.contractFileABI.set(file.replace('.cpp', '.abi'))
            self.parent.log("Opened contract:\n\n"+self.contractFileCPP.get())
        else:
            self.parent.log("Something went wrong!")

    # delete
    def test(self):
        mes = self.toConsole.get()+" "+self.walletName.get()
        self.parent.log(mes)

