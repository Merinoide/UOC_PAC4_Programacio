#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
Arxiu amb totes les funcions que s'executaran des de l'arxiu main.py

"""

import pandas as pd
import matplotlib.pyplot as plt
import folium
import io
from PIL import Image
from selenium import webdriver

def read_csv(url:str)->pd.DataFrame:
    """ Fa lectura del csv i imprimexi el datafrem 
    el simbol ->pd.DataFrame és simplemenet una anotació
    
    Valor d'entrada:
    Com a paràmetre demana una ulr que serà de tipus string
    
    Retorna:
    pd.DataFrame: El DataFrme té les dades del csv.
    Amb el simbol "->" indiquem que retornará i amb pd.DataFrame el tipus d'objecte
    
    """
    df = pd.read_csv(url)
    
    # En aquest print demanem FINS les 5 primeres columnes i no especifiquem fileres
    print("Primeres 5 fileres:\n", df.iloc[:,:5])
    return df


def clean_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Neteja del DataFrame i seleccionem unes columnes en específic 
    el simbol ->pd.DataFrame és simplemenet una anotació
    
    Valor d'entrada:
    Demana un df de tipus pd.DataFrame 
    
    Retorna:
    Reotrna un dataframe amb les columnes que hem demanat    
    """
    llista_columnes_seleccionades = ['month', 'state', 'permit', 'handgun', 'long_gun']
    
    neteja_df = df[llista_columnes_seleccionades]
    
    print("DataFrame amb les columnes seleccionades", neteja_df.columns.tolist())
    
    return neteja_df
    
    
def rename_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    Renombrem a columna 'long_gun' a 'longgun' del datafrem inicial
    
    Valor d'entrada:
    Demana un df tipus DataFrame on està la columna que volem renombrar
    
    Retorna:
    Retorna el datafrem de la primera funció amb la columna renombrada
    """
    
    # Primerament validem si està la columna
    if 'long_gun' in df.columns:
                # Si la columna està renombrem la columna
        
        df = df.rename(columns={'long_gun':'longgun'})
        
        print("Columna renombrada", df.columns.tolist())
    else:# En cas que no existeixi la columna
        print("No existeix la columna long_gun")
        
    return df

def breakdown_date(df:pd.DataFrame) ->pd.DataFrame:
    """
    Dividir la columna month en dues columnes year i month
    
    Valor d'entrada:
    Un df definit com pd.DataFrame que té la columna month
    
    Return:
    Retorna un DataFrame com dues columnes, year i month
    
    """
    # Creem les dues columnes i les separem pel simbol - que és el que separa any i mes
    df[['year','month']]= df['month'].str.split('-',expand=True).astype(int)
    print("Dataset amb la columna year i mont\n", df.head(5))
    
    return df


def erase_month(df:pd.DataFrame) -> pd.DataFrame:
    """
    Elimina la columna month del datafrem
    
    Valor d'entrada:
    Un df definit com pd.DataFrame que té la columna month
    
    Return: 
    Datafrem sense la columna month
    """
    df = df.drop(columns=['month'])
    print("Datafrem sense la columna month\n", df.head())
    print("Llista de columnes del datafrem", df.columns.tolist())
    
    return df


def groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa el datagrem per la columna stat i year i fà la suma per cada grup
    
    Valor d'entrada:
    df definit com a DataFrame
    
    Return: 
    DataFrame agruap per les columes state i year amb els valors sumats
    """
    df_agrupat = df.groupby(['year','state']).sum().reset_index()
    print("Dataset agrupat per year i state",df_agrupat )
    return df_agrupat


def print_biggest_handguns(df:pd.DataFrame):
    """
    Imprimeix l'estat i any amb el valor més gran a la columna handguns
    
    Valor d'entrada:
    Datafem de la función grupby_state_and_year
    
    Retorna:
    NO retonra res, simplement imprimeix el resultat
    """
    
    #La funció idxmax retorna el valor màxim, si no indiquem columna agafará el valor màxim del dataset
    valor_maxim_handguns = df.loc[df['handgun'].idxmax()]
    
    print(f"L'estat {valor_maxim_handguns['state']} per l'any {valor_maxim_handguns['year']} te el maxim d'armes curtes {valor_maxim_handguns['handgun']}")


def print_biggest_longguns(df:pd.DataFrame):
    """
    Imprimeix l'estat i any amb el valor més gran a la columna longguns
    
    Valor d'entrada:
    Datafem de la función grupby_state_and_year
    
    Retorna:
    NO retonra res, simplement imprimeix el resultat
    """
    
    #La funció idxmax retorna el valor màxim, si no indiquem columna agafará el valor màxim del dataset
    valor_maxim_longguns = df.loc[df['longgun'].idxmax()]
    
    print(f"L'estat {valor_maxim_longguns['state']} per l'any {valor_maxim_longguns['year']} te el maxim d'armes llargues {valor_maxim_longguns['longgun']}")


    
def time_evolution(df: pd.DataFrame):
    """
    Grafica de la serie temporal dels permisos, total d'armes curtes i llargues
    
    Valor d'entrada:
    Datafrem que té separació entre any i mes
    
    Retorna la grafica
    
    """
    
    df_grouped = df.groupby('year').sum().reset_index()
    plt.figure(figsize=(10,6))
    plt.plot(df_grouped['year'], df_grouped['permit'], label='Permit')
    plt.plot(df_grouped['year'], df_grouped['handgun'], label='Handgun')
    plt.plot(df_grouped['year'], df_grouped['longgun'], label='Longgun')
    
    plt.xlabel('Year')
    plt.ylabel('Total Cunts')
    plt.title('Evolució dels permisos, armes de curtes i llargues')
    plt.legend()
    plt.show()
    
    
def interpretacio_grafica():
    """
    Funció que imprimeix l'interpretació de les gràfiques
    
    """
    
    print(f"Període 1994-2005: Hi ha més armes llargues i curtes que permisos, és a dir les persones amb llicència d'armes tene més d'una\n",
         f"Període del 2005-2014: Incremente el nombre de llicències fins finalmente superar la tenencia d'armes curtes i llarges, però no la suma de les dues\n"
         f"Període del 2024-2020: Punt màxim de nombre de llicències, superior a la tenencia d'amres curtes i llarges per després caura novament per sota d'aquestes. Posicionant les armes curtes per sobre de la resta\n"
         f"Període del 2020-actualitat: Amb la Covid hi ha una caiguda de totres les tendencies\n"
         f"Conclusió final: Quan la linia de permisos està per sota indica que els propietaris d'armes tenen més d'una arma en promig. Quan està per sobre indica que donat més permisos de la compra de noves armes")
    
    
    
def groupby_state(df: pd.DataFrame):
    """
    Agrupa les dades per estat i any
    
    Valor d'entrada:
    Datafrem del exercici groupby_state_and_year
    
    Retorna:
    Datafrem agrupat per estat i any
    
    """
    grouped_df = df.groupby('state').sum().reset_index()
    print("Les 5 primeres fileres del dataset agrupat per estats.\n", grouped_df.head())
    return grouped_df


def clean_states(df: pd.DataFrame):
    """
    Elimina les fileres dels estats Guam, Mariana Isalnd, Puerto RIco, and VIrgin Islands.
    
    
    Valor d'entrada:
    df de la funció group_satet
    
    Retorna:
    
    Datafrem sense els estats mencionats     
    
    """
    
    llista_estats_eliminar = ['Guam', 'Mariana Islands', 'Puerto Rico', 'Virgins Islands']
    
    fileres_inicials = df.shape[0]
    
    # Amb el simbol ~ indiquem que volem un dataset contrari als valors que estan a la llista
    df = df[~df['state'].isin(llista_estats_eliminar)]
    
    fileres_finals = df.shape[0]
    
    return df


def merge_datasets(df1: pd.DataFrame, url: str):
    """
    Fusiona dos dataset per la columna 'state'
    
    Valor d'entrada:
    datafrem de la funció merge
    
    datafrem de la url
    
    Retrona:
    un dataset on s'ha fet el merge dels dos datasets d'entrada
    
    """
    
    # Datafrem de la url
    df2 = pd.read_csv(url)
    
    merged_df = pd.merge(df1, df2, on='state')
    
    print("Dataset 'fusionat': \n", merged_df.head())
    
    return merged_df



def calculate_relative_values(df: pd.DataFrame):
    """
    Incopora la columna del percentatges dels permisos, armes curtes i armes llargues relatives a la població 
    de cada estat.
    
    
    Valor d'entrada:
    
    Dataset de la funció merged_df
    
    Retorna:
    Datafrem amb les columnes dels percentatges
    
    """
    df['permit_perc'] = (df['permit']/df['pop_2014'])*100
    df['handgun_perc'] = (df['handgun']/df['pop_2014'])*100
    df['longgund_perc'] = (df['longgun']/df['pop_2014'])*100
    print("Dataframe amb les columnes percentuals: \n", df.head())
    
    return df

def outlier_kentucky(df: pd.DataFrame):
    """
    Calcula la mitjana dels permisos per tot el conjunt dedades i després torna a fer-ho perso sense l'estat de Kentucky
    
    
    Valor d'entrada:
    
    Datafrem de la funció calculate_relative_values
    
    Retorna:
    La mitjana amb i sense l'estat de Kentucky
    
    """
    
    mitjana_permisos = round(df['permit_perc'].mean(),2)
    print(f"Mitjana de permisos en percentatge: {mitjana_permisos}")
    
    informacio_kentucky = df[df['state']=='Kentucky']
    print(f"Información de Kentucky\n",informacio_kentucky)
    
    # Identifiquem l'estat de Kentucky y la columna permit_perc i li donem el valor general de la mitjana
    df.loc[df['state']=='Kentucky', 'permit_perc']= mitjana_permisos
    
    nova_mitjana_permisos = df['permit_perc'].median()
    
    print(f"Mitjana de permisos en percentatge sense outlier:{nova_mitjana_permisos}")
    


def crear_mapa_choropleth(df: pd.DataFrame, column:str, data_geo:str, imatge_sortida:str):
    """
    Creem un mapa choropletico i es guarda com a imatge.
    
    Valor d'entrada:
    Datafrem     
    La columna amb el valor que volem que es visualitzi
    Arxiu amb el GEoJson del mapa dels Estats UNits
    Ruta de la carpeta on serà guardada
    
    Retorna:
    Res
    
    """
    # Creem el mapa replicant l'exemple de https://python-graph-gallery.com/292-choropleth-map-with-folium/
    mapa = folium.Map(location=[48,-102], zoom_start=3)
    
    folium.Choropleth(
        geo_data = data_geo,
        name ="Choropletic",
        data=df,
        columns=['state',column],
        key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2
#         legend_name=f'{column}(%)',  
    ).add_to(mapa)
    
    
    folium.LayerControl().add_to(mapa)    
    
    
    #Guardem el mapa com imatge segons el codi facilitat
    
    img_data = mapa._to_png(5)
    img = Image.open(io.BytesIO(img_data))
    img.save(imatge_sortida)
    print(f'{imatge_sortida} guardada correctament')
    
    
    
def mapa_choropleth(df: pd.DataFrame, url_geo_data: str):
    """
    Crida la función que genera el mapa i et demana el datafrem i les columnes per generar-ho
    
    Paràmetre:
    
    Et demana el datafrem en aquest cas de la funció calculate_relative_values
    
    Valor d'entrada:
    Datafrem amb els valors per estat i les columnes amb els permisos, armes curtes i llargues
    URL de GEOjson amb el mapa dels EEUU
    
    Retorna:
    Res 
    
    """
    
    crear_mapa_choropleth(df, 'permit_perc', url_geo_data, 'permit_perc.png')
    crear_mapa_choropleth(df, 'handgun_perc', url_geo_data, 'handgun_perc.png')
    crear_mapa_choropleth(df, 'longgun_perc', url_geo_data, 'longgun_perc.png')
    

