# Import necessary libraries
import json
import pandas as pd
import dataframe_image as dfi

# Read and load JSON data from file
with open("data.json", "r") as outfile: 
    data = json.loads(outfile.read())
    print(type(data))

# Create a dictionary to store the transformed data
solution = dict()

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

# Convert the dictionary to a Pandas DataFrame
data = pd.DataFrame(solution)
print(data)

# Apply a background gradient style to the DataFrame
df_styled = data.style.background_gradient() 

# Export the styled DataFrame to an image file (result.png)
dfi.export(df_styled, "result.png")
