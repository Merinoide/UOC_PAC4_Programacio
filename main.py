#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Arxi principal per executar totes les funcions de l'arxiu funcions.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import folium
import io
from PIL import Image
from selenium import webdriver

from funcions import (
    read_csv, clean_csv, rename_col, breakdown_date, erase_month, 
    groupby_state_and_year, print_biggest_handguns, print_biggest_longguns,
    time_evolution, interpretacio_grafica, groupby_state, clean_states,
    merge_datasets, calculate_relative_values, outlier_kentucky, mapa_choropleth
)

def main():
    # URL amb les dades del csv
    url_data = "https://raw.githubusercontent.com/BuzzFeedNews/nics-firearm-background-checks/master/data/nics-firearm-background-checks.csv"
    url_population_data = "https://gist.githubusercontent.com/bradoyler/0fd473541083cfa9ea6b5da57b08461c/raw/fa5f59ff1ce7ad9ff792e223b9ac05c564b7c0fe/us-state-populations.csv"
    geo_data_url = "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json"
    
    # Executem 1ª funció: llegir el csv
    df = read_csv(url_data)
    
    # Exectuem 2ª funció: neteja
    df = clean_csv(df)
    
    # Exectuem 3ª funció: renombrar columnes
    df = rename_col(df)
    
    # Exectuem 4ª columna de any i mes
    df = breakdown_date(df)
    
    # Exectuem 5ª funció: eliminar columna month
    df = erase_month(df)
    
    # Exectuem 6ª agrupar per estat i any
    df_grouped = groupby_state_and_year(df)
    
    # Exectuem 7ª estat amb més armes curtes
    print_biggest_handguns(df_grouped)
    
    # Exectuem 8ª estat amb més armes llargues
    print_biggest_longguns(df_grouped)
    
    # Exectuem 9ª evolució permisos, armes curtes i llargues
    time_evolution(df)
    
    # Exectuem 10ª interpretació gràfica
    interpretacio_grafica()
    
    # Exectuem 11ª agrupació per estat
    df_grouped_by_state = groupby_state(df)
    
    # Exectuem 12ª neteja dels estats
    df_cleaned_states = clean_states(df_grouped_by_state)
    
    # Exectuem 13ª fusonar dos conjunts de dades
    df_population = pd.read_csv(url_population_data)
    df_merged = merge_datasets(df_cleaned_states, url_population_data)
    
    # Exectuem 14ª calcular valor relatiu permisos i armes amb pbolació
    df_with_relative_values = calculate_relative_values(df_merged)
    
    # Exectuem 15ª  eliminar estat kentucky
    outlier_kentucky(df_with_relative_values)
    
    # Exectuem 16ª mapa choropleth
    mapa_choropleth(df_with_relative_values, geo_data_url)

if __name__ == "__main__":
    main()

