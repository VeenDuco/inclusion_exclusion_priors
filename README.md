# Using Inclusion and Exclusion Criteria as Priors

Testing how well it works to use inclusion and exclusion criteria as priors for ASReview. Simulations will be run using Makita. Innitially simulations will be done on the synergy datasets. 

## Data 

The data for the inclusion and exclusion criteria are based upon @ca8cb9e. Two versions are used. The first version in which the raw eligibility criteria are split into inclusion and exclusion criteria. A second version in which these are cleaned up. 

## Preliminary Results

**Comparing raw criteria with a standard 1+1 prior starting point.**

Comparing the two visually. The plot below shows the recall for each synergy dataset and their average recall for both the raw criteria and the 1+1 prior starting point.

![Average recall for both the raw criteria and the 1+1 prior starting point.](output/mean_recall_together_raw_criteria.png)


We can also numerically express this by looking at the loss for each simulation here: [View Loss Raw Table](output/Loss_raw.csv)



**Comparing cleaned criteria with a standard 1+1 prior starting point.**

Comparing the two visually. The plot below shows the recall for each synergy dataset and their average recall for both the cleaned criteria and the 1+1 prior starting point.

![Average recall for both the cleaned criteria and the 1+1 prior starting point.](output/mean_recall_together_cleaned_criteria.png)

We can also numerically express this by looking at the loss for each simulation here: [View Loss Raw Table](output/Loss_cleaned.csv)