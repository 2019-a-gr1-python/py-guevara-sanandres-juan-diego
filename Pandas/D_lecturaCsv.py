# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:33 2019

@author: junt_
"""

import numpy as np
import pandas as pd
import os

# 1) Csv, Jason, HTML, XML
# 2) Binary
# 3) Relational Databases

path = "Z://junt_//Documents//7mo//Python//Pandas//Data//pokemon.csv"

df_one = pd.read_csv(
        path,
        nrows = 10)

columnas = ['#','Name','Type 1','Total','Attack','Defense','Sp. Atk','Sp. Def','Speed']

df_dos = pd.read_csv(
        path,
        nrows = 10,
        usecols = columnas,
        index_col = '#')

df_tres = pd.read_csv(path)

save_path = "Z://junt_//Documents//7mo//Python//Pandas//Data//pokemon_completo.pickle"

df_tres.to_pickle(save_path)

df_cuatro = pd.read_pickle(save_path)