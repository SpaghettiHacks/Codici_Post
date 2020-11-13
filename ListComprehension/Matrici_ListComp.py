"""
Creazione di una matrice 5x5
METODO CLASSICO
"""
#dichirando value=0 nei parametri della funzione imposterà
# quest'ultimo a 0 di default in caso non fosse passato 
# durante la chiamata di funzione
def crea_matrice_classica(righe, colonne, value=0):
    matrice = []
    #per ogni riga   
    for each_r in range(righe):
        #Crea una lista vuota
        row = []
        #Per ogni colonna
        for each_c in range(colonne):
            #Aggiunge alla riga il valore
            row.append(value)
        #Aggiunge alla matrice la riga appena creata
        matrice.append(row)
    #Ritorna la lista di liste(Matrice)  
    return matrice

"""
Creazione di una matrice 5x5
METODO CON LIST COMPREHENSION
"""
#dichirando value=1 nei parametri della funzione imposterà
# quest'ultimo a 1 di default in caso non fosse passato 
# durante la chiamata di funzione
def crea_matrice_listComp(righe, colonne, value=1):
    return [[value] * colonne for righe in range(righe)]

#Impone che il codice all'interno dell'if venga eseguiro solamente 
# se il file è eseguito come script e non importato altrove
if __name__ == "__main__":
    righe = 5
    colonne = 5

    matrice_classica = crea_matrice_classica(righe, colonne)

    #Stampa delle singole righe della matrice creata
    for riga in matrice_classica:
        print(riga)

    print('\n###############\n')

    #Stampa delle singole righe della matrice creata
    matrice_ListComp = crea_matrice_listComp(righe, colonne)
    for riga in matrice_ListComp:
        print(riga)