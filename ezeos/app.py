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
    # TODO move to __init__ or conf file
    DOCKER_CONTAINER_NAME = 'eos'
    global DOCKER_COMMAND

    DOCKER_COMMAND = ['docker', 'exec', DOCKER_CONTAINER_NAME]
    CLEOS_COMMAND = ['/opt/eosio/bin/cleos', '-h']
    global cleos

    try:
        subprocess.check_output(DOCKER_COMMAND+CLEOS_COMMAND)
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
        out = out.stdout.decode('utf-8')
    except Exception as e:
        print(e)
        out = 'Could not get info.\n' + str(e)
    finally:
        app.outputPanel.logger(out)


def getBlockInfo():
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(), 'get', 'block', app.tabPanel.blockNumber.get()], stdout=subprocess.PIPE)
        out = out.stdout.decode('utf-8')
    except Exception as e:
        print(e)
        out = 'Could not get block info.\n' + str(e)
    finally:
        app.outputPanel.logger(out)


def getBlockProducers():
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(), 'system', 'listproducers'], stdout=subprocess.PIPE)
        out = out.stdout.decode('utf-8')
    except Exception as e:
        print(e)
        out = "Could not get producer list.\n" + str(e)
    finally:
        app.outputPanel.logger(out)


def getWalletList():
    try:
        out = subprocess.run(cleos + ['wallet', 'list'], stdout=subprocess.PIPE)
        out = out.stdout.decode('utf-8')
    except Exception as e:
        print(e)
        out = "Could not get wallet list. \n" + str(e)
    finally:
        app.outputPanel.logger(out)


def getWalletListFilesystem():
    if 'docker' in cleos:
        # docker exec eos ls /root/eosio-wallet | egrep '\.wallet$'
        out = b"Found wallets in filesystem inside docker container:\n> /root/eosio-wallet\n\n"
        com = " ".join(DOCKER_COMMAND + ['ls', '/root/eosio-wallet', '|', 'egrep', '\.wallet$'])
        out += subprocess.check_output(com, shell=True)
    else:
        # ls ~/eosio-wallet | egrep '\.wallet$'
        out = b"Found wallets in filesystem:\n> ~/eosio-wallet\n\n"
        com = " ".join(['ls', '~/eosio-wallet', '|', 'egrep', '\.wallet$'])
        out += subprocess.check_output(com, shell=True)

    app.outputPanel.logger(out)


def createWallet():
    toConsole = app.tabPanel.toConsole.get()

    if 'docker' in cleos:
        # docker - cleos wallet create -n twal --file /root/twal saved indide docker /root/
        try:
            if toConsole == '--to-console':
                out = subprocess.run(cleos + ['wallet', 'create', '-n', app.tabPanel.walletName.get(), '--to-console'], stdout=subprocess.PIPE)
                out = out.stdout.decode('utf-8')
            elif toConsole == '--file':
                out = subprocess.run(cleos + ['wallet', 'create', '-n', app.tabPanel.walletName.get(), '--file', "/root/" + app.tabPanel.walletName.get()], stdout=subprocess.PIPE)
                out = out.stdout.decode('utf-8')
        except Exception as e:
            print(e)
            out = "Could not create wallet.\n" + str(e)
        finally:
            app.outputPanel.logger(out)
    else:
        walletDir = os.environ['HOME'] + '/eosio-wallet'
        if not os.path.exists(walletDir):
            os.makedirs(walletDir)
        try:
            if toConsole == '--to-console':
                out = subprocess.run(cleos + ['wallet', 'create', '-n', app.tabPanel.walletName.get(), '--to-console'], stdout=subprocess.PIPE)
                out = out.stdout.decode('utf-8')
            elif toConsole == '--file':
                out = subprocess.run(cleos + ['wallet', 'create', '-n', app.tabPanel.walletName.get(), '--file', walletDir + "/" + app.tabPanel.walletName.get()], stdout=subprocess.PIPE)
                out = out.stdout.decode('utf-8')
        except Exception as e:
            print(e)
            out = "Could not create wallet.\n" + str(e)
        finally:
            app.outputPanel.logger(out)
