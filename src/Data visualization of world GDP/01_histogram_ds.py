import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.graph_objects as px

plt.figure(figsize=(10,10))

def histogramOfRandomFromDataSet(gdp, eco):
    plt.hist(gdp, color="orange")
    plt.yticks(range(0, 10, 2))

dataset = pd.read_csv("GDP.csv")
countries_econ = dataset[['country code','Economy','US dollars)']]
icountries_econ = countries_econ[100:190]

random_gdp = icountries_econ['US dollars)']
random_Economy = icountries_econ['country code']

mylist = []

for i in random_gdp:
    cal = int(i)*1/100
    res = int(cal)
    mylist.append(res)


histogramOfRandomFromDataSet(mylist,random_Economy)