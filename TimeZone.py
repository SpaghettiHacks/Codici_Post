"""
La nuova versione 3.9.0 di python integra grazie all'installazione
di un modulo (tzdata) che introduce il supporto all'IANA time zone database.
Questo nuovo modulo permette di accedere alle date e agli orari di un determinato
luogo tramite dei semplici comandi.
"""

#pip install tzdata
import time
from zoneinfo import ZoneInfo
from datetime import datetime

#Funzione di formattazzione
def datetime_formatter(current_time):
    return current_time.strftime("%d-%m-%Y | %H:%M")

#Oraio attuale
current_time = datetime.now()

#Viene chiamata la funzione di formattazione passando l'ora attuale
italian_format_datetime = datetime_formatter(current_time)
print("Data e Orario senza formattazzione:\n",current_time,"\n") #Stampa della data senza formattazzione
print("Data e Orario in formato italiano:\n", italian_format_datetime,"\n") #Stampa della data con formattazzione italiana


#Date e Orari non locali
current_time_Los_Angeles = current_time.astimezone(ZoneInfo("America/Los_Angeles"))
current_time_Tokyo = current_time.astimezone(ZoneInfo("Asia/Tokyo"))

#Viene chiamata la funzione di formattazione passando l'ora attuale di Los Angeles
italian_format_datetime_Los_Angeles = datetime_formatter(current_time_Los_Angeles)

#Viene chiamata la funzione di formattazione passando l'ora attuale di Tokyo
italian_format_datetime_Tokyo = datetime_formatter(current_time_Tokyo)

print("Data e Orario in formato italiano di Los Angeles:\n",italian_format_datetime_Los_Angeles,"\n") #Stampa della data con formattazzione italiana

print("Data e Orario in formato italiano di Tokyo:\n",italian_format_datetime_Tokyo,"\n") #Stampa della data con formattazzione italiana
