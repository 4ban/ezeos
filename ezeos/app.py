#!/usr/bin/env python
# coding: utf-8

from tkinter import Tk
from gui.ui import UI
import subprocess
import os


def run():
    global app
    root = Tk()
    app = UI(root)
    # Application
    getCleosCommand()
    # print(app.tabPanel.producer.get())
    root.mainloop()


def getCleosCommand():
    DOCKER_CONTAINER_NAME = 'eos'
    DOCKER_COMMAND = ['docker', 'exec', DOCKER_CONTAINER_NAME, '/opt/eosio/bin/cleos', '-h']
    global cleos

    try:
        subprocess.check_output(DOCKER_COMMAND)
    except OSError as e:
        cleos = ['cleos']
    except Exception as e:
        cleos = ['cleos']
    else:
        cleos = ['docker', 'exec', DOCKER_CONTAINER_NAME, '/opt/eosio/bin/cleos']


# Logic functions
def getProducerInfo():
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(), 'get', 'info'], stdout=subprocess.PIPE)
    except Exception as e:
        print(e)
        print('\nCould not get info')
    else:
        out = out.stdout.decode('utf-8')
        app.outputPanel.logger(out)


def getBlockInfo():
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(), 'get', 'block', app.tabPanel.blockNumber.get()], stdout=subprocess.PIPE)
    except Exception as e:
        print(e)
        print('\nCould not get block info')
    else:
        out = out.stdout.decode('utf-8')
        app.outputPanel.logger(out)


def getBlockProducers():
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(), 'system', 'listproducers'], stdout=subprocess.PIPE)
    except Exception as e:
        print(e)
        print("\nCould not get producer list")
    else:
        out = out.stdout.decode('utf-8')
        app.outputPanel.logger(out)
