
import pandas as pd
#%%

synergy_dataframe = pd.read_csv('synergy_logistics_database.csv', index_col=0,
                                encoding='utf-8', 
                                parse_dates=[4, 5])
#%%
"""
Synergy logistics esta considerando la posibilidad de enfocar sus esfuerzos en
los el top  8 de la combinacion 'product', 'transport_mode' y 'company_name'.
Acorde a cada a;o, cuales son esas 10 rutas?
"""

combinaciones = synergy_dataframe.groupby(by=['product', 'transport_mode',
                                               'company_name'])

descripcion = combinaciones.describe()['total_value']

#%%

mean = descripcion['count']
#print(descripcion['mean'])

mean_sort = mean.sort_values(ascending=False)

#%%
import seaborn as sns
import matplotlib.pyplot as plt

mean_sort = mean_sort.to_frame().reset_index()

#%%

g = sns.barplot(x='product', y='count', data=mean_sort.head(8), hue='transport_mode')
plt.show()

#%%

datos_2018 = synergy_dataframe[synergy_dataframe['year'] == '2018'].copy()

datos_2018['month'] = datos_2018['date'].dt.month

datos_por_mes = datos_2018.groupby(['month', 'transport_mode'])

datos_por_mes.sum()

datos_por_mes.count()['total_value']

datos_por_mes.describe()

serie = datos_por_mes.count()['total_value']
d18 = serie.to_frame().reset_index()

d18 = d18.pivot('month', 'transport_mode', 'total_value')

sns.lineplot(data=d18)

#%%

datos = synergy_dataframe.copy()

datos['year_month'] = datos['date'].dt.strftime('%Y-%m')
datos_year_month = datos.groupby(['year_month', 'transport_mode'])

serie = datos_year_month.count()['total_value']

dym = serie.to_frame().reset_index()

dym = dym.pivot('year_month', 'transport_mode', 'total_value')

sns.lineplot(data=dym)

#%%
exports = synergy_dataframe[synergy_dataframe['direction'] == 'Exports']
imports = synergy_dataframe[synergy_dataframe['direction'] == 'Imports']

paises= exports['origin'].value_counts()
paises_total= exports.groupby('origin').sum()['total_value'].reset_index()
total_value_percent = paises_total['total_value'].sum()
paises_total['percent'] = 100 * paises_total['total_value'] / total_value_percent

paises_exp_dest= exports['destination'].value_counts()
paises_total_exp_dest= exports.groupby('destination').sum()['total_value'].reset_index()
total_value_percent_exp_dest = paises_total_exp_dest['total_value'].sum()
paises_total_exp_dest['percent'] = 100 * paises_total_exp_dest['total_value'] / total_value_percent_exp_dest

paises_imports= imports['origin'].value_counts()
paises_total_imports= imports.groupby('origin').sum()['total_value'].reset_index()
total_value_percent_imports = paises_total_imports['total_value'].sum()
paises_total_imports['percent'] = 100 * paises_total_imports['total_value'] / total_value_percent_imports

paises_imp_dest= imports['destination'].value_counts()
paises_total_imp_dest= imports.groupby('destination').sum()['total_value'].reset_index()
total_value_percent_imp_dest = paises_total_imp_dest['total_value'].sum()
paises_total_imp_dest['percent'] = 100 * paises_total_imp_dest['total_value'] / total_value_percent_imp_dest
