import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

df = pd.read_csv("WineQT.csv")
df = df.sort_values("quality")

print(df.shape)
print(df.columns)
print(df.info())
print(df.describe)
print(df.isnull().sum())

#Convert quality into categories for giving colours
df["quality"] = df["quality"].astype(str)

fig = make_subplots(
    rows=1,
    cols=3,
    subplot_titles=("Alcohol content by quality","Alcohol VS Density")
)

hist = px.histogram(df,
                    x="alcohol",
                    color="quality")

scatter = px.scatter(df,
                     x="alcohol",
                     y="density",
                     color="quality",
                     size="sulphates")

for trace in hist.data:
    fig.add_trace(trace, row=1, col=1)
for trace in scatter.data:
    fig.add_trace(trace, row=1, col=2)

fig.update_layout(title="Wine quality dashboard",
                  template="plotly_dark",
                  height=600,
                  showlegend=True)

fig.update_xaxes(title_text="Alcohol (%)",row=1,col=1)
fig.update_yaxes(title_text="Wine Count",row=1,col=1)

fig.update_xaxes(title_text="Alcohol (%)",row=1,col=2)
fig.update_yaxes(title_text="Density",row=1,col=2)

fig.show()