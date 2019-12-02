# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:46:23 2019

@author: junt_
"""

import numpy as np
import pandas as pd

lista_numeros = [4,13,18,21]
tupla_numeros = (9,8,7,6)
np_numeros = np.array((29,45,7,34))

serie_a = pd.Series(
        lista_numeros)
serie_b = pd.Series(
        tupla_numeros)
serie_c = pd.Series(
        np_numeros)
serie_d = pd.Series([
        True,
        False,
        100,
        1.00001,
        "Juxx",
        None,
        (),
        [],
        {"nombre":"juxxi"},
        ])

serie_d[3]

lista_ciudades = ["Riobamba","Quito","Montañita","Ibarra"]

serie_ciudad = pd.Series(
        lista_ciudades,
        index=[
                "R",
                "Q",
                "M",
                "I",
                ])

serie_ciudad["R"]
serie_ciudad[1]

valores_ciudad = {
        "Riobamba": 2014,
        "Quito": 2018,
        "Montañita": 2019,
        "Ibarra":2015,
        }

serie_valor_ciudad = pd.Series(
        valores_ciudad
        )

serie_valor_ciudad['Ibarra']
serie_valor_ciudad[2]

ciudades_menores_2018 = serie_valor_ciudad < 2018

serie_valor_ciudad[ciudades_menores_2018]

serie_valor_ciudad = serie_valor_ciudad * 1.10
serie_valor_ciudad["Quito"] = serie_valor_ciudad["Quito"] - 50

print("Guayaquil" in serie_valor_ciudad)
print("Montañita" in serie_valor_ciudad)

serie_valor_ciudad = np.square(serie_valor_ciudad)
serie_valor_ciudad = np.sin(serie_valor_ciudad)

ciudades_uno = pd.Series({
        "Guayaquil":2019,
        "Ambato":2015,
        "Guaranda":2014,
        })

ciudades_dos = pd.Series({
        "Puyo":2012,
        "Guayaquil":2014,
        })

ciudades_uno["Puyo"] = 2009 
print(ciudades_uno + ciudades_dos)

ciudad_add = ciudades_uno.add(ciudades_dos)
ciudades_con_v = pd.concat([
        ciudades_uno,
        ciudades_dos],
        verify_integrity = True
        )

print(ciudades_uno.max())

ciudades_uno.mean()
ciudades_uno.median()
np.average(ciudades_uno)

ciudades_uno.head(2)
ciudades_uno.tail(2)

ciudades_uno.sort_values(
        ascending = False
        ).head(2)

ciudades_uno.sort_values().tail(2)

#0-1000 5%
#1001 - 5000 10%
#5000 - 20000 15%

def calculo(valor):
    if(valor <= 1000):
        return valor * 1.05
    if(valor <= 5000 and valor > 1000):
        return valor * 1.10
    if(valor <= 20000 and valor > 5000):
        return valor * 1.15

ciudades_uno.map(calculo)

ciudades_uno.where(ciudades_uno < 1000, ciudades_uno * 1.05)






















