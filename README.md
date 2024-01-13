# JSON to DataFrame Converter

This Python script demonstrates how to read data from a JSON file, convert it to a dictionary, and then transform it into a Pandas DataFrame. The resulting DataFrame is styled and exported as an image.

## Prerequisites

Make sure you have the required libraries installed. You can install them using the following command:

```bash
pip install pandas dataframe_image
```

## Instructions

1. Clone the Repository:
```bash
git clone https://github.com/rkstu/AutomatedVisualization.git
```
2. Navigate to the Project Directory:
```bash
cd AutomatedVisualization
```
3. Run the Script:
```bash
python sample.py
```

This will execute the Python script, reading data from data.json, converting it, and exporting the final results as result.png.

## Code Explanation
#### Step 1: Import Libraries
```
import json
import pandas as pd
import dataframe_image as dfi

```
These lines import the necessary Python libraries for working with JSON data, Pandas, and creating styled DataFrame images.
#### Step 2: Read and Load JSON Data
```
with open("data.json", "r") as outfile: 
    data = json.loads(outfile.read())

```
This section reads data from a JSON file named data.json and loads it into a Python dictionary.
#### Step 3: Transform Data to DataFrame
```
# Iterate through the keys and values in the loaded JSON data
for key, value in data.items():
    # Initialize a nested dictionary for each key in the solution
    solution[key] = dict()
    # Assign a placeholder value to the inner dictionary
    solution[key][key] = '--'
    # Iterate through the keys and values in the nested JSON data
    for key_, value_ in value.items():
        # Assign the 'L' value from the nested JSON to the solution dictionary
        solution[key][key_] = value_['L']

```
This part of the script iterates through the loaded JSON data, transforms it into a dictionary (solution), and then converts it to a Pandas DataFrame (data).
#### Step 4: Style DataFrame and Export
```
df_styled = data.style.background_gradient() 
dfi.export(df_styled, "result.png")


```
