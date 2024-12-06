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

#The_year_2008

# Add a specific point for your presence in USA in 2008
plt.scatter(2008, "USA", s=100, c='red', edgecolors="black", label='USA')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2008, "USA"), xytext=(2009, "USA"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in United Kingdom in 2008
plt.scatter(2008, "United Kingdom", s=100, c='red', edgecolors="black", label='United Kingdom')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2008, "United Kingdom"), xytext=(2009, "United Kingdom"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in Switzerland in 2008
plt.scatter(2008, "Switzerland", s=100, c='red', edgecolors="black", label='Switzerland')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2008, "Switzerland"), xytext=(2009, "Switzerland"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in Italy in 2008
plt.scatter(2008, "Italy", s=100, c='red', edgecolors="black", label='Italy')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2008, "Italy"), xytext=(2009, "Italy"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------

#===================================================================================================================================================#
#The_year_2009

# Add a specific point for your presence in Iran in 2009
plt.scatter(2009, "Iran", s=100, c='red', edgecolors="black", label='Iran')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2009, "Iran"), xytext=(2010, "Iran"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in Costa Rika in 2009
plt.scatter(2009, "Costa Rica", s=100, c='red', edgecolors="black", label='Costa Rika')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2009, "Costa Rica"), xytext=(2010, "Costa Rica"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in China in 2009
plt.scatter(2009, "China", s=100, c='red', edgecolors="black", label='China')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2009, "China"), xytext=(2010, "China"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in Belgium in 2009
plt.scatter(2009, "Belgium", s=100, c='red', edgecolors="black", label='Belgium')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2009, "Belgium"), xytext=(2010, "Belgium"),
             arrowprops=dict(facecolor='black', shrink=0.05))

#===================================================================================================================================================#

#The_year_2010

# Add a specific point for your presence in United Kingdom in 2010
plt.scatter(2010, "United Kingdom", s=100, c='red', edgecolors="black", label='United Kingdom')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2010, "United Kingdom"), xytext=(2011, "United Kingdom"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in Netherlands in 2010
plt.scatter(2010, "Netherlands", s=100, c='red', edgecolors="black", label='Netherlands')

# Annotate the point to specify it was a single visit
plt.annotate('3', xy=(2010, "Netherlands"), xytext=(2011, "Netherlands"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in Germany in 2010
plt.scatter(2010, "Germany", s=100, c='red', edgecolors="black", label='Germany')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2010, "Germany"), xytext=(2011, "Germany"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in Ecuador in 2010
plt.scatter(2010, "Ecuador", s=100, c='red', edgecolors="black", label='Ecuador')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2010, "Ecuador"), xytext=(2011, "Ecuador"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in Colombia in 2010
plt.scatter(2010, "Colombia", s=100, c='red', edgecolors="black", label='Colombia')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2010, "Colombia"), xytext=(2011, "Colombia"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#===================================================================================================================================================#

#The_year_2011

# Add a specific point for your presence in USA in 2011
plt.scatter(2011, "USA", s=100, c='red', edgecolors="black", label='USA')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2011, "USA"), xytext=(2012, "USA"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in France in 2011
plt.scatter(2011, "France", s=100, c='red', edgecolors="black", label='France')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2011, "France"), xytext=(2012, "France"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in Brazil in 2011
plt.scatter(2011, "Brazil", s=100, c='red', edgecolors="black", label='Brazil')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2011, "Brazil"), xytext=(2012, "Brazil"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#===================================================================================================================================================#

#The_year_2012

# Add a specific point for your presence in USA in 2012
plt.scatter(2012, "USA", s=100, c='red', edgecolors="black", label='USA')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2012, "USA"), xytext=(2013, "USA"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in United Kingdom in 2012
plt.scatter(2012, "United Kingdom", s=100, c='red', edgecolors="black", label='United Kingdom')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2012, "United Kingdom"), xytext=(2013, "United Kingdom"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in Philippines in 2012
plt.scatter(2012, "Philippines", s=100, c='red', edgecolors="black", label='Philippines')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2012, "Philippines"), xytext=(2013, "Philippines"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in Netherlands in 2012
plt.scatter(2012, "Netherlands", s=100, c='red', edgecolors="black", label='Netherlands')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2012, "Netherlands"), xytext=(2013, "Netherlands"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in Italy in 2012
plt.scatter(2012, "Italy", s=100, c='red', edgecolors="black", label='Italy')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2012, "Italy"), xytext=(2013, "Italy"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in Italy in 2012
plt.scatter(2012, "Italy", s=100, c='red', edgecolors="black", label='Italy')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2012, "Italy"), xytext=(2013, "Italy"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in Germany in 2012
plt.scatter(2012, "Germany", s=100, c='red', edgecolors="black", label='Germany')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2012, "Germany"), xytext=(2013, "Germany"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in France in 2012
plt.scatter(2012, "France", s=100, c='red', edgecolors="black", label='France')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2012, "France"), xytext=(2013, "France"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in Ecuador in 2012
plt.scatter(2012, "Ecuador", s=100, c='red', edgecolors="black", label='Ecuador')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2012, "Ecuador"), xytext=(2013, "Ecuador"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in Costa Rica in 2012
plt.scatter(2012, "Costa Rica", s=100, c='red', edgecolors="black", label='Costa Rica')

# Annotate the point to specify it was a single visit
plt.annotate('2', xy=(2012, "Costa Rica"), xytext=(2013, "Costa Rica"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in Costa Rica in 2012
plt.scatter(2012, "Costa Rica", s=100, c='red', edgecolors="black", label='Costa Rica')

# Annotate the point to specify it was a single visit
plt.annotate('2', xy=(2012, "Costa Rica"), xytext=(2013, "Costa Rica"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------
# Add a specific point for your presence in China in 2012
plt.scatter(2012, "China", s=100, c='red', edgecolors="black", label='China')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2012, "China"), xytext=(2013, "China"),
             arrowprops=dict(facecolor='black', shrink=0.05))

#===================================================================================================================================================#




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