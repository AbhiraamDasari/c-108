import csv
from pickle import FALSE 
import pandas as pd
import plotly.figure_factory as ff

data = pd.read_csv("data.csv")
figure = ff.create_distplot([data["Height(Inches)"].tolist()],["Height"],show_hist=False)
figure.show()