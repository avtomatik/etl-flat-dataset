#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 20:48:13 2025

@author: alexandermikhailov
"""


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR.joinpath('data')

FILE_NAMES = (
    'dataset_usa_0000_public_debt.txt',
    'dataset_usa_0022_m1.txt',
    'dataset_usa_0025_p_r.txt',
)

FILE_NAME = 'dataset_usa_misc.csv'
