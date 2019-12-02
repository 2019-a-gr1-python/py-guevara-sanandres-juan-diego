# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:42:29 2019

@author: junt_
"""

import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

df_one = pd.DataFrame(arr_pand)
s_one = df_one[0]
s_new = pd.Series(np.random.randint(0,10,2))
df_one.insert(3,3,s_new)

datos_fisicos_uno = pd.DataFrame(
        arr_pand,
        columns=['Estatura (cm)',
                 'Peso (kg)',
                 'Edad (yr)' ])

datos_fisicos_dos = pd.DataFrame(
        arr_pand,
        columns=['Estatura (cm)',
                 'Peso (kg)',
                 'Edad (yr)' ],
        index = ['Juxx',
                 'Camch'])

df_one.index = ['Insu','Coellito']
df_one.columns = ['Nv','Lvl','Pw','En']
