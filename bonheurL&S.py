import pandas as pd
import matplotlib as plt
df = pd.read_csv('datahappy.csv')
df.head()

len(df)

df.describe()

country = df['Country name'].unique()
country

df.shape

tab = [i for i in range (2199)]

df['indice'] = tab
df.head()

col = df.columns
col = col[2:-1]
len(col)
col

# +
Note = []
for i in range (2199):
    valeur = 0
    valeur = 7*df.loc[i,col[0]]+df.loc[i,col[1]]+12*df.loc[i,col[2]]+df.loc[i,col[3]]/5+10*df.loc[i,col[4]]+10*df.loc[i,col[5]]-5*df.loc[i,col[6]]+5*df.loc[i,col[7]]-5*df.loc[i,col[8]]
    Note.append(valeur)

#notre calcul de la 'valeur du bonheur' est assez arbitraire et basé sur nos propres critères#
# -

df['Note'] = Note
df.head()

# +
for k in country :
    by_country = df.groupby(by = 'Country name')
    new = by_country.get_group(k)    
    new = new.set_index('year')
    new.Note.plot(kind = 'bar')

#on a essayé de tracer le graphique du bonheur dans chaque pays en fonction du temps mais on a pas réussi donc on s'est focalisé sur des pays précis#
# -

by_country = df.groupby(by = 'Country name')
new = by_country.get_group('Yemen')
new = new.set_index('year')
new.Note.plot(kind = 'bar')
#on pourrait essayer d'expliquer la baisse du bonheur au Yemen par la crise yemenite de 2011#

by_country = df.groupby(by = 'Country name')
new = by_country.get_group('France')
new = new.set_index('year')
new.Note.plot(kind = 'bar')
#on observe pour la France une valeur de bonheur constante, qu'on pourrait expliquer par le fait que la France est un pays développé qui ne connaît pas de crise majeure#

by_country = df.groupby(by = 'Country name')
new = by_country.get_group('Israel')
new = new.set_index('year')
new.Note.plot(kind = 'bar')

by_country = df.groupby(by = 'Country name')
new = by_country.get_group('Syria')
new = new.set_index('year')
new.Note.plot(kind = 'bar')
#on remarque une valeur de bonheur décroissante, qu'on pourrait expliquer par la situation instable de la Syrie et la guerre#
