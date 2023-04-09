import pandas as pd
import plotly.express as px

# read in the CSV file with the planned Amtrak HSR routes
df = pd.read_csv('amtrak_hsr_routes.csv')

# create a scatter plot of the routes, with the investment amount determining the size of the marker
fig = px.scatter(df, x='start_city', y='end_city', size='investment', hover_data=['investment'], title='Planned Amtrak HSR Routes')
fig.update_layout(xaxis_title='Start City', yaxis_title='End City')

# display the plot
fig.show()
