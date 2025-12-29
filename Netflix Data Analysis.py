# Importing necessary libraries
import pandas as pd
import plotly.express as px
import plotly.offline as pyo


# --- Loading the Netflix dataset ---
# The Netflix Titles dataset is a curated collection of Netflix content
try:
    df = pd.read_csv('netflix_titles.csv',encoding='ISO-8859-1')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: netflix_titles.csv not found.")
    # Exiting the script if the file is not found.
    exit()

# Cleaning column names by replacing spaces with underscores for easier attribute access
df.columns = df.columns.str.replace(' ', '_')


# Handling multiple genres listed in a single string by splitting and expanding
genres_df = df['listed_in'].str.split(', ').explode()

# Counting the occurrences of each genre
genre_counts = genres_df.value_counts().reset_index()
genre_counts.columns = ['Genre', 'Count']

# Get the top 10 genres
top_10_genres = genre_counts.head(10)

# Creating a bar chart to visualize the counts of the top 10 genres
fig1 = px.bar(top_10_genres, x='Genre', y='Count',
              title='Top 10 Netflix Content Genres')

# Saving the figure as an HTML file for offline viewing
pyo.plot(fig1, filename='results/genre_distribution_bar_chart.html')

# Visualizing when content was added to Netflix over time using a line chart
# Converting 'date_added' column to datetime objects for proper time-series analysis
df['date_added'] = pd.to_datetime(
    df['date_added'].str.strip(),  # removes leading/trailing spaces
    format='mixed',
    errors='coerce'
)
# Counting the number of titles added per month and sort the results chronologically
# Using 'to_period('M')' groups by month, and 'sort_index()' ensures chronological order
monthly_additions = df['date_added'].dt.to_period('M').value_counts().sort_index()
# Converting the Period index back to Timestamp for compatibility with Plotly Express plotting
monthly_additions.index = monthly_additions.index.to_timestamp()

# Converting the Series to a DataFrame for Plotly Express
monthly_additions_df = monthly_additions.reset_index()
monthly_additions_df.columns = ['Date', 'Count']

# Creating a line chart to show the trend of content additions over time
fig2 = px.line(monthly_additions_df, x='Date', y='Count',
              title='Number of Titles Added to Netflix Over Time')

# Saving the figure as an HTML file
pyo.plot(fig2, filename='results/content_added_timeline.html')

# Comparing the proportion of movies versus TV shows available on Netflix

# Counting the occurrences of each content type ('Movie' and 'TV Show')
type_counts = df['type'].value_counts().reset_index()
type_counts.columns = ['Type', 'Count']

# Creating a pie chart to show the proportion visually
fig3 = px.pie(type_counts, values='Count', names='Type',
              title='Proportion of Movies vs TV Shows on Netflix')
# Customizing the text displayed on the pie slices
fig3.update_traces(textposition='inside', textinfo='percent+label')

# Saving the figure as an HTML file (generic plot save)
pyo.plot(fig3, filename='results/content_type_proportion_pie_chart.html')


# Analyzing content length trends using a scatter plot

# Filtering the DataFrame to include only entries of type 'Movie'
movies_df = df[df['type'] == 'Movie'].copy()
# Converting the 'duration' string to an integer representing minutes for movies
movies_df['duration_minutes'] = movies_df['duration'].str.replace(' min', '', regex=False).astype(int)

# Creating a scatter plot for Movies showing Release Year versus Duration in Minutes
fig4_movies = px.scatter(movies_df, x='release_year', y='duration_minutes',
                         hover_name='title',
                         title='Movie Duration vs. Release Year',
                         labels={'release_year': 'Release Year', 'duration_minutes': 'Duration (minutes)'})

# Saving the scatter plot for movies as an HTML file
pyo.plot(fig4_movies, filename='results/movie_duration_scatter_plot.html')

# Filtering the DataFrame to include only entries of type 'TV Show'
tv_shows_df = df[df['type'] == 'TV Show'].copy()
# Converting the 'duration' string to an integer representing the number of seasons for TV shows
tv_shows_df['duration_seasons'] = tv_shows_df['duration'].str.replace(' Season.*', '', regex=True).astype(int)

# Creating a scatter plot for TV Shows showing Release Year versus Duration in Seasons
fig4_tvshows = px.scatter(tv_shows_df, x='release_year', y='duration_seasons',
                          hover_name='title',
                          title='TV Show Duration vs. Release Year',
                          labels={'release_year': 'Release Year', 'duration_seasons': 'Duration (seasons)'})

# Saving the scatter plot for TV shows as an HTML file
pyo.plot(fig4_tvshows, filename='results/tvshow_duration_scatter_plot.html')

# Plotting a choropleth map to show the distribution of content production by country
# Removing rows where 'country' information is missing
country_df = df.dropna(subset=['country']).copy()

# Handling entries where multiple countries are listed for a single title: split the string and count each country individually
country_counts_list = country_df['country'].str.split(', ').explode()

# counting the total number of titles associated with each country
country_counts = country_counts_list.value_counts().reset_index()
country_counts.columns = ['Country', 'Count']

# Creating a choropleth map using Plotly Express

fig5 = px.choropleth(country_counts,
                     locations='Country',
                     locationmode='country names',
                     color='Count',
                     hover_name='Country',
                     color_continuous_scale=px.colors.sequential.Plasma,
                     title='Netflix Content Production by Country',
                     projection='natural earth')

# Customizing the layout of the map
fig5.update_layout(
    title_text='Netflix Content Production by Country',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='natural earth'
    )
)

# Saving the choropleth map as an HTML file
pyo.plot(fig5, filename='results/content_production_choropleth_map.html')

