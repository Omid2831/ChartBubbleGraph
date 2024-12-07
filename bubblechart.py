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
    alpha=0.0,
    c='blue',
    edgecolors="black"
)

# shrink the size of the black arrows to prevent from collision with the other bubbles and clean the graph from crowdedness



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

#The_year_2013

# Add a specific point for your presence in USA in 2013
plt.scatter(2013, "USA", s=100, c='red', edgecolors="black", label='USA')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2013, "USA"), xytext=(2014, "USA"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------

# Add a specific point for your presence in Switzerland in 2013
plt.scatter(2013, "Switzerland", s=100, c='red', edgecolors="black", label='Switzerland')

# Annotate the point to specify it was a single visit
plt.annotate('2', xy=(2013, "Switzerland"), xytext=(2014, "Switzerland"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------

# Add a specific point for your presence in Singapore in 2013
plt.scatter(2013, "Singapore", s=100, c='red', edgecolors="black", label='Singapore')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2013, "Singapore"), xytext=(2014, "Singapore"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------

# Add a specific point for your presence in Netherlands in 2013
plt.scatter(2013, "Netherlands", s=100, c='red', edgecolors="black", label='Netherlands')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2013, "Netherlands"), xytext=(2014, "Netherlands"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------

# Add a specific point for your presence in Italy in 2013
plt.scatter(2013, "Italy", s=100, c='red', edgecolors="black", label='Italy')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2013, "Italy"), xytext=(2014, "Italy"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------

# Add a specific point for your presence in Indonesia in 2013
plt.scatter(2013, "Indonesia", s=100, c='red', edgecolors="black", label='Indonesia')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2013, "Indonesia"), xytext=(2014, "Indonesia"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------

# Add a specific point for your presence in Ecuador in 2013
plt.scatter(2013, "Ecuador", s=100, c='red', edgecolors="black", label='Ecuador')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2013, "Ecuador"), xytext=(2014, "Ecuador"),
             arrowprops=dict(facecolor='black', shrink=0.05))
#------------------------------------------------------------------------

# Add a specific point for your presence in Australia in 2013
plt.scatter(2013, "Australia", s=100, c='red', edgecolors="black", label='Australia')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2013, "Australia"), xytext=(2014, "Australia"),
             arrowprops=dict(facecolor='black', shrink=0.05))

#===================================================================================================================================================#

#The_year_2014

# Add a specific point for your presence in Switzerland in 2014
plt.scatter(2014, "Switzerland", s=100, c='red', edgecolors="black", label='Switzerland')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2014, "Switzerland"), xytext=(2014.3, "Switzerland"),
             arrowprops=dict(facecolor='black', shrink=0.02))
#------------------------------------------------------------------------

# Add a specific point for your presence in Netherlands in 2014
plt.scatter(2014, "Netherlands", s=100, c='red', edgecolors="black", label='Netherlands')

# Annotate the point to specify it was a single visit
plt.annotate('3', xy=(2014, "Netherlands"), xytext=(2014.3, "Netherlands"),
             arrowprops=dict(facecolor='black', shrink=0.02))
#------------------------------------------------------------------------

# Add a specific point for your presence in Italy in 2014
plt.scatter(2014, "Italy", s=100, c='red', edgecolors="black", label='Italy')

# Annotate the point to specify it was a single visit
plt.annotate('2', xy=(2014, "Italy"), xytext=(2014.3, "Italy"),
             arrowprops=dict(facecolor='black', shrink=0.02))
#------------------------------------------------------------------------
# Add a specific point for your presence in Indonesia in 2014
plt.scatter(2014, "Indonesia", s=100, c='red', edgecolors="black", label='Indonesia')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2014, "Indonesia"), xytext=(2014.3, "Indonesia"),
             arrowprops=dict(facecolor='black', shrink=0.02))
#------------------------------------------------------------------------

# Add a specific point for your presence in Ecuador in 2014
plt.scatter(2014, "Ecuador", s=100, c='red', edgecolors="black", label='Ecuador')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2014, "Ecuador"), xytext=(2014.3, "Ecuador"),
             arrowprops=dict(facecolor='black', shrink=0.02))
#------------------------------------------------------------------------

# Add a specific point for your presence in Costa Rica in 2014
plt.scatter(2014, "Costa Rica", s=100, c='red', edgecolors="black", label='Costa Rica')

# Annotate the point to specify it was a single visit
plt.annotate('2', xy=(2014, "Costa Rica"), xytext=(2014.3, "Costa Rica"),
             arrowprops=dict(facecolor='black', shrink=0.02))
#------------------------------------------------------------------------
# Add a specific point for your presence in Colombia in 2014
plt.scatter(2014, "Colombia", s=100, c='red', edgecolors="black", label='Colombia')

# Annotate the point to specify it was a single visit
plt.annotate('2', xy=(2014, "Colombia"), xytext=(2014.3, "Colombia"),
             arrowprops=dict(facecolor='black', shrink=0.02))
#------------------------------------------------------------------------

# Add a specific point for your presence in Belgium in 2014
plt.scatter(2014, "Belgium", s=100, c='red', edgecolors="black", label='Belgium')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2014, "Belgium"), xytext=(2014.3, "Belgium"),
             arrowprops=dict(facecolor='black', shrink=0.02))

#===================================================================================================================================================#

#The_year_2015

# Add a specific point for your presence in USA in 2015
plt.scatter(2015, "USA", s=100, c='red', edgecolors="black", label='USA')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2015, "USA"), xytext=(2015.3, "USA"),
             arrowprops=dict(facecolor='black', shrink=0.02))

#------------------------------------------------------------------------

# Add a specific point for your presence in Tunisia in 2015
plt.scatter(2015, "Tunisia", s=100, c='red', edgecolors="black", label='Tunisia')

# Annotate the point to specify it was a single visit
plt.annotate('2', xy=(2015, "Tunisia"), xytext=(2015.3, "Tunisia"),
             arrowprops=dict(facecolor='black', shrink=0.02))

#------------------------------------------------------------------------

# Add a specific point for your presence in Singapore in 2015
plt.scatter(2015, "Singapore", s=100, c='red', edgecolors="black", label='Singapore')

# Annotate the point to specify it was a single visit
plt.annotate('1', xy=(2015, "Singapore"), xytext=(2015.3, "Singapore"),
             arrowprops=dict(facecolor='black', shrink=0.02))

#------------------------------------------------------------------------

# Add a specific point for your presence in Netherlands in 2015
plt.scatter(2015, "Netherlands", s=100, c='red', edgecolors="black", label='Netherlands')

# Annotate the point to specify it was a single visit
plt.annotate('2', xy=(2015, "Netherlands"), xytext=(2015.3, "Netherlands"),
             arrowprops=dict(facecolor='black', shrink=0.02))
#------------------------------------------------------------------------
             
# Add a specific point for your presence in Germany in 2015
plt.scatter(2015, "Germany", s=100, c='red', edgecolors="black", label='Germany')

# Annotate the point to specify it was a single visit
plt.annotate('2', xy=(2015, "Germany"), xytext=(2015.3, "Germany"),
             arrowprops=dict(facecolor='black', shrink=0.02))

#------------------------------------------------------------------------

# Add a specific point for your presence in China in 2015
plt.scatter(2015, "China", s=100, c='red', edgecolors="black", label='China')

# Annotate the point to specify it was a single visit
plt.annotate('2', xy=(2015, "China"), xytext=(2015.3, "China"),
             arrowprops=dict(facecolor='black', shrink=0.02))

#------------------------------------------------------------------------

# Add a specific point for your presence in Brazil in 2016
plt.scatter(2015, "Brazil", s=100, c='red', edgecolors="black", label='Brazil')

# Annotate the point to specify it was a single visit
plt.annotate('2', xy=(2015, "Brazil"), xytext=(2015.3, "Brazil"),
             arrowprops=dict(facecolor='black', shrink=0.02))

#===================================================================================================================================================#

#The_year_2016

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in USA in 2016
plt.scatter(2016, "USA", s=bubble_size, c='red', edgecolors="black", label='USA')

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2016, "USA"), xytext=(2016, "USA"),
             )

#------------------------------------------------------------------------
 
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Philippines in 2016
plt.scatter(2016, "Philippines", s=bubble_size, c='red', edgecolors="black", label='Philippines')

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2016, "Philippines"), xytext=(2016, "Philippines"),
             )

#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Netherlands in 2016
plt.scatter(2016, "Netherlands", s=bubble_size, c='red', edgecolors="black", label='Netherlands')

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2016, "Netherlands"), xytext=(2016, "Netherlands"),
             )

#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Ecuador in 2016
plt.scatter(2016, "Ecuador", s=bubble_size, c='red', edgecolors="black", label='Ecuador')

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2016, "Ecuador"), xytext=(2016, "Ecuador"),
             )


#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in China in 2016
plt.scatter(2016, "China", s=bubble_size, c='red', edgecolors="black", label='China')

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2016, "China"), xytext=(2016, "China"),
             )

#===================================================================================================================================================#

#The_year_2017

# Example value to represent in the bubble
value = 3

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in USA in 2017
plt.scatter(2017, "USA", s=bubble_size, c='red', edgecolors="black", label='USA')

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "USA"), xytext=(2017, "USA"),
             )

#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in United Kingdom in 2017
plt.scatter(2017, "United Kingdom", s=bubble_size, c='red', edgecolors="black", label='United Kingdom')

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "United Kingdom"), xytext=(2017, "United Kingdom"),
             )

#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Philippines in 2017
plt.scatter(2017, "Philippines", s=bubble_size, c='red', edgecolors="black", label='Philippines')

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "Philippines"), xytext=(2017, "Philippines"),
             )

#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 3

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed

# Add a specific point for your presence in Netherlands in 2017
plt.scatter(2017, "Netherlands", s=bubble_size, c='red', edgecolors="black", label='Netherlands')

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "Netherlands"), xytext=(2017, "Netherlands"),
            )

#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Germany in 2017
plt.scatter(2017, "Germany", s=bubble_size, c='red', edgecolors="black", label='Germany')

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "Germany"), xytext=(2017, "Germany"),
             )

#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed

# Add a specific point for your presence in Colombia in 2017
plt.scatter(2017, "Colombia", s=bubble_size, c='red', edgecolors="black", label='Colombia')

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "Colombia"), xytext=(2017, "Colombia"),
            )
#------------------------------------------------------------------------









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