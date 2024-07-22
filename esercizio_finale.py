# Esercizio finale:

# L'obiettivo di questo esercizio è generare un set di dati di serie temporali
# utilizzando NumPy, analizzarli con pandas e visualizzare i risultati usando
# Matplotlib. Gli studenti dovranno eseguire le seguenti operazioni:

# Generazione dei Dati: Utilizzare NumPy per generare una serie temporale
# di 365 giorni di dati, simulando il numero di visitatori giornalieri in
# un parco. Assumere che il numero medio di visitatori sia 2000 con una
# deviazione standard di 500. Inoltre, aggiungere un trend crescente nel
# tempo per simulare l'aumento della popolarità del parco.
# Creazione del DataFrame: Creare un DataFrame pandas con le date come
# indice e il numero di visitatori come colonna.
# Analisi dei Dati: Calcolare il numero medio di visitatori per mese e la
# deviazione standard.
# Visualizzazione dei Dati:
# Creare un grafico a linee del numero di visitatori giornalieri.
# Aggiungere al grafico la media mobile a 7 giorni per mostrare la
# tendenza settimanale.
# Creare un secondo grafico che mostri la media mensile dei visitatori.

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Generimao dati visitatori per un num.specifciato di giorni
def genera_dati_visitatori(giorni=365, media=2000, dev_standard=500, trend_max=500):
    if giorni <= 0:
        print("errore: il numero di giorni dev'essere positivo.")
        return np.array([])
    if media <= 0:
        print("erorre la media dev'essere postiva.")
        return np.array([])
    if dev_standard <= 0:
        print("errore la devizaione standard dev'essere positva")
        return np.array([])
    
    visitatori_base = np.random.normal(media, dev_standard, giorni)     #genero dati base
    trend= np.linspace(0, trend_max, giorni)   #genero il trend
    return visitatori_base + trend         #creazione dei dati finali 
    
    # crea un intervallo di date a partire da una data iniizalòe per num.di giorni specificicato
def crea_inervallo_date(data_inizio, giorni):
    try:
        return pd.date_range(start=pd.to_datetime(data_inizio), periods= giorni, freq='D')
    except:
        print("Errore nella creazione dell'intervallo di date")
        return pd.DatetimeIndex([])
    
    
    # Crea un DataFrame con le date come indice e il numero di visitatori come colonna
def crea_dataframe(visitatori_giornalieri, date):
    if len(visitatori_giornalieri) != len(date):
        print("Errore: La lunghezza dei dati dei visitatori non corrisponde al numero di date.")
        return pd.DataFrame()                         # Restituisce un DataFrame vuoto in caso di errore
    return pd.DataFrame(data={'Visitatori': visitatori_giornalieri}, index=date)


    # calcola la media e la deviazione standard dei visitatori per mese
def analizza_dati(dati):
    if dati.empty:
        print("Errore Il DataFrame dei dati è vuoto.")
        return pd.DataFrame(), pd.DataFrame()  # Restituisce DataFrame vuoti in caso di errore
    media_mensile = dati.resample('M').mean()
    std_mensile = dati.resample('M').std()
    return media_mensile, std_mensile


def traccia_visitatori_giornalieri(dati):
    if dati.empty:
        print("erorre il dataframe dei dati è vuoto")
        return