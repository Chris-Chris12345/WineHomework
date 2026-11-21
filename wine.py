import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots


df = pd.read_csv("WineQT.csv")
#Sort the DataFrame by quality to ensure a clean color gradient
df = df.sort_values("quality")

#Define the shared color palette (Viridis adapted for discrete classes)
unique_qualities = df["quality"].nunique()
viridis_palette = px.colors.sample_colorscale("Viridis", [i/(unique_qualities-1) for i in range(unique_qualities)])


fig = make_subplots(
    rows=1, 
    cols=3,
    subplot_titles=(
        "Alcohol Content by Quality", 
        "Alcohol vs Density (Size = Sulphates)",
    )
)


fig_hist = px.histogram(
    df, 
    x="alcohol", 
    color="quality", 
    color_discrete_sequence=viridis_palette
)


fig_scatter = px.scatter(
    df, 
    x="alcohol", 
    y="density", 
    color="quality", 
    size="sulphates",
    color_discrete_sequence=viridis_palette
)

#Assemble the two requested graphs into the layout structure
for trace in fig_hist.data:
    fig.add_trace(trace, row=1, col=1)

for trace in fig_scatter.data:
    fig.add_trace(trace, row=1, col=2)

#Configure the Global Title and the Shared Theme
fig.update_layout(
    title_text="Wine Quality & Chemical Properties Dashboard",
    title_font_size=22,
    title_x=0.5,                    # Center the dashboard title
    template="plotly_dark",          # Shared dark theme
    showlegend=False,               # Hide repetitive legends
    height=550
)

#Configure axis labels for Graph 1 and Graph 2
fig.update_xaxes(title_text="Alcohol(%)", row=1, col=1)
fig.update_xaxes(title_text="Alcohol(%)", row=1, col=2)

fig.update_yaxes(title_text="Wine Count", row=1, col=1)
fig.update_yaxes(title_text="Density", row=1, col=2)



fig.write_html("wine_dashboard.html", auto_open=True)