# Data-Analysis-and-Visualisation

````md
# Exploratory Data Analysis of Netflix Titles

##  Project Overview
This project performs an exploratory data analysis (EDA) on the Netflix Titles dataset using **Python**, **pandas**, and **Plotly**.  
The goal is to clean the dataset, handle mixed date formats, and generate interactive visualizations to uncover trends in Netflix content.

The analysis focuses on:
- Genre distribution
- Content additions over time
- Movies vs TV shows comparison
- Content duration trends
- Global content production by country

All visualizations are saved as **interactive HTML files** for offline viewing.

---

##  Dataset
- **Name:** Netflix Titles Dataset
- **Source:** Public Netflix dataset (CSV format)
- **Encoding:** ISO-8859-1
- **Key Columns Used:**
  - `type`
  - `title`
  - `listed_in`
  - `date_added`
  - `release_year`
  - `duration`
  - `country`

---

##  Technologies Used
- **Python**
- **pandas** – data loading and cleaning
- **Plotly Express** – interactive visualizations
- **Plotly Offline** – saving charts as HTML files

---

##  Data Cleaning & Preparation
- Standardized column names by replacing spaces with underscores
- Split and expanded multi-value fields such as genres and countries
- Cleaned and parsed the `date_added` column:
  - Removed leading/trailing whitespace
  - Handled mixed date formats using `format='mixed'`
  - Invalid dates converted to `NaT` using `errors='coerce'`
- Converted duration fields into numeric values:
  - Movie duration → minutes
  - TV show duration → number of seasons

---

##  Visualizations Generated
The project produces the following interactive charts:

1. **Top 10 Netflix Content Genres** (Bar Chart)  
   `genre_distribution_bar_chart.html`

2. **Titles Added Over Time** (Line Chart)  
   `content_added_timeline.html`

3. **Movies vs TV Shows Proportion** (Pie Chart)  
   `content_type_proportion_pie_chart.html`

4. **Movie Duration vs Release Year** (Scatter Plot)  
   `movie_duration_scatter_plot.html`

5. **TV Show Duration vs Release Year** (Scatter Plot)  
   `tvshow_duration_scatter_plot.html`

6. **Global Content Production by Country** (Choropleth Map)  
   `content_production_choropleth_map.html`

---

##  How to Run the Project
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/netflix-eda.git
````

2. Install required libraries:

   ```bash
   pip install pandas plotly
   ```
3. Update the dataset path in the script if necessary.
4. Run the Python script:

   ```bash
   python netflix_analysis.py
   ```
5. Open the generated `.html` files in a web browser to view the visualizations.

---

## ⚠️ Notes & Limitations

* Some titles contain missing or inconsistent metadata.
* Mixed date formats required additional cleaning.
* Country and genre counts may be inflated due to multi-country and multi-genre entries per title.

---

##  Learning Outcomes

* Practical data cleaning with pandas
* Handling mixed date formats in real-world datasets
* Exploratory data analysis techniques
* Creating interactive visualizations with Plotly
* Saving and sharing offline visual analytics

---

## Author

**Andiswa Dlamini**

```


