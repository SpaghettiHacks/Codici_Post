#pip install pandas
#pip install matplotlib
import pandas
"""
Importare nel file la libreria matplotlib.pyplot e 
rinominarla localmente come plt per comodità d'uso
"""
import matplotlib.pyplot as plt
#Assegnazione dei dati presenti nel file iphone_price.csv alla variabile data
data = pandas.read_csv('iphone_price.csv')
"""
Tramitela il comando plot viene generato un grafico sulla base
dei dati presenti nel file iphone_price.csv.
Diversi tipi di dati possono essere creati con differenti 
comandi:
>>>dir(plt) per vedere tutti i comandi disponibili nella libreria
Altrimenti visita il sito:
https://matplotlib.org/3.3.2/tutorials/introductory/sample_plots.html
"""
plt.plot(data['version'], data['price'])
#Mostra il grafico generato sulla base dei dati ne file iphone_price.csv
plt.show()