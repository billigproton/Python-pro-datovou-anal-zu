# # Titanic dataset

# import pandas
# # 1 - načtení do Data Frame a do proměnné titanic 

# titanic = pandas.read_csv('titanic.csv')

# # 2 - zobrazení názvu sloupců

# print(titanic.columns)

# # 3 - kolik má dataset řádků?

# print(titanic.shape)

# # 4 - v jakých sloupcích chybí hodnoty? - metoda info()

# print(titanic.info())
 
#  # BONUS: metoda isna()

# sloupce_s_prazdnymi_hodnotami = titanic.columns[titanic.isna().any()]

# print(sloupce_s_prazdnymi_hodnotami)



# staré zadání

# Titanic dataset

import pandas
# 1 - načtení do Data Frame a do proměnné titanic 

titanic = pandas.read_csv('Lekce_1/titanic.csv')

 # nebo cestou url

url = 'https://kodim.cz/cms/assets/analyza-dat/python-data-1/python-pro-data-1/nacteni-dat/excs/titanic/titanic.csv'

titanic = pandas.read_csv(url)

# 2 - zobrazení názvu sloupců

print(titanic.columns)

# 3 - kolik má dataset řádků?

print(titanic.shape[0])

# 4 - průměrný věk pasažérů?, 5 - nejstarší pasažér?

print(titanic.describe())

 # navíc - kdybychom chtěli z výsledného Dataframu vydolovat JEN tu hodnotu nejstaršího pasažéra
statisticky_souhrn = titanic.describe()

nejstarsi_pasazer = statisticky_souhrn['Age']['max']

print(nejstarsi_pasazer)


