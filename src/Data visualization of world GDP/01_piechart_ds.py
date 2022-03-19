import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.graph_objects as px

def Top_10_gdp_world(coun, econ):
    top10ec = coun.iloc[1:11]
    top10nm = econ.iloc[1:11]
    plt.pie(top10ec, labels = top10nm)
    plt.axis('equal')
    plt.show()

dataset = pd.read_csv("GDP.csv")

countries = dataset['US dollars)']
economy = dataset['Economy']

Top_10_gdp_world(countries, economy)