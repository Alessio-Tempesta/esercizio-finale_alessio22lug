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

# Genera dati dei visitatori per un numero specificato di giorni
def genera_dati_visitatori(giorni=365, media=2000, dev_standard=500, trend_max=500):      # np.array Array di dati generati con una componente di trend crescente.
    if giorni <= 0:
        print("Errore: il numero di giorni dev'essere positivo.")
        return np.array([])
    if media <= 0:
        print("Errore: la media dev'essere positiva.")
        return np.array([])
    if dev_standard <= 0:
        print("Errore: la deviazione standard dev'essere positiva.")
        return np.array([])
    
    visitatori_base = np.random.normal(media, dev_standard, giorni)  # Genera dati base
    trend = np.linspace(0, trend_max, giorni)  # Genera il trend
    return visitatori_base + trend  # Creazione dei dati finali

# Crea un intervallo di date a partire da una data iniziale per un numero specificato di giorni
def crea_intervallo_date(data_inizio, giorni):
    try:
        return pd.date_range(start=pd.to_datetime(data_inizio), periods=giorni, freq='D')
    except:
        print("Errore nella creazione dell'intervallo di date")
        return pd.DatetimeIndex([])

# Crea un DataFrame con le date come indice e il numero di visitatori come colonna
def crea_dataframe(visitatori_giornalieri, date):
    if len(visitatori_giornalieri) != len(date):
        print("Errore: La lunghezza dei dati dei visitatori non corrisponde al numero di date.")
        return pd.DataFrame()       # Restituisce un DataFrame vuoto in caso di errore
    return pd.DataFrame(data={'Visitatori': visitatori_giornalieri}, index=date)

# Calcola la media e la deviazione standard dei visitatori per mese
def analizza_dati(dati):
    if dati.empty:
        print("Errore: Il DataFrame dei dati è vuoto.")
        return pd.DataFrame(), pd.DataFrame()  # Restituisce DataFrame vuoti in caso di errore
    media_mensile = dati.resample('M').mean()
    std_mensile = dati.resample('M').std()
    return media_mensile, std_mensile

# Traccia il numero di visitatori giornalieri
def traccia_visitatori_giornalieri(dati):
    if dati.empty:
        print("Errore: il DataFrame dei dati è vuoto.")
        return
    
    plt.figure(figsize=(14, 7))
    plt.plot(dati.index, dati['Visitatori'], label='Visitatori giornalieri')

    # Aggiungi la media mobile a 7 giorni
    dati['Media Mobile 7 Giorni'] = dati['Visitatori'].rolling(window=7).mean()
    plt.plot(dati.index, dati['Media Mobile 7 Giorni'], label='Media mobile a 7 giorni', color='blue')
    plt.xlabel('Data')
    plt.ylabel('Numero di Visitatori')
    plt.title('Numero di visitatori giornalieri con media mobile a 7 giorni')
    plt.legend()
    plt.show()

# Traccia la media mensile dei visitatori
def traccia_media_mensile(media_mensile):
    if media_mensile.empty:
        print("Errore: il DataFrame della media mensile è vuoto.")
        return

    plt.figure(figsize=(14, 7))
    plt.plot(media_mensile.index, media_mensile['Visitatori'], label='Media mensile dei visitatori')
    plt.xlabel('Mese')
    plt.ylabel('Numero di Visitatori')
    plt.title('Media mensile dei visitatori')
    plt.legend()
    plt.show()

# Funzione principale
def main():
    giorni = 365
    data_inizio = '2023-01-01'
    media_visitatori = 2000
    dev_standard = 500
    trend_max = 500
    
    # Genera i dati dei visitatori
    visitatori = genera_dati_visitatori(giorni, media_visitatori, dev_standard, trend_max)
    # Crea l'intervallo di date
    date = crea_intervallo_date(data_inizio, giorni)
    # Crea il DataFrame
    df = crea_dataframe(visitatori, date)
    # Analizza i dati
    media_mensile, std_mensile = analizza_dati(df)
    
    print(f"Media mensile dei visitatori:\n{media_mensile}")
    print(f"\nDeviazione standard mensile dei visitatori:\n{std_mensile}")
    
    # Traccia i grafici
    traccia_visitatori_giornalieri(df)
    traccia_media_mensile(media_mensile)

# Esegui la funzione principale
main()
