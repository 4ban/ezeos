#!/usr/bin/env python
# coding: utf-8

from tkinter import Tk
from gui.ui import UI
from ezeos import DOCKER_CONTAINER_NAME
from ezeos import TIMEOUT
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
        cleos = ['docker', 'exec', DOCKER_CONTAINER_NAME,
                 '/opt/eosio/bin/cleos']


# Logic functions
def getProducerInfo():
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(), 'get', 'info'],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Producer is not available\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not get info.\n' + str(e)
    finally:
        app.outputPanel.logger(out)


def getBlockInfo():
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(),
                                      'get', 'block', app.tabPanel.blockNumber.get()],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not get block info\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not get block info.\n' + str(e)
    finally:
        app.outputPanel.logger(out)


def getBlockProducers():
    try:
        out = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(),
                                      'system', 'listproducers'],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not get producer list\n' + str(e)
    except Exception as e:
        print(e)
        out = "Could not get producer list.\n" + str(e)
    finally:
        app.outputPanel.logger(out)


def getWalletList():
    try:
        out = subprocess.run(cleos + ['wallet', 'list'],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not get wallet list\n' + str(e)
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
                out = subprocess.run(cleos + ['wallet', 'create', '-n', app.tabPanel.walletName.get(),
                                              '--to-console'],
                                     timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                out = out.stdout.decode('utf-8')
            elif toConsole == '--file':
                out = subprocess.run(cleos + ['wallet', 'create', '-n', app.tabPanel.walletName.get(),
                                              '--file', "/root/" + app.tabPanel.walletName.get()],
                                     timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                out = out.stdout.decode('utf-8')
        except subprocess.TimeoutExpired as e:
            print(e)
            out = 'Timeout. Can not create wallet\n' + str(e)
        except Exception as e:
            print(e)
            out = "Could not create wallet.\n" + str(e)
        finally:
            app.tabPanel.openWalletName.insert(0, app.tabPanel.walletName.get())
            app.outputPanel.logger(out)
    else:
        walletDir = os.environ['HOME'] + '/eosio-wallet'
        if not os.path.exists(walletDir):
            os.makedirs(walletDir)
        try:
            if toConsole == '--to-console':
                out = subprocess.run(cleos + ['wallet', 'create', '-n', app.tabPanel.walletName.get(),
                                              '--to-console'],
                                     timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                out = out.stdout.decode('utf-8')
            elif toConsole == '--file':
                out = subprocess.run(cleos + ['wallet', 'create', '-n', app.tabPanel.walletName.get(),
                                              '--file', walletDir + "/" + app.tabPanel.walletName.get()],
                                     timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                out = out.stdout.decode('utf-8')
        except subprocess.TimeoutExpired as e:
            print(e)
            out = 'Timeout. Can not create wallet\n' + str(e)
        except Exception as e:
            print(e)
            out = "Could not create wallet.\n" + str(e)
        finally:
            app.tabPanel.openWalletName.insert(0, app.tabPanel.walletName.get())
            app.outputPanel.logger(out)


def openWallet():
    try:
        out = subprocess.run(cleos + ['wallet', 'open', '-n', app.tabPanel.openWalletName.get()],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not open the wallet\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not open the wallet.\n' + str(e)
    finally:
        if 'Opened' in out:
            out += "\nRemember this wallet as default for this ezeos session!"
        app.outputPanel.logger(out)


def unlockWallet(password):
    try:
        out = subprocess.run(cleos + ['wallet', 'unlock', '-n', app.tabPanel.openWalletName.get(), '--password', password],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Unlock the wallet\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not unlock the wallet.\n' + str(e)
    finally:
        app.outputPanel.logger(out)


def showKeys():
    try:
        out = subprocess.run(cleos + ['wallet', 'keys'],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not show keys\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not show keys.\n' + str(e)
    finally:
        app.outputPanel.logger(out)


def showPrivateKeys(password):
    try:
        out = subprocess.run(cleos + ['wallet', 'private_keys', '-n', app.tabPanel.openWalletName.get(), '--password', password],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not show private keys\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not show private keys.\n' + str(e)
    finally:
        app.outputPanel.logger(out)


def importKey(key):
    try:
        out = subprocess.run(cleos + ['wallet', 'import', '-n', app.tabPanel.openWalletName.get(), '--private-key', key],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not import the key\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not import the key.\n' + str(e)
    finally:
        app.outputPanel.logger(out)


def createKeys():
    # TODO add --tofile feature
    try:
        out = subprocess.run(cleos + ['create', 'key', '--to-console'],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not create keys\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not create keys.\n' + str(e)
    finally:
        app.outputPanel.logger(out)


def compileContract():
    cpp = app.tabPanel.contractFileCPP.get()
    wasm = app.tabPanel.contractFileWASM.get()
    wast = app.tabPanel.contractFileWAST.get()
    abi = app.tabPanel.contractFileABI.get()

    try:
        out = subprocess.run(['eosio-cpp', '-o', wasm, cpp, '--abigen'],
                             timeout=TIMEOUT+60, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not compile contract\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not compile contract.\n' + str(e)
    finally:
        if 'error' in out:
            app.outputPanel.logger(out)
        else:
            app.outputPanel.logger("Compile successful\n\n" + out)

    try:
        out = subprocess.run(['eosio-cpp', '-o', wast, cpp, '--abigen'],
                             timeout=TIMEOUT+60, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = out.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not compile contract\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not compile contract.\n' + str(e)
    finally:
        if 'error' in out:
            app.outputPanel.logger(out)
        else:
            app.outputPanel.logger("Compile successful\n\n" + out)

def setContract():
    cpp = app.tabPanel.contractFileCPP.get()
    wasm = app.tabPanel.contractFileWASM.get()
    wast = app.tabPanel.contractFileWAST.get()
    abi = app.tabPanel.contractFileABI.get()

    try:
        out_code = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(), 'set', 'code', app.tabPanel.accountName.get(), wasm],
                             timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out_abi = subprocess.run(cleos + ['--url', app.tabPanel.producer.get(), 'set', 'abi', app.tabPanel.accountName.get(), abi],
            timeout=TIMEOUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out_code = out_code.stdout.decode('utf-8')
        out_abi = out_abi.stdout.decode('utf-8')
        out = str(out_code) + str(out_abi)
    except subprocess.TimeoutExpired as e:
        print(e)
        out = 'Timeout. Can not set contract\n' + str(e)
    except Exception as e:
        print(e)
        out = 'Could not set contract.\n' + str(e)
    finally:
        app.outputPanel.logger("Contract successfully pished to the net.\n\n" + out)

