import glob
import json
import os

# Base directory to search
base_dir = "simulations/raw_inclusion_exclusion/"

# Patterns to match the files
metrics_without = glob.glob(
    f"{base_dir}*/output/simulation/metrics/metrics_sim_without_priors.json",
    recursive=True,
)

metrics_with = glob.glob(
    f"{base_dir}*/output/simulation/metrics/metrics_sim_with_priors.json",
    recursive=True,
)

# Function to extract 'loss' value and directory info from a file
def extract_loss_with_context(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            
            # Navigate to "data" -> "items" and find the item with "id" == "loss"
            items = data.get("data", {}).get("items", [])
            for item in items:
                if item.get("id") == "loss":
                    # Extract the part of the path for context
                    dir_context = os.path.basename(os.path.normpath(file_path.split("\\")[1]))
                    return {"loss": item.get("value", None), "context": dir_context}

        # Return None if no "loss" found
        return {"loss": None, "context": None}

    except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
        print(f"Error reading {file_path}: {e}")
        return {"loss": None, "context": None}

# Extract 'loss' values with context from all matched files
loss_without_context = [extract_loss_with_context(file) for file in metrics_without]
loss_with_context = [extract_loss_with_context(file) for file in metrics_with]

# Combine the results into a structured format
results = {
    "metrics_without": loss_without_context,
    "metrics_with": loss_with_context,
}

import pandas as pd

print(type(loss_without_context))
# Create a DataFrame for loss_without_context
df_loss_without_context = pd.DataFrame(loss_without_context)

# Create a DataFrame for loss_with_context
df_loss_with_context = pd.DataFrame(loss_with_context)


# Merge the two DataFrames on the 'context' column
df_combined = pd.merge(df_loss_without_context, df_loss_with_context, on='context', suffixes=('_without', '_with'))
df_combined = df_combined[["context", "loss_without", "loss_with"]]
df_combined.rename(columns={
    "context": "study",
    "loss_without": "1+1 prior",
    "loss_with": "In- and exclusion priors"
}, inplace=True)

# Calculate the difference between the two losses
df_combined["difference"] = (df_combined["In- and exclusion priors"] - df_combined["1+1 prior"]).round(3)

# Round all columns to three decimals
df_combined = df_combined.round(3)

# print to csv
df_combined.to_csv("output/Loss_raw.csv", index=False)