import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.graph_objects as px

dataset = pd.read_csv("GDP.csv")
countries = dataset['US dollars)']

c_200 = countries.iloc[1:200]
cont = c_200.sample(n=25)
reversed_list = countries[::-1]

economy = dataset['Economy']
top_10_economies = economy.iloc[1:100]

lst = []
for i in cont:
    per_10 = (int(i)*10)/100
    lst.append(per_10)
lst.reverse()

def WholeGDP(filename):
    data = pd.read_csv(filename)
    plot = px.Figure(data=[px.Scatter(
        y=reversed_list,
        mode='lines',)
    ])

    plot.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                        step="month",
                        stepmode="backward"),
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
        )
    )

    plot.show()
WholeGDP("GDP.csv")