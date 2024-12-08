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

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#The_year_2008
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in USA in 2008
plt.scatter(2008, "USA", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2008, "USA"), xytext=(2008, "USA"),
             )

#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in United Kingdom in 2008
plt.scatter(2008, "United Kingdom", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2008, "United Kingdom"), xytext=(2008, "United Kingdom"),
             )

#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Switzerland in 2008
plt.scatter(2008, "Switzerland", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2008, "Switzerland"), xytext=(2008, "Switzerland"),
             )

#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Italy in 2008
plt.scatter(2008, "Italy", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2008, "Italy"), xytext=(2008, "Italy"),
             )

#===================================================================================================================================================#
#The_year_2009

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Iran in 2009
plt.scatter(2009, "Iran", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2009, "Iran"), xytext=(2009, "Iran"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Costa Rica in 2009
plt.scatter(2009, "Costa Rica", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2009, "Costa Rica"), xytext=(2009, "Costa Rica"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in China in 2009
plt.scatter(2009, "China", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2009, "China"), xytext=(2009, "China"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Belgium in 2009
plt.scatter(2009, "Belgium", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2009, "Belgium"), xytext=(2009, "Belgium"),
             )

#===================================================================================================================================================#

#The_year_2010

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in United Kingdom in 2010
plt.scatter(2010, "United Kingdom", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2010, "United Kingdom"), xytext=(2010, "United Kingdom"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 3

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Netherlands in 2010
plt.scatter(2010, "Netherlands", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2010, "Netherlands"), xytext=(2010, "Netherlands"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Germany in 2010
plt.scatter(2010, "Germany", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2010, "Germany"), xytext=(2010, "Germany"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Ecuador in 2010
plt.scatter(2010, "Ecuador", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2010, "Ecuador"), xytext=(2010, "Ecuador"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Colombia in 2010
plt.scatter(2010, "Colombia", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2010, "Colombia"), xytext=(2010, "Colombia"),
             )
#===================================================================================================================================================#

#The_year_2011

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in USA in 2011
plt.scatter(2011, "USA", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2011, "USA"), xytext=(2011, "USA"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in France in 2011
plt.scatter(2011, "France", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2011, "France"), xytext=(2011, "France"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Brazil in 2011
plt.scatter(2011, "Brazil", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2011, "Brazil"), xytext=(2011, "Brazil"),
             )
#===================================================================================================================================================#

#The_year_2012

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in USA in 2012
plt.scatter(2012, "USA", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2012, "USA"), xytext=(2012, "USA"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in United Kingdom in 2012
plt.scatter(2012, "United Kingdom", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2012, "United Kingdom"), xytext=(2012, "United Kingdom"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Philippines in 2012
plt.scatter(2012, "Philippines", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2012, "Philippines"), xytext=(2012, "Philippines"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Netherlands in 2012
plt.scatter(2012, "Netherlands", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2012, "Netherlands"), xytext=(2012, "Netherlands"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Italy in 2012
plt.scatter(2012, "Italy", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2012, "Italy"), xytext=(2012, "Italy"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Germany in 2012
plt.scatter(2012, "Germany", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2012, "Germany"), xytext=(2012, "Germany"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in France in 2012
plt.scatter(2012, "France", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2012, "France"), xytext=(2012, "France"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Ecuador  in 2012
plt.scatter(2012, "Ecuador", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2012, "Ecuador"), xytext=(2012, "Ecuador"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Costa Rica in 2012
plt.scatter(2012, "Costa Rica", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2012, "Costa Rica"), xytext=(2012, "Costa Rica"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in China in 2012
plt.scatter(2012, "China", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2012, "China"), xytext=(2012, "China"),
             )

#===================================================================================================================================================#

#The_year_2013
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in USA in 2013
plt.scatter(2013, "USA", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2013, "USA"), xytext=(2013, "USA"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Switzerland in 2013
plt.scatter(2013, "Switzerland", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2013, "Switzerland"), xytext=(2013, "Switzerland"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Sangapore in 2013
plt.scatter(2013, "Sangapore", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2013, "Sangapore"), xytext=(2013, "Sangapore"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Netherlands in 2013
plt.scatter(2013, "Netherlands", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2013, "Netherlands"), xytext=(2013, "Netherlands"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Italy in 2013
plt.scatter(2013, "Italy", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2013, "Italy"), xytext=(2013, "Italy"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Indonesia in 2013
plt.scatter(2013, "Indonesia", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2013, "Indonesia"), xytext=(2013, "Indonesia"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Australia in 2013
plt.scatter(2013, "Australia", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2013, "Australia"), xytext=(2013, "Australia"),
             )

#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Australia in 2013
plt.scatter(2013, "Australia", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2013, "Australia"), xytext=(2013, "Australia"),
             )

#===================================================================================================================================================#

#The_year_2014

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Switzerland in 2014
plt.scatter(2014, "Switzerland", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2014, "Switzerland"), xytext=(2014, "Switzerland"),
             )
#------------------------------------------------------------------------

 # Example value to represent in the bubble
value = 3

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Netherlands in 2014
plt.scatter(2014, "Belgium", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2014, "Belgium"), xytext=(2014, "Belgium"),
             )
#------------------------------------------------------------------------

 # Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Italy in 2014
plt.scatter(2014, "Italy", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2014, "Italy"), xytext=(2014, "Italy"),
             )
#------------------------------------------------------------------------

 # Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Indonesia in 2014
plt.scatter(2014, "Indonesia", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2014, "Indonesia"), xytext=(2014, "Indonesia"),
             )
#------------------------------------------------------------------------


 # Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Ecuador in 2014
plt.scatter(2014, "Ecuador", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2014, "Ecuador"), xytext=(2014, "Ecuador"),
             )
#------------------------------------------------------------------------

 # Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Costa Rica in 2014
plt.scatter(2014, "Costa Rica", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2014, "Costa Rica"), xytext=(2014, "Costa Rica"),
             )
#------------------------------------------------------------------------

 # Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Switzerland in 2014
plt.scatter(2014, "Switzerland", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2014, "Switzerland"), xytext=(2014, "Switzerland"),
             )
#------------------------------------------------------------------------

 # Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Netherlands in 2014
plt.scatter(2014, "Netherlands", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2014, "Netherlands"), xytext=(2014, "Netherlands"),
             )

#===================================================================================================================================================#

#The_year_2015

 # Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in USA in 2015
plt.scatter(2015, "USA", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2015, "USA"), xytext=(2015, "USA"),
             )

#------------------------------------------------------------------------

 # Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Tunisia in 2015
plt.scatter(2015, "Tunisia", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2015, "Tunisia"), xytext=(2015, "Tunisia"),
             )

#------------------------------------------------------------------------

 # Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Singapore in 2015
plt.scatter(2015, "Singapore", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2015, "Singapore"), xytext=(2015, "Singapore"),
             )

#------------------------------------------------------------------------

 # Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Netherlands in 2015
plt.scatter(2015, "Netherlands", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2015, "Netherlands"), xytext=(2015, "Netherlands"),
             )
#------------------------------------------------------------------------
             
 # Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Germany in 2015
plt.scatter(2015, "Germany", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2015, "Germany"), xytext=(2015, "Germany"),
             )

#------------------------------------------------------------------------
 # Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in China in 2015
plt.scatter(2015, "China", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2015, "China"), xytext=(2015, "China"),
             )

#------------------------------------------------------------------------
 
 # Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Brazil in 2015
plt.scatter(2015, "Brazil", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2015, "Brazil"), xytext=(2015, "Brazil"),
             )

#===================================================================================================================================================#

#The_year_2016

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in USA in 2016
plt.scatter(2016, "USA", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2016, "USA"), xytext=(2016, "USA"),
             )

#------------------------------------------------------------------------
 
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Philippines in 2016
plt.scatter(2016, "Philippines", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2016, "Philippines"), xytext=(2016, "Philippines"),
             )

#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Netherlands in 2016
plt.scatter(2016, "Netherlands", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2016, "Netherlands"), xytext=(2016, "Netherlands"),
             )

#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Ecuador in 2016
plt.scatter(2016, "Ecuador", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2016, "Ecuador"), xytext=(2016, "Ecuador"),
             )


#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in China in 2016
plt.scatter(2016, "China", s=bubble_size, c='red', edgecolors="black")

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
plt.scatter(2017, "USA", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "USA"), xytext=(2017, "USA"),
             )

#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in United Kingdom in 2017
plt.scatter(2017, "United Kingdom", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "United Kingdom"), xytext=(2017, "United Kingdom"),
             )

#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Philippines in 2017
plt.scatter(2017, "Philippines", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "Philippines"), xytext=(2017, "Philippines"),
             )

#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 3

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed

# Add a specific point for your presence in Netherlands in 2017
plt.scatter(2017, "Netherlands", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "Netherlands"), xytext=(2017, "Netherlands"),
            )

#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Germany in 2017
plt.scatter(2017, "Germany", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "Germany"), xytext=(2017, "Germany"),
             )

#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed

# Add a specific point for your presence in Colombia in 2017
plt.scatter(2017, "Colombia", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "Colombia"), xytext=(2017, "Colombia"),
            )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed

# Add a specific point for your presence in China in 2017
plt.scatter(2017, "China", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "China"), xytext=(2017, "China")
            )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed

# Add a specific point for your presence in Australia in 2017
plt.scatter(2017, "Australia", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "Australia"), xytext=(2017, "Australia")
            )
#===================================================================================================================================================#

#The_year_2018

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Austria in 2018
plt.scatter(2018, "Austria", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2018, "Austria"), xytext=(2018, "Austria"),
             )
#===================================================================================================================================================#

#The_year_2019

# Example value to represent in the bubble
value = 3

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in USA in 2019
plt.scatter(2019, "USA", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2019, "USA"), xytext=(2019, "USA"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Philippines in 2019
plt.scatter(2019, "Philippines", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2019, "Philippines"), xytext=(2019, "Philippines"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Germany in 2019
plt.scatter(2019, "Germany", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2019, "Germany"), xytext=(2019, "Germany"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Colombia in 2019
plt.scatter(2019, "Colombia", s=bubble_size, c='red', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2019, "Colombia"), xytext=(2019, "Colombia"),
             )
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