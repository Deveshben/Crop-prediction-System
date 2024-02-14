import pandas as pd

# Load the new data for prediction
new_data = pd.read_csv('datafile (2).csv', index_col=0)

# Convert all values to numeric (errors='coerce' will convert non-numeric values to NaN)
new_data = new_data.apply(pd.to_numeric, errors='coerce')

# Drop rows with NaN values (non-numeric)
new_data.dropna(inplace=True)

# Select only the relevant features used during training
new_data = new_data[X.columns]

# Make predictions using the trained model
predictions = model.predict(new_data)

# Print the predictions
print("Predicted crop production:")
for crop, prediction in zip(new_data.index, predictions):
    print(f"{crop}: {prediction}")
