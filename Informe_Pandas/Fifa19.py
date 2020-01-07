# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

path = "X://Documents//7mo//Python//FifaDataSet//players_20.csv"

columns = ['ID',
           'Name',
           'Age',
           'Nationality',
           'Club',
           'Position',
           'Overall',
           'Potential',
           'Preferred Foot',
           'Weak Foot',
           'Skill Moves',
           'Pace',
           'Shooting',
           'Passing',
           'Dribbling',
           'Defending',
           'Physic',
           'Contract Valid Until',
           'Value',
           'Wage']

fifa_all_players = pd.read_csv(
        path,
        usecols = columns,
        index_col = 'ID')

print(len(fifa_all_players.index))

fifa_young_players = fifa_all_players.loc[fifa_all_players.Age <= 20]

labels = ['Jugadores Totales','Jugadores Mayores de 20','Jugadores Menores de 20']
y_pos = np.arange(len(labels))
data = [len(fifa_all_players.index),len(fifa_all_players.index)-len(fifa_young_players.index),len(fifa_young_players.index)]
fig1, graph_gender_loan_amount = plt.subplots()
fig1.set_size_inches(10, 7)
plt.bar(y_pos, data, align='center', alpha=0.5)
plt.xticks(y_pos, labels)
plt.ylabel('Cantidad')
plt.title('Número de jugadores por Edad')
plt.show()



fifa_young_best_potential_players = fifa_young_players.loc[fifa_young_players.Potential >= 80].sort_values(ascending=False,by='Potential')

fifa_young_players_by_country = fifa_young_best_potential_players.groupby('Nationality')['Name'].count().sort_values(ascending = False)

amount_by_country_top = fifa_young_players_by_country[fifa_young_players_by_country>10]
amount_by_country_bottom = pd.Series(fifa_young_players_by_country[fifa_young_players_by_country <= 10].sum(), index=['Others'])
amount_by_country_final = amount_by_country_top.append(amount_by_country_bottom)
##explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
number_players_by_country = amount_by_country_final.array
graph_amount_players_by_country = amount_by_country_final.plot(pctdistance=0.9, autopct='%1.0f%%', legend=True, shadow=True, kind='pie', figsize = (30, 25), fontsize=20)
plt.title(label='Países con mayor cantidad de futbolisitas jóvenes', fontsize=40)
#graph_amount_by_sector_top.legend(values_amount_by_region, loc='best', title = 'Values', title_fontsize=16 ,fontsize=13)

circle_donut=plt.Circle( (0,0), 0.6, color='white')
p=plt.gcf()
p.gca().add_artist(circle_donut)
plt.ylabel('')

plt.show()

fifa_young_players_by_country = fifa_young_best_potential_players.groupby('Nationality')

##----------- NO TOCAR--------------------------------------------------------------------------------
fifa_young_players_France = fifa_young_players_by_country.get_group('France')
fifa_young_players_England = fifa_young_players_by_country.get_group('England')
fifa_young_players_Spain = fifa_young_players_by_country.get_group('Spain')
fifa_young_players_Argentina = fifa_young_players_by_country.get_group('Argentina')
fifa_young_players_Netherlands = fifa_young_players_by_country.get_group('Netherlands')
##----------------------------------------------------------------------------------------------------
saving_path = "X://Documents//7mo//Python//FifaDataSet//players_Netherlands.pickle"
fifa_young_players_Netherlands.to_pickle(saving_path)
##----------------------------------------------------------------------------------------------------

france_players = pd.read_pickle("X://Documents//7mo//Python//FifaDataSet//players_France.pickle")

france_forward_players = france_players.query('Position == \'ST\' | Position == \'RW\' | Position == \'LW\' | Position == \'CF\' ')
france_mid_players = france_players.query('Position == \'CAM\' | Position == \'CM\' | Position == \'CDM\' | Position == \'RM\' | Position == \'LM\'')
france_defense_players = france_players.query('Position == \'GK\' | Position == \'LB\' | Position == \'RB\' | Position == \'CB\' ')



##-----------------------------------------------------------------------------------------------------
def average_Ability(team_players):
    return (np.average(team_players.Potential))

labels = np.array(['Delantera','Mediocampo','Defensa'])
stats = np.array([average_Ability(france_forward_players),average_Ability(france_mid_players),average_Ability(france_defense_players)])
##------------------------------------------------------------------------------------------------------
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
stats = np.concatenate((stats,[stats[0]]))
angles = np.concatenate((angles,[angles[0]]))

fig = plt.figure(figsize=(9,9))
ax  = fig.add_subplot(111, polar=True)
plt.yticks([50,60,70,80], ["50","60","70","80"], color="black", size=10)
plt.ylim(40,90)
ax.plot(angles, stats, 'o-', linewidth=1)
ax.fill(angles, stats, alpha=0.25)
ax.set_thetagrids(angles * 180/np.pi, labels)
ax.set_title('Francia-Sub20-Potencial')
ax.grid(True)



argentina_players = fifa_young_players_Argentina.query('Position != \'GK\'')


def average_Stats(team_players,stat):
    return (np.average(team_players[stat]))


france_players_no_GK = france_players.query('Position != \'GK\'')

labels = np.array(['Pace','Shooting','Passing','Dribbling','Defending','Physic'])
stats = np.array([average_Stats(france_players_no_GK,'Pace'),
                  average_Stats(france_players_no_GK,'Shooting'),
                  average_Stats(france_players_no_GK,'Passing'),
                  average_Stats(france_players_no_GK,'Dribbling'),
                  average_Stats(france_players_no_GK,'Defending'),
                  average_Stats(france_players_no_GK,'Physic')])
##------------------------------------------------------------------------------------------------------
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
stats = np.concatenate((stats,[stats[0]]))
angles = np.concatenate((angles,[angles[0]]))

ax  = plt.subplot(111, polar=True)
plt.yticks([70,80,90], ["70","80","90"], color="grey", size=7)
plt.ylim(50,100)
ax.plot(angles, stats, 'o-', linewidth=1)
ax.fill(angles, stats, alpha=0.25)
ax.set_thetagrids(angles * 180/np.pi, labels)
ax.set_title('Argentina-Sub20')
ax.grid(True)
##------------------------------------------------------------------------------------------------------

france_players_no_GK['Total'] = (france_players_no_GK['Pace'] + france_players_no_GK ['Dribbling'] )/2
france_best_players = france_players_no_GK.sort_values(ascending = False,by='Total').head(5)

# data to plot
n_groups = 4
means_frank = (90, 55, 40, 65)
means_guido = (85, 62, 54, 20)

# create plot
fig, ax = plt.subplots(figsize=(12,9))
index = np.arange(len(france_best_players.index))
bar_width = 0.25
opacity = 0.8

rects1 = plt.bar(index, france_best_players['Value'], bar_width,
                 alpha=opacity,
                 color='g',
                 label='Valor de Mercado')

rects2 = plt.bar(index + bar_width, france_best_players['Wage'], bar_width,
                 alpha=opacity,
                 color='y',
                 label='Sueldo')

plt.xlabel('Jugador-Posición')
plt.ylabel('Dinero en Euros')
plt.title('Costo y Salario por Jugador')
plt.yticks(np.arange(0, 100, 5))
plt.xticks(index + bar_width/2, france_best_players['Name']+'-'+france_best_players['Position'])
plt.legend()
plt.tight_layout()
plt.show()


fig1, graph_gender_loan_amount = plt.subplots()
fig1.set_size_inches(14, 7)
plt.bar(index, france_best_players['Value'], align='center', alpha=0.5, color = "black")
plt.xticks(index, france_best_players['Name']+'-'+france_best_players['Position'])
plt.ylabel('Dinero en Euros')
plt.xlabel('Jugador-Posición')
plt.title('Costo por Jugador')
plt.show()

#---------------------------------------------------------------------------------

england_players = pd.read_pickle("X://Documents//7mo//Python//FifaDataSet//players_England.pickle")

england_forward_players = england_players.query('Position == \'ST\' | Position == \'RW\' | Position == \'LW\' | Position == \'CF\' ')
england_mid_players = england_players.query('Position == \'CAM\' | Position == \'CM\' | Position == \'CDM\' | Position == \'RM\' | Position == \'LM\'')
england_defense_players = england_players.query('Position == \'GK\' | Position == \'LB\' | Position == \'RB\' | Position == \'CB\' ')

labels = np.array(['Delantera','Mediocampo','Defensa'])
stats = np.array([average_Ability(england_forward_players),average_Ability(england_mid_players),average_Ability(england_defense_players)])
##------------------------------------------------------------------------------------------------------
 

england_players_no_GK = england_players.query('Position != \'GK\'')

labels = np.array(['Pace','Shooting','Passing','Dribbling','Defending','Physic'])
stats = np.array([average_Stats(england_players_no_GK,'Pace'),
                  average_Stats(england_players_no_GK,'Shooting'),
                  average_Stats(england_players_no_GK,'Passing'),
                  average_Stats(england_players_no_GK,'Dribbling'),
                  average_Stats(england_players_no_GK,'Defending'),
                  average_Stats(england_players_no_GK,'Physic')])


england_players_no_GK['Total'] = (england_players_no_GK['Passing'] + england_players_no_GK ['Dribbling']+ england_players_no_GK['Shooting'])/3
england_best_players = england_players_no_GK.sort_values(ascending = False,by='Total').head(5)


fig, ax = plt.subplots(figsize=(16,10))
index = np.arange(len(england_best_players.index))
bar_width = 0.25
opacity = 0.8

rects1 = plt.bar(index, england_best_players['Passing'], bar_width,
                 alpha=opacity,
                 color='b',
                 label='Pase')

rects2 = plt.bar(index + bar_width, france_best_players['Dribbling'], bar_width,
                 alpha=opacity,
                 color='m',
                 label='Drible')

rects3 = plt.bar(index + bar_width*2, france_best_players['Shooting'], bar_width,
                 alpha=opacity,
                 color='r',
                 label='Tiro')

plt.xlabel('Jugador-Posición')
plt.ylabel('Valoración')
plt.title('Valoración por Jugador')
plt.yticks(np.arange(0, 100, 5))
plt.xticks(index + bar_width, england_best_players['Name']+'-'+england_best_players['Position'])
plt.legend()
plt.tight_layout()
plt.show()


fig1, graph = plt.subplots()
fig1.set_size_inches(14, 7)
plt.bar(index, england_best_players['Value'], align='center', alpha=0.5, color="blue")
plt.xticks(index, england_best_players['Name']+'-'+england_best_players['Position'])
plt.ylabel('Dinero en Euros')
plt.xlabel('Jugador-Posición')
plt.title('Costo por Jugador')
plt.show()

fig1, graph= plt.subplots()
fig1.set_size_inches(14, 7)
plt.bar(index, england_best_players['Wage'], align='center', alpha=0.5, color="black")
plt.xticks(index, england_best_players['Name']+'-'+england_best_players['Position'])
plt.ylabel('Dinero en Euros')
plt.xlabel('Jugador-Posición')
plt.title('Salario mensual por Jugador')
plt.show()

##barcelona_players.to_pickle("X://Documents//7mo//Python//FifaDataSet//players_barca.pickle")
barcelona_players = pd.read_pickle("X://Documents//7mo//Python//FifaDataSet//players_barca.pickle")

barcelona_first_team = barcelona_players.loc[barcelona_players.Overall >= 76]

barcelona_first_team_no_GK = barcelona_first_team.query('Position != \'GK\'')

labels = np.array(['Pace','Shooting','Passing','Dribbling','Defending','Physic'])
stats = np.array([average_Stats(barcelona_first_team_no_GK,'Pace'),
                  average_Stats(barcelona_first_team_no_GK,'Shooting'),
                  average_Stats(barcelona_first_team_no_GK,'Passing'),
                  average_Stats(barcelona_first_team_no_GK,'Dribbling'),
                  average_Stats(barcelona_first_team_no_GK,'Defending'),
                  average_Stats(barcelona_first_team_no_GK,'Physic')])
    
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
stats = np.concatenate((stats,[stats[0]]))
angles = np.concatenate((angles,[angles[0]]))

fig = plt.figure(figsize=(9,9))
ax  = fig.add_subplot(111, polar=True)
plt.yticks([50,60,70,80], ["50","60","70","80"], color="black", size=10)
plt.ylim(40,90)
ax.plot(angles, stats, 'o-', linewidth=1, color="purple")
ax.fill(angles, stats, alpha=0.25, color="purple")
ax.set_thetagrids(angles * 180/np.pi, labels)
ax.set_title('Barcelona de España valoración general')
ax.grid(True)












