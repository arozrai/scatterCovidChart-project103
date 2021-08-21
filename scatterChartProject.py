import pandas as pd
import plotly.express as px

df = pd.read_csv("covidData.csv")
figure = px.scatter(df,x = "date",y = "cases",color = "country",size_max = 60, title = "covid cases")
figure.show()