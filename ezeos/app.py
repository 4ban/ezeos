#!/usr/bin/env python
# coding: utf-8

from tkinter import Tk
from gui.ui import UI
import subprocess
import os


def run():
    global app
    global cleos
    root = Tk()
    app = UI(root)
    # Application
    getCleosCommand()
    # print(app.tabPanel.producer.get())
    root.mainloop()


def getCleosCommand():
    DOCKER_CONTAINER_NAME = 'eos'
    DOCKER_COMMAND = ['docker', 'exec', DOCKER_CONTAINER_NAME, '/opt/eosio/bin/cleos', '-h']

    try:
        subprocess.check_output(DOCKER_COMMAND)
    except OSError as e:
        cleos = ['cleos']
    except Exception as e:
        cleos = ['cleos']
    else:
        cleos = ['docker', 'exec', DOCKER_CONTAINER_NAME, '/opt/eosio/bin/cleos']


def getBlockInfo():
    print("dmitry")
    # out = ''
    # try:
    #     out = subprocess.check_output(cleos + ['--url', app.tabPanel.producer.get(), 'get', 'block', app.tabPanel.block.number])
    #     out = out.decode("utf-8")
    # except Exception as e:
    #     print(e)
    #     print('\nCould not get block info')


