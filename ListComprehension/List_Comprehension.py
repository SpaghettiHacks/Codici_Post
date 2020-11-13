"""
Creare un lista dei numeri pari da 0 a 50
METODO CLASSICO
"""
n_pari = []
for numero in range(51):
    if numero%2 == 0:
        n_pari.append(numero)
print(n_pari)

print()

"""
Creare un lista dei numeri pari da 0 a 50
METODO CON LIST COMPREHENSION
"""
#Le List Comprehension sono dei metodi compatti per scivere 
# determinate porzioni di codice
n_pari_list = [numero for numero in range(51) if numero%2 == 0]
print(n_pari_list)
