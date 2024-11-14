

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

python -m asreview simulate generated_data/dataset_with_priors.csv -s output/simulation/state_files/sim_with_priors_0.asreview --seed 165 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min --prior_idx 2873 2874
python -m asreview metrics output/simulation/state_files/sim_with_priors_0.asreview -o output/simulation/metrics/metrics_sim_with_priors_0.json

python -m asreview simulate generated_data/dataset_without_priors.csv -s output/simulation/state_files/sim_without_priors_0.asreview --init_seed 535 --seed 165 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min
python -m asreview metrics output/simulation/state_files/sim_without_priors_0.asreview -o output/simulation/metrics/metrics_sim_without_priors_0.json

python -m asreview simulate generated_data/dataset_with_priors.csv -s output/simulation/state_files/sim_with_priors_1.asreview --seed 166 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min --prior_idx 2873 2874
python -m asreview metrics output/simulation/state_files/sim_with_priors_1.asreview -o output/simulation/metrics/metrics_sim_with_priors_1.json

python -m asreview simulate generated_data/dataset_without_priors.csv -s output/simulation/state_files/sim_without_priors_1.asreview --init_seed 536 --seed 166 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min
python -m asreview metrics output/simulation/state_files/sim_without_priors_1.asreview -o output/simulation/metrics/metrics_sim_without_priors_1.json

python -m asreview simulate generated_data/dataset_with_priors.csv -s output/simulation/state_files/sim_with_priors_2.asreview --seed 167 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min --prior_idx 2873 2874
python -m asreview metrics output/simulation/state_files/sim_with_priors_2.asreview -o output/simulation/metrics/metrics_sim_with_priors_2.json

python -m asreview simulate generated_data/dataset_without_priors.csv -s output/simulation/state_files/sim_without_priors_2.asreview --init_seed 537 --seed 167 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min
python -m asreview metrics output/simulation/state_files/sim_without_priors_2.asreview -o output/simulation/metrics/metrics_sim_without_priors_2.json

python -m asreview simulate generated_data/dataset_with_priors.csv -s output/simulation/state_files/sim_with_priors_3.asreview --seed 168 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min --prior_idx 2873 2874
python -m asreview metrics output/simulation/state_files/sim_with_priors_3.asreview -o output/simulation/metrics/metrics_sim_with_priors_3.json

python -m asreview simulate generated_data/dataset_without_priors.csv -s output/simulation/state_files/sim_without_priors_3.asreview --init_seed 538 --seed 168 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min
python -m asreview metrics output/simulation/state_files/sim_without_priors_3.asreview -o output/simulation/metrics/metrics_sim_without_priors_3.json

python -m asreview simulate generated_data/dataset_with_priors.csv -s output/simulation/state_files/sim_with_priors_4.asreview --seed 169 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min --prior_idx 2873 2874
python -m asreview metrics output/simulation/state_files/sim_with_priors_4.asreview -o output/simulation/metrics/metrics_sim_with_priors_4.json

python -m asreview simulate generated_data/dataset_without_priors.csv -s output/simulation/state_files/sim_without_priors_4.asreview --init_seed 539 --seed 169 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min
python -m asreview metrics output/simulation/state_files/sim_without_priors_4.asreview -o output/simulation/metrics/metrics_sim_without_priors_4.json

python -m asreview simulate generated_data/dataset_with_priors.csv -s output/simulation/state_files/sim_with_priors_5.asreview --seed 170 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min --prior_idx 2873 2874
python -m asreview metrics output/simulation/state_files/sim_with_priors_5.asreview -o output/simulation/metrics/metrics_sim_with_priors_5.json

python -m asreview simulate generated_data/dataset_without_priors.csv -s output/simulation/state_files/sim_without_priors_5.asreview --init_seed 540 --seed 170 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min
python -m asreview metrics output/simulation/state_files/sim_without_priors_5.asreview -o output/simulation/metrics/metrics_sim_without_priors_5.json

python -m asreview simulate generated_data/dataset_with_priors.csv -s output/simulation/state_files/sim_with_priors_6.asreview --seed 171 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min --prior_idx 2873 2874
python -m asreview metrics output/simulation/state_files/sim_with_priors_6.asreview -o output/simulation/metrics/metrics_sim_with_priors_6.json

python -m asreview simulate generated_data/dataset_without_priors.csv -s output/simulation/state_files/sim_without_priors_6.asreview --init_seed 541 --seed 171 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min
python -m asreview metrics output/simulation/state_files/sim_without_priors_6.asreview -o output/simulation/metrics/metrics_sim_without_priors_6.json

python -m asreview simulate generated_data/dataset_with_priors.csv -s output/simulation/state_files/sim_with_priors_7.asreview --seed 172 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min --prior_idx 2873 2874
python -m asreview metrics output/simulation/state_files/sim_with_priors_7.asreview -o output/simulation/metrics/metrics_sim_with_priors_7.json

python -m asreview simulate generated_data/dataset_without_priors.csv -s output/simulation/state_files/sim_without_priors_7.asreview --init_seed 542 --seed 172 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min
python -m asreview metrics output/simulation/state_files/sim_without_priors_7.asreview -o output/simulation/metrics/metrics_sim_without_priors_7.json

python -m asreview simulate generated_data/dataset_with_priors.csv -s output/simulation/state_files/sim_with_priors_8.asreview --seed 173 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min --prior_idx 2873 2874
python -m asreview metrics output/simulation/state_files/sim_with_priors_8.asreview -o output/simulation/metrics/metrics_sim_with_priors_8.json

python -m asreview simulate generated_data/dataset_without_priors.csv -s output/simulation/state_files/sim_without_priors_8.asreview --init_seed 543 --seed 173 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min
python -m asreview metrics output/simulation/state_files/sim_without_priors_8.asreview -o output/simulation/metrics/metrics_sim_without_priors_8.json

python -m asreview simulate generated_data/dataset_with_priors.csv -s output/simulation/state_files/sim_with_priors_9.asreview --seed 174 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min --prior_idx 2873 2874
python -m asreview metrics output/simulation/state_files/sim_with_priors_9.asreview -o output/simulation/metrics/metrics_sim_with_priors_9.json

python -m asreview simulate generated_data/dataset_without_priors.csv -s output/simulation/state_files/sim_without_priors_9.asreview --init_seed 544 --seed 174 -m nb -e tfidf -q max -b double --n_instances 1 --stop_if min
python -m asreview metrics output/simulation/state_files/sim_without_priors_9.asreview -o output/simulation/metrics/metrics_sim_without_priors_9.json

# Generate plot and tables for dataset
python scripts/get_plot.py -s output/simulation/state_files/ -o output/figures/plot_recall_sim.png -l filename --hide_random
python scripts/merge_metrics.py -s output/simulation/metrics/ -o output/tables/metrics/metrics_sim.csv
python scripts/merge_tds.py -s output/simulation/metrics/ -o output/tables/time_to_discovery/tds_sim.csv
python scripts/merge_descriptives.py  -s output/simulation/descriptives/