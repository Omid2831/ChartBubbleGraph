import tkinter as Tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

#on work
# Function to open file dialog and load Excel files
#def load_excel_file():
   # Create a Tkinter root window and hide it 
#    root = Tk.Tk()
#    root.withdraw()

    # Open file dialog to select Excel files
#    file_paths = filedialog.askopenfilenames( title="Select Excel Files", filetypes=[("Excel files", "*.xlsx *.xls")])
    
    # Process each selected file
 #   for file_path in file_paths:
  #      df = pd.read_excel(file_path)
   #     print(f"Loaded {file_path}")
  #      print(df.head())  # Display the first few rows of the dataframe

# Call the function to load Excel files
#load_excel_file()


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
plt.scatter(2008, "USA", s=bubble_size, c='lightblue', edgecolors="black")

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
plt.scatter(2008, "Switzerland", s=bubble_size, c='aqua', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2008, "Switzerland"), xytext=(2008, "Switzerland"),
             )

#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Italy in 2008
plt.scatter(2008, "Italy", s=bubble_size, c='magenta', edgecolors="black")

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
plt.scatter(2009, "Iran", s=bubble_size, c='slateblue', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2009, "Iran"), xytext=(2009, "Iran"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Costa Rica in 2009
plt.scatter(2009, "Costa Rica", s=bubble_size, c='gray', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2009, "Costa Rica"), xytext=(2009, "Costa Rica"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in China in 2009
plt.scatter(2009, "China", s=bubble_size, c='orange', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2009, "China"), xytext=(2009, "China"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Belgium in 2009
plt.scatter(2009, "Belgium", s=bubble_size, c='palegoldenrod', edgecolors="black")

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
plt.scatter(2010, "Netherlands", s=bubble_size, c='teal', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2010, "Netherlands"), xytext=(2010, "Netherlands"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Germany in 2010
plt.scatter(2010, "Germany", s=bubble_size, c='peru', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2010, "Germany"), xytext=(2010, "Germany"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Ecuador in 2010
plt.scatter(2010, "Ecuador", s=bubble_size, c='yellowgreen', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2010, "Ecuador"), xytext=(2010, "Ecuador"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Colombia in 2010
plt.scatter(2010, "Colombia", s=bubble_size, c='coral', edgecolors="black")

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
plt.scatter(2011, "USA", s=bubble_size, c='lightblue', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2011, "USA"), xytext=(2011, "USA"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in France in 2011
plt.scatter(2011, "France", s=bubble_size, c='Brown', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2011, "France"), xytext=(2011, "France"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Brazil in 2011
plt.scatter(2011, "Brazil", s=bubble_size, c='thistle', edgecolors="black")

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
plt.scatter(2012, "USA", s=bubble_size, c='lightblue', edgecolors="black")

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
plt.scatter(2012, "Philippines", s=bubble_size, c='ivory', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2012, "Philippines"), xytext=(2012, "Philippines"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Netherlands in 2012
plt.scatter(2012, "Netherlands", s=bubble_size, c='teal', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2012, "Netherlands"), xytext=(2012, "Netherlands"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Italy in 2012
plt.scatter(2012, "Italy", s=bubble_size, c='magenta', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2012, "Italy"), xytext=(2012, "Italy"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Germany in 2012
plt.scatter(2012, "Germany", s=bubble_size, c='peru', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2012, "Germany"), xytext=(2012, "Germany"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in France in 2012
plt.scatter(2012, "France", s=bubble_size, c='Brown', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2012, "France"), xytext=(2012, "France"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Ecuador  in 2012
plt.scatter(2012, "Ecuador", s=bubble_size, c='yellowgreen', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2012, "Ecuador"), xytext=(2012, "Ecuador"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Costa Rica in 2012
plt.scatter(2012, "Costa Rica", s=bubble_size, c='gray', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2012, "Costa Rica"), xytext=(2012, "Costa Rica"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in China in 2012
plt.scatter(2012, "China", s=bubble_size, c='orange', edgecolors="black")

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
plt.scatter(2013, "USA", s=bubble_size, c='lightblue', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2013, "USA"), xytext=(2013, "USA"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Switzerland in 2013
plt.scatter(2013, "Switzerland", s=bubble_size, c='aqua', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2013, "Switzerland"), xytext=(2013, "Switzerland"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Singapore in 2013
plt.scatter(2013, "Singapore", s=bubble_size, c='peachpuff', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2013, "Singapore"), xytext=(2013, "Singapore"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Netherlands in 2013
plt.scatter(2013, "Netherlands", s=bubble_size, c='teal', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2013, "Netherlands"), xytext=(2013, "Netherlands"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Italy in 2013
plt.scatter(2013, "Italy", s=bubble_size, c='magenta', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2013, "Italy"), xytext=(2013, "Italy"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Indonesia in 2013
plt.scatter(2013, "Indonesia", s=bubble_size, c='violet', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2013, "Indonesia"), xytext=(2013, "Indonesia"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Australia in 2013
plt.scatter(2013, "Australia", s=bubble_size, c='gold', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2013, "Australia"), xytext=(2013, "Australia"),
             )

#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Australia in 2013
plt.scatter(2013, "Australia", s=bubble_size, c='gold', edgecolors="black")

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
plt.scatter(2014, "Switzerland", s=bubble_size, c='aqua', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2014, "Switzerland"), xytext=(2014, "Switzerland"),
             )
#------------------------------------------------------------------------

 # Example value to represent in the bubble
value = 3

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Netherlands in 2014
plt.scatter(2014, "Netherlands", s=bubble_size, c='teal', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2014, "Netherlands"), xytext=(2014, "Netherlands"),
             )
#------------------------------------------------------------------------

 # Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Italy in 2014
plt.scatter(2014, "Italy", s=bubble_size, c='magenta', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2014, "Italy"), xytext=(2014, "Italy"),
             )
#------------------------------------------------------------------------

 # Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Indonesia in 2014
plt.scatter(2014, "Indonesia", s=bubble_size, c='violet', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2014, "Indonesia"), xytext=(2014, "Indonesia"),
             )
#------------------------------------------------------------------------


 # Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Ecuador in 2014
plt.scatter(2014, "Ecuador", s=bubble_size, c='yellowgreen', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2014, "Ecuador"), xytext=(2014, "Ecuador"),
             )
#------------------------------------------------------------------------

 # Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Costa Rica in 2014
plt.scatter(2014, "Costa Rica", s=bubble_size, c='gray', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2014, "Costa Rica"), xytext=(2014, "Costa Rica"),
             )
#------------------------------------------------------------------------

  # Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Colombia in 2014
plt.scatter(2014, "Colombia", s=bubble_size, c='coral', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2014,  "Colombia"), xytext=(2014,  "Colombia"),
             )
#------------------------------------------------------------------------

 # Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Belgium in 2014
plt.scatter(2014, "Belgium", s=bubble_size, c='palegoldenrod', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2014, "Belgium"), xytext=(2014, "Belgium"),
             )

#===================================================================================================================================================#

#The_year_2015

 # Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in USA in 2015
plt.scatter(2015, "USA", s=bubble_size, c='lightblue', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2015, "USA"), xytext=(2015, "USA"),
             )

#------------------------------------------------------------------------

 # Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Tunisia in 2015
plt.scatter(2015, "Tunisia", s=bubble_size, c='lightgreen', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2015, "Tunisia"), xytext=(2015, "Tunisia"),
             )

#------------------------------------------------------------------------

 # Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Singapore in 2015
plt.scatter(2015, "Singapore", s=bubble_size, c='peachpuff', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2015, "Singapore"), xytext=(2015, "Singapore"),
             )

#------------------------------------------------------------------------

 # Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Netherlands in 2015
plt.scatter(2015, "Netherlands", s=bubble_size, c='teal', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2015, "Netherlands"), xytext=(2015, "Netherlands"),
             )
#------------------------------------------------------------------------
             
 # Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Germany in 2015
plt.scatter(2015, "Germany", s=bubble_size, c='peru', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2015, "Germany"), xytext=(2015, "Germany"),
             )

#------------------------------------------------------------------------
 # Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in China in 2015
plt.scatter(2015, "China", s=bubble_size, c='orange', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2015, "China"), xytext=(2015, "China"),
             )

#------------------------------------------------------------------------
 
 # Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Brazil in 2015
plt.scatter(2015, "Brazil", s=bubble_size, c='thistle', edgecolors="black")

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
plt.scatter(2016, "USA", s=bubble_size, c='lightblue', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2016, "USA"), xytext=(2016, "USA"),
             )

#------------------------------------------------------------------------
 
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Philippines in 2016
plt.scatter(2016, "Philippines", s=bubble_size, c='ivory', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2016, "Philippines"), xytext=(2016, "Philippines"),
             )

#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Netherlands in 2016
plt.scatter(2016, "Netherlands", s=bubble_size, c='teal', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2016, "Netherlands"), xytext=(2016, "Netherlands"),
             )

#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Ecuador in 2016
plt.scatter(2016, "Ecuador", s=bubble_size, c='yellowgreen', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2016, "Ecuador"), xytext=(2016, "Ecuador"),
             )


#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in China in 2016
plt.scatter(2016, "China", s=bubble_size, c='orange', edgecolors="black")

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
plt.scatter(2017, "USA", s=bubble_size, c='lightblue', edgecolors="black")

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
plt.scatter(2017, "Philippines", s=bubble_size, c='ivory', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "Philippines"), xytext=(2017, "Philippines"),
             )

#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 3

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed

# Add a specific point for your presence in Netherlands in 2017
plt.scatter(2017, "Netherlands", s=bubble_size, c='teal', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "Netherlands"), xytext=(2017, "Netherlands"),
            )

#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Germany in 2017
plt.scatter(2017, "Germany", s=bubble_size, c='peru', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "Germany"), xytext=(2017, "Germany"),
             )

#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed

# Add a specific point for your presence in Colombia in 2017
plt.scatter(2017, "Colombia", s=bubble_size, c='coral', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "Colombia"), xytext=(2017, "Colombia"),
            )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed

# Add a specific point for your presence in China in 2017
plt.scatter(2017, "China", s=bubble_size, c='orange', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2017, "China"), xytext=(2017, "China")
            )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed

# Add a specific point for your presence in Australia in 2017
plt.scatter(2017, "Australia", s=bubble_size, c='gold', edgecolors="black")

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
plt.scatter(2018, "Austria", s=bubble_size, c='oldlace', edgecolors="black")

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
plt.scatter(2019, "USA", s=bubble_size, c='lightblue', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2019, "USA"), xytext=(2019, "USA"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Philippines in 2019
plt.scatter(2019, "Philippines", s=bubble_size, c='ivory', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2019, "Philippines"), xytext=(2019, "Philippines"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Germany in 2019
plt.scatter(2019, "Germany", s=bubble_size, c='peru', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2019, "Germany"), xytext=(2019, "Germany"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Colombia in 2019
plt.scatter(2019, "Colombia", s=bubble_size, c='coral', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2019, "Colombia"), xytext=(2019, "Colombia"),
             )
#===================================================================================================================================================#

#The_year_2020

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Panama in 2020
plt.scatter(2020, "Panama", s=bubble_size, c='lightpink', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2020, "Panama"), xytext=(2020, "Panama"),
             )

#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Netherlands in 2020
plt.scatter(2020, "Netherlands", s=bubble_size, c='teal', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2020, "Netherlands"), xytext=(2020, "Netherlands"),
             )

#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Germany in 2020
plt.scatter(2020, "Germany", s=bubble_size, c='peru', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2020, "Germany"), xytext=(2020, "Germany"),
             )

#===================================================================================================================================================#

#The_year_2021

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Germany in 2021
plt.scatter(2021, "Germany", s=bubble_size, c='peru', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2021, "Germany"), xytext=(2021, "Germany"),
             )

#===================================================================================================================================================#

#The_year_2022

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Tanzania in 2022
plt.scatter(2022, "Tanzania", s=bubble_size, c='lightyellow', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2022, "Tanzania"), xytext=(2022, "Tanzania"),
             )

#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 3

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Netherlands in 2022
plt.scatter(2022, "Netherlands", s=bubble_size, c='teal', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2022, "Netherlands"), xytext=(2022, "Netherlands"),
             )

#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Germany in 2022
plt.scatter(2022, "Germany", s=bubble_size, c='peru', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2022, "Germany"), xytext=(2022, "Germany"),
             )

#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1


# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Ecuador in 2022
plt.scatter(2022, "Ecuador", s=bubble_size, c='yellowgreen', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2022, "Ecuador"), xytext=(2022, "Ecuador"),
             )
#===================================================================================================================================================#

#The_year_2023

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in USA in 2023
plt.scatter(2023, "USA", s=bubble_size, c='lightblue', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2023, "USA"), xytext=(2023, "USA"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Netherlands in 2023
plt.scatter(2023, "Netherlands", s=bubble_size, c='teal', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2023, "Netherlands"), xytext=(2023, "Netherlands"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 3

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Indonesia in 2023
plt.scatter(2023, "Indonesia", s=bubble_size, c='violet', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2023, "Indonesia"), xytext=(2023, "Indonesia"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 2

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in France in 2023
plt.scatter(2023, "France", s=bubble_size, c='Brown', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2023, "France"), xytext=(2023, "France"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Ecuador in 2023
plt.scatter(2023, "Ecuador", s=bubble_size, c='yellowgreen', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2023, "Ecuador"), xytext=(2023, "Ecuador"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Colombia in 2023
plt.scatter(2023, "Colombia", s=bubble_size, c='coral', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2023, "Colombia"), xytext=(2023, "Colombia"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Belgium in 2023
plt.scatter(2023, "Belgium", s=bubble_size, c='palegoldenrod', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2023, "Belgium"), xytext=(2023, "Belgium"),
             )

#===================================================================================================================================================#

#The_year_2024

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Switzerland in 2024
plt.scatter(2024, "Switzerland", s=bubble_size, c='aqua', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2024, "Switzerland"), xytext=(2024, "Switzerland"),
             )
#------------------------------------------------------------------------

# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Panama in 2024
plt.scatter(2024, "Panama", s=bubble_size, c='lightpink', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2024, "Panama"), xytext=(2024, "Panama"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Ecuador in 2024
plt.scatter(2024, "Ecuador", s=bubble_size, c='yellowgreen', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2024, "Ecuador"), xytext=(2024, "Ecuador"),
             )
#------------------------------------------------------------------------
# Example value to represent in the bubble
value = 1

# Scale the size of the bubble (use a multiplier to make it visually clear)
bubble_size = value * 550  # Adjust the multiplier as needed
# Add a specific point for your presence in Costa Rica in 2024
plt.scatter(2024, "Costa Rica", s=bubble_size, c='gray', edgecolors="black")

# Annotate the point to specify it was a single visit
plt.annotate(str(value), xy=(2024, "Costa Rica"), xytext=(2024, "Costa Rica"),
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