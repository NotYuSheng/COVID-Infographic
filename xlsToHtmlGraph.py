import plotly
import plotly.graph_objects as go
import pandas as pd

excel_file = 'dataset.xlsx'
df = pd.read_excel(excel_file)

confirmed_data = [go.Scatter( x=df['date'], y=df['confirmed'])]
death_data = [go.Scatter( x=df['date'], y=df['deaths'])]
recovered_data = [go.Scatter( x=df['date'], y=df['recovered'])]

confirmed_fig = go.Figure(confirmed_data)
death_fig = go.Figure(death_data)
recoveredfig = go.Figure(recovered_data)

plotly.offline.plot(confirmed_fig, filename="confirmed.html")
plotly.offline.plot(death_fig, filename="death.html")
plotly.offline.plot(recoveredfig, filename="recovered.html")