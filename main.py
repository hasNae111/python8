import numpy as np
import pandas as pd

#challenge1
data = {
    'key':['d1','d2',"d3","d4","d5","d6","d7","d8","d9"],
    'note':[ 1, 2, 3, 4, 5, 6, 7,  8, 9]
}
df = pd.DataFrame(data)
print(df)

#challenge2

transactions = pd.DataFrame({
    'TransactionID': [1, 2, 3, 4, 5],
    'Montant': [100, 200, 2000, 3000, 700]
})

filtre = transactions[transactions['Montant'] > 1000]

print("les transactions superieures a 1000 :")
print(filtre)

#challenge3

ventes = pd.DataFrame({
    'Region': ['nord', 'est', 'nord', 'est', 'sud'],
    'Ventes': [100, 200, 300, 400, 500]
})

total_region = ventes.groupby('Region')['Ventes'].sum()

print("le total de ventes par region :")
print(total_region)


#challenge4

clients = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'nom': ['ahmad', 'sara', 'nada']
})

commandes = pd.DataFrame({
    'order_id': [1, 2, 3],
    'customer_id': [1, 2, 1],
    'montant': [100, 200, 250]
})

fusion = pd.merge(clients, commandes, on='customer_id')

print("DataFrame fusionnee :")
print(fusion)

#challenge5

data = pd.DataFrame({
    'Produit': ['a', 'a', 'b', 'b', 'c'],
    'Region': ['nord', 'est', 'sud', 'nord', 'est'],
    'Ventes': [100, 200, 300, 520, 300]
})

ppp = pd.pivot_table(data, values='Ventes', index='Produit', columns='Région', aggfunc='sum', fill_value=0)

print("le tableau finale est :")
print(ppp)



