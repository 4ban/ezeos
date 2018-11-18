#!/usr/bin/env python
# coding: utf-8

import os

VERSION = "v0.0.1"

EZEOS='''
  ______   ______  ______    ____     _____ 
 |  ____| |___  / |  ____|  / __ \   / ____|
 | |__       / /  | |__    | |  | | | (___  
 |  __|     / /   |  __|   | |  | |  \___ \ 
 | |____   / /__  | |____  | |__| |  ____) |
 |______| /_____| |______|  \____/  |_____/ 
                                            
                                            '''


EZEOS_DIR = os.path.dirname(os.path.abspath(__file__))

ROOT_DIR = os.path.abspath(os.path.join(EZEOS_DIR, os.pardir))

CONFIG_PATH = os.path.join(ROOT_DIR, 'ezeos.conf')

MAIN_PRODUCERS = ['https://api.eosnewyork.io:443',
                  'https://api.eosdetroit.io:443',
                  'https://eos.greymass.com:443',
                  'https://api.eosmetal.io:18890',
                  'http://api.hkeos.com:80',
                  'https://eosapi.blockmatrix.network:443',
                  'https://fn.eossweden.se:443',
                  'http://api.blockgenicbp.com:8888',
                  'http://mainnet.eoscalgary.io:80',
                  'http://mainnet.eoscalgary.io:80',
                  'https://node1.eosphere.io',
                  'https://eos.saltblock.io',
                  'http://eos-api.worbli.io:80',
                  'https://eos-api.worbli.io:443',
                  'http://mainnet.eoscalgary.io:80',
                  'https://user-api.eoseoul.io:443',
                  'http://user-api.eoseoul.io:80',
                  'https://node2.liquideos.com:8883',
                  'http://node2.liquideos.com:8888',
                  'https://api.eosuk.io:443',
                  'http://api1.eosdublin.io:80',
                  'http://api.eosvibes.io:80',
                  'http://api.cypherglass.com:8888',
                  'https://api.cypherglass.com:443',
                  'http://bp.cryptolions.io:8888',
                  'http://dc1.eosemerge.io:8888',
                  'https://dc1.eosemerge.io:5443',
                  'https://api.eosio.cr:443',
                  'https://api.eosn.io',
                  'https://eu1.eosdac.io:443']

TEST_PRODUCERS = ['http://api.kylin.alohaeos.com',
                  'http://127.0.0.1:8888',
                  'http://35.183.129.78:8080']

PRODUCER = ''
