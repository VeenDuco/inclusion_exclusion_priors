

# version 0.10

# Create folder structure. By default, the folder 'output' is used to store output.
mkdir output
mkdir output/simulation
mkdir output/simulation/metrics
mkdir output/figures
mkdir output/tables/metrics
mkdir output/tables/time_to_discovery

mkdir output/simulation/descriptives
python -m asreview data describe generated_data/dataset_with_priors.csv -o output/simulation/descriptives/data_stats_dataset_with_priors.json
python -m asreview data describe generated_data/dataset_without_priors.csv -o output/simulation/descriptives/data_stats_dataset_without_priors.json

python -m asreview simulate generated_data/dataset_with_priors.csv -s output/simulation/state_files/sim_with_priors.asreview --seed 165 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min --prior_idx 4878 4879
python -m asreview metrics output/simulation/state_files/sim_with_priors.asreview -o output/simulation/metrics/metrics_sim_with_priors.json

python -m asreview simulate generated_data/dataset_without_priors.csv -s output/simulation/state_files/sim_without_priors.asreview --init_seed 535 --seed 165 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min
python -m asreview metrics output/simulation/state_files/sim_without_priors.asreview -o output/simulation/metrics/metrics_sim_without_priors.json

# Generate plot and tables for dataset
python scripts/get_plot.py -s output/simulation/state_files/ -o output/figures/plot_recall_sim.png -l filename --hide_random
python scripts/merge_metrics.py -s output/simulation/metrics/ -o output/tables/metrics/metrics_sim.csv
python scripts/merge_tds.py -s output/simulation/metrics/ -o output/tables/time_to_discovery/tds_sim.csv
python scripts/merge_descriptives.py  -s output/simulation/descriptives/