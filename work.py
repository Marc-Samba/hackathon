# # Hackathon 31/10/2023
# # Salomé BRICHET, Gaspard PEREIRA, Louise PHILIBERT--NICOL, Marc SAMBA

# ## Appréhension de la dataframe

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('dfhappiness.csv', sep=';')
df.head(15)

#on remarque un problème de type dans la colonne Healthy life expectancy at birth
df['Healthy life expectancy at birth']=df['Healthy life expectancy at birth'].str.replace(',', '.').astype(float)

# On constate que le problème est solvé, toutes les colonnes ont un type adapté
df.info()

# ## Regroupement intemporel par pays et définition de l'indicateur de bonheur

# +
# On regroupe par pays
dfmeant=df.groupby('Country name').mean()
dfmeant=dfmeant.drop('year', axis=1)

#Normalisation de la table
L_noms_colonnes = ['Life Ladder', 'Log GDP per capita', 'Social support', 'Healthy life expectancy at birth', 
                   'Freedom to make life choices','Generosity', 'Perceptions of corruption', 'Positive affect',
                   'Negative affect']

#dfnorm['Country name']=dfmeant['Country name']

dfmeant['Life Ladder']=dfmeant['Life Ladder']/max(dfmeant['Life Ladder'])
dfmeant['Log GDP per capita']=dfmeant['Log GDP per capita']/max(dfmeant['Log GDP per capita'])
dfmeant['Social support']=dfmeant['Social support']/max(dfmeant['Social support'])
dfmeant['Healthy life expectancy at birth']=dfmeant['Healthy life expectancy at birth']/max(dfmeant['Healthy life expectancy at birth'])
dfmeant['Freedom to make life choices']=dfmeant['Freedom to make life choices']/max(dfmeant['Freedom to make life choices'])
dfmeant['Generosity']=dfmeant['Generosity']/max(dfmeant['Generosity'])
dfmeant['Perceptions of corruption']=dfmeant['Perceptions of corruption']/max(dfmeant['Perceptions of corruption'])
dfmeant['Positive affect']=dfmeant['Positive affect']/max(dfmeant['Positive affect'])
dfmeant['Negative affect']=dfmeant['Negative affect']/max(dfmeant['Negative affect'])

## Cette boucle ne fonctionnait pas :
##for nom in L_noms_colonnes : 
##    dfmeant['nom']=dfmeant['nom']/max(dfmeant['nom'])

# On impose arbitrairement une hiérarchie des critères

dfmeant['indicateur'] = 3 * dfmeant['Life Ladder'] + dfmeant['Log GDP per capita'] + 4 * dfmeant['Social support'] + 2 * dfmeant['Healthy life expectancy at birth'] + dfmeant['Freedom to make life choices'] + 4 * dfmeant['Generosity'] - 3 * dfmeant['Perceptions of corruption'] + 4 * dfmeant['Positive affect'] - 4 * dfmeant['Negative affect']

# On normalise aussi l'indicateur en vue du tracé

dfmeant['indicateur'] = dfmeant['indicateur'] / max(dfmeant['indicateur'])

dfmeant
# -

# ## Liste des pays du moins au plus heureux

dfmeant=dfmeant.sort_values(by=['indicateur'])
liste_des_pays_les_plus_heureux=list(dfmeant.index)
liste_des_pays_les_plus_heureux

plt.plot(np.array(dfmeant.index),np.array(dfmeant['indicateur']), '.')
plt.show()

# Les abscisses sont illisibles, on choisit donc de se référer à la liste triée des pays les plus heureux
