import pandas as pd
# Initialize data
data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

df = pd.DataFrame(data) # Create DataFrame

# Add computed column
df["D"] = df["A"] + df["B"] + df["C"]

# Print final DataFrame
print(df)