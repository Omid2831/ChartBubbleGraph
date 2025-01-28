import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# List of countries
countries = [
    "USA", "United Kingdom", "Tunisia", "Tanzania", "Switzerland", 
    "Singapore", "Philippines", "Panama", "Netherlands", "Italy", 
    "Iran", "Indonesia", "Germany", "France", "Ecuador", 
    "Cuba", "Costa Rica", "Colombia", "China", "Brazil", 
    "Belgium", "Austria", "Australia"
]

# Generate random years and number of talks for each country
data = {
    "Country": [],
    "Year": [],
    "Number of Talks": []
}

# Populate the data dictionary
for country in countries:
    year = np.random.choice(range(2008, 2025))  # Random year between 2008 and 2024
    number_of_talks = np.random.randint(1, 5)  # Random number of talks between 1 and 4
    data["Country"].append(country)
    data["Year"].append(year)
    data["Number of Talks"].append(number_of_talks)

# Convert to DataFrame
df = pd.DataFrame(data)

# Create a list of years from 2008 to 2024
years = list(range(2008, 2025))

# Create the bubble chart
plt.figure(figsize=(14, 10))
scatter = plt.scatter(
    df["Year"], 
    df["Country"], 
    s=df["Number of Talks"] * 100,  # Bubble size
    alpha=0.6,
    c='blue',
    edgecolors="black"
)

# Function to add a specific point if it doesn't already exist
def add_point(year, country, value, color):
    if not ((df["Year"] == year) & (df["Country"] == country)).any():
        bubble_size = value * 550  # Adjust the multiplier as needed
        plt.scatter(year, country, s=bubble_size, c=color, edgecolors="black")
        plt.annotate(str(value), xy=(year, country), xytext=(year, country))

# Add specific points
add_point(2008, "USA", 1, 'lightblue')
add_point(2008, "United Kingdom", 1, 'red')
add_point(2008, "Switzerland", 1, 'aqua')
add_point(2008, "Italy", 1, 'magenta')
add_point(2009, "Iran", 1, 'slateblue')
add_point(2009, "Costa Rica", 1, 'gray')
add_point(2009, "China", 1, 'orange')
add_point(2009, "Belgium", 1, 'palegoldenrod')
add_point(2010, "United Kingdom", 1, 'red')
add_point(2010, "Netherlands", 3, 'teal')
add_point(2010, "Germany", 1, 'peru')
add_point(2010, "Ecuador", 1, 'yellowgreen')
add_point(2010, "Colombia", 1, 'coral')
add_point(2011, "USA", 1, 'lightblue')
add_point(2011, "France", 1, 'brown')
add_point(2011, "Brazil", 1, 'thistle')
add_point(2012, "USA", 1, 'lightblue')
add_point(2012, "United Kingdom", 1, 'red')
add_point(2012, "Philippines", 1, 'ivory')
add_point(2012, "Netherlands", 1, 'teal')
add_point(2012, "Italy", 1, 'magenta')
add_point(2012, "Germany", 1, 'peru')
add_point(2012, "France", 1, 'brown')
add_point(2012, "Ecuador", 1, 'yellowgreen')
add_point(2012, "Costa Rica", 2, 'gray')
add_point(2012, "China", 1, 'orange')
add_point(2013, "USA", 1, 'lightblue')
add_point(2013, "Switzerland", 2, 'aqua')
add_point(2013, "Singapore", 1, 'peachpuff')
add_point(2013, "Netherlands", 1, 'teal')
add_point(2013, "Italy", 1, 'magenta')
add_point(2013, "Indonesia", 1, 'violet')
add_point(2013, "Australia", 1, 'gold')
add_point(2014, "Switzerland", 1, 'aqua')
add_point(2014, "Netherlands", 3, 'teal')
add_point(2014, "Italy", 2, 'magenta')
add_point(2014, "Indonesia", 1, 'violet')
add_point(2014, "Ecuador", 1, 'yellowgreen')
add_point(2014, "Costa Rica", 2, 'gray')
add_point(2014, "Colombia", 2, 'coral')
add_point(2014, "Belgium", 1, 'palegoldenrod')
add_point(2015, "USA", 1, 'lightblue')
add_point(2015, "Tunisia", 2, 'lightgreen')
add_point(2015, "Singapore", 1, 'peachpuff')
add_point(2015, "Netherlands", 2, 'teal')
add_point(2015, "Germany", 2, 'peru')
add_point(2015, "China", 2, 'orange')
add_point(2015, "Brazil", 2, 'thistle')
add_point(2016, "USA", 1, 'lightblue')
add_point(2016, "Philippines", 1, 'ivory')
add_point(2016, "Netherlands", 1, 'teal')
add_point(2016, "Ecuador", 1, 'yellowgreen')
add_point(2016, "China", 2, 'orange')
add_point(2017, "USA", 3, 'lightblue')
add_point(2017, "United Kingdom", 1, 'red')
add_point(2017, "Philippines", 1, 'ivory')
add_point(2017, "Netherlands", 3, 'teal')
add_point(2017, "Germany", 1, 'peru')
add_point(2017, "Colombia", 1, 'coral')
add_point(2017, "China", 1, 'orange')
add_point(2017, "Australia", 1, 'gold')
add_point(2018, "Austria", 1, 'oldlace')
add_point(2019, "USA", 3, 'lightblue')
add_point(2019, "Philippines", 1, 'ivory')
add_point(2019, "Germany", 2, 'peru')
add_point(2019, "Colombia", 1, 'coral')
add_point(2020, "Panama", 1, 'lightpink')
add_point(2020, "Netherlands", 1, 'teal')
add_point(2020, "Germany", 1, 'peru')
add_point(2021, "Germany", 1, 'peru')
add_point(2022, "Tanzania", 1, 'lightyellow')
add_point(2022, "Netherlands", 3, 'teal')
add_point(2022, "Germany", 1, 'peru')
add_point(2022, "Ecuador", 1, 'yellowgreen')
add_point(2023, "USA", 1, 'lightblue')
add_point(2023, "Netherlands", 1, 'teal')
add_point(2023, "Indonesia", 3, 'violet')
add_point(2023, "France", 2, 'brown')
add_point(2023, "Ecuador", 1, 'yellowgreen')
add_point(2023, "Colombia", 1, 'coral')
add_point(2023, "Belgium", 1, 'palegoldenrod')
add_point(2024, "Switzerland", 1, 'aqua')
add_point(2024, "Panama", 1, 'lightpink')
add_point(2024, "Ecuador", 1, 'yellowgreen')
add_point(2024, "Costa Rica", 1, 'gray')

# Labeling
plt.title("Number of Talks by Country and Year", fontsize=25)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Country", fontsize=14)

# Set x-ticks to show years from 2008 to 2024
plt.xticks(years)

# Add a legend
plt.legend()

# Show the plot
plt.grid(alpha=0.4)
plt.show()
