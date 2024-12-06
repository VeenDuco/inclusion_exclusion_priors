import numpy as np
import matplotlib.pyplot as plt
import glob
from utils.average_recall import plot_average_recall
from utils.average_recall import plot_average_recall_two_groups
# Base directory to search
base_dir = "simulations/raw_inclusion_exclusion/"

# Pattern to match the files in the specific directory structure
state_files_without = glob.glob(
    f"{base_dir}*/output/simulation/state_files/sim_without_priors*.asreview",
    recursive=True,
)

state_files_with = glob.glob(
    f"{base_dir}*/output/simulation/state_files/sim_with_priors*.asreview",
    recursive=True,
)

# Plot the average recall curve
fig, ax = plt.subplots(figsize=(8, 6))

plot_average_recall(
    ax,
    state_files_with,
    priors=False,         # Include prior labels if needed
    show_ci=True,         # Display confidence intervals
    ci_alpha=0.2,         # Transparency for CI shading
    show_random=True,     # Include random recall curve
    show_optimal=False,    # Include optimal recall curve
    legend_label="Mean Recall with raw inclusion and exlusion priors",
    line_color="blue",    # Color for the mean recall curve
)

plt.tight_layout()
plt.savefig("output/mean_recall_in_exclusion_raw_criteria.png") 

# Plot the average recall curve
fig, ax = plt.subplots(figsize=(8, 6))

plot_average_recall(
    ax,
    state_files_without,
    priors=False,         # Include prior labels if needed
    show_ci=True,         # Display confidence intervals
    ci_alpha=0.2,         # Transparency for CI shading
    show_random=True,     # Include random recall curve
    show_optimal=False,    # Include optimal recall curve
    legend_label="Mean Recall with 1+1 priors",
    line_color="blue",    # Color for the mean recall curve
)

plt.tight_layout()
plt.savefig("output/mean_recall_1plus1_raw_criteria.png") 

# Plot the average recall curves for the two groups
fig, ax = plt.subplots(figsize=(10, 6))

plot_average_recall_two_groups(
    ax,
    state_files_with,
    state_files_without,
    priors=False,
    show_ci=True,
    ci_alpha=0.2,
    show_random=True,
    show_optimal=False,
    legend_labels=("Mean Recall with raw inclusion and exlusion priors", 
    "Mean Recall with 1+1 priors"),
    colors=("blue", "red"),
)

plt.tight_layout()
plt.savefig("output/mean_recall_together_raw_criteria.png") 
