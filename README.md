# **Synthetic Dataset Generator**
This script generates a synthetic classification dataset using scikit-learn's make_classification and exports it to a CSV file.

## Requirements
- Python 3.x
- Install dependencies via: pip install -r requirements.txt

## Usage
- Run the script from the command line with the required arguments.

## Command-Line Arguments:
- export_filename: Path to the output CSV file (required, str).
- n_samples: Number of samples (rows) in the dataset (required, int, must be > 0).
- n_features: Number of features (columns) in the dataset (required, int, must be > 0).
- random_seed: Random seed for reproducibility (required, int, must be >= 0).
- --separator: CSV separator (optional, str, default: ',').
- --nan_input: Symbol for NaN values (optional, str, default: '').
- --include_index: Flag to include index in CSV (optional, no value needed).

## Example:
```bash
python DataFrame_toCSV.py output.csv 1000 20 42 --separator ";" --nan_input "NaN" --include_index
```