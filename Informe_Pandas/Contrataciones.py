# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 23:04:40 2019

@author: junt_
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

path = "X://Documents//fifa20_data.csv"

columns = ['ID',
           'Name',
           'Age',
           'Country',
           'Club',
           'BP',
           'Overall',
           'Potential',
           'foot',
           'W/F',
           'SM',
           'PAC',
           'SHO',
           'PAS',
           'DRI',
           'DEF',
           'PHY',
           'Value',
           'Wage']

all_players = pd.read_csv(
        path,
        usecols = columns,
        index_col = 'ID')

all_players_with_stats = pd.read_csv(
        path,
        index_col = 'ID')

young_players = all_players.loc[all_players.Age <= 22]

young_best_potential_players = young_players.loc[young_players.Potential >= 80].sort_values(ascending=False,by='Potential')

left_back_player = young_best_potential_players.query('BP == \'LB\' | BP == \'LWB\'')
midfielder_player = young_best_potential_players.query('BP == \'CDM\' | BP == \'CM\' | BP == \'CAM\'')
right_wing_player = young_best_potential_players.query('BP == \'RM\' | BP == \'RW\'')
left_wing_player = young_best_potential_players.query('BP == \'LM\' | BP == \'LW\'')