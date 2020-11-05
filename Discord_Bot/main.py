#pip install discord
#pip install certifi

import discord 
import random
from discord.ext import commands
from time import sleep

#Importare da un secondo file il dizionario con le citazioni
#da randomizzare
from citazioni import citazioni

#Creazione del prefisso per richiamare il bot "!"
client = commands.Bot(command_prefix = "!")

#La funzione è decorata per gli eventi
@client.event
#La funzione è standard nella libreria discord e 
#viene richiamata quando il bor viene attivato
async def on_ready():
    print("Bot is ready")

#La funzione vinene richiamata quando 
#nella chat viene inserito il comando prefisso+aliases
#   !cit.
@client.command(aliases=['cit.'])
async def cit(ctx):
    #La funzione aspetterà mezzo secondo
    #prima di essere eseguita
    sleep(0.5)

    #Con la funzione random.choice vine presa una citazione 
    # casuale dal dizionario importato  
    citazione = str(random.choice(citazioni))

    #Scrive in chat la citazione scelta
    await ctx.send(f"{citazione}")

#TOKEN
client.run('NzcxODMyODc3ODIyMjQ2OTEy.X5x3Yg.O-d-UtvsK1RwxxRMZtvcE7UrHVQ')