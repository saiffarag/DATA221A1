import pandas as pd

data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

# Create DataFrame
df = pd.DataFrame(data)

# Add computed column
df["D"] = df["A"] + df["B"] + df["C"]

# Print final DataFrame
print(df)