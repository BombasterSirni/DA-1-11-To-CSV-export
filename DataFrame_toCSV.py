import numpy as np
import pandas as pd
import os
from sklearn.datasets import make_classification # To create synthetic DataSet
import argparse


def getSynthoDataset(n_samples: int, n_features: int, random_seed: int) -> pd.DataFrame:
    """
    Generate a synthetic dataset using make_classification from sklearn.

    Parameters:
    n_samples (int): Number of samples in the dataset.
    n_features (int): Number of features in the dataset.
    random_seed (int): Random seed for reproducibility.

    Returns:
    pd.DataFrame: Generated synthetic dataset with features and target.
    """
    
    try:
        X, y = make_classification(n_samples=n_samples, n_features=n_features, random_state=random_seed)
        data = pd.DataFrame(X, columns=[i for i in range(1, n_features+1)])
        data['Target'] = y
        return data
    
    except ValueError as err:
        raise ValueError(f"Error generating dataset: {err}")


def exportToCsv(data: pd.DataFrame, export_filename:str, separator: str =",", nan_input: str = '', idxs: bool = False) -> None:
    
    """
    Export the DataFrame to a CSV file.

    Parameters:
    data (pd.DataFrame): The DataFrame to export.
    export_filename (str): Path to the export file.
    separator (str, optional): Separator for CSV. Defaults to ",".
    nan_input (str, optional): Representation for NaN values. Defaults to ''.
    idxs (bool, optional): Whether to include index in CSV. Defaults to False.

    Raises:
    ValueError: If export_filename is not provided.
    IOError: If there's an issue writing to the file.
    """
    
    if(not export_filename):
        raise ValueError("Export filename must be provided")
    
    try:
        data.to_csv(export_filename, sep=separator, na_rep=nan_input, index=idxs)
        print(f"DataFrame was exported to {export_filename}? {os.path.exists(export_filename)}")
    except IOError as err:
        raise IOError(f"Error with exporting to CSV: {err}")
    

# Основная функция 
def main() -> None:
    """
    Main function to parse arguments, generate dataset, and export to CSV.
    """
    parser = argparse.ArgumentParser(description="Generate & export a synthetic dataset to CSV-file")
    
    parser.add_argument("export_filename", type=str, help="Path to the export CSV file in string format.")
    parser.add_argument("n_samples", type=int, help="Number of samples (rows) in the dataset.")
    parser.add_argument("n_features", type=int, help="Number of features (columns) in the dataset.")
    parser.add_argument("random_seed", type=int, help="Random seed for dataset generation.")
    parser.add_argument("--separator", type=str, default=",", help="Separator for CSV (default: ',').")
    parser.add_argument("--nan_input", type=str, default='', help="Symbol to represent NaN values (default: '').")
    parser.add_argument("--include_index", action="store_true", help="Include index in the CSV export.")

    args = parser.parse_args()
    
    # Validation of basic errors
    if(args.n_samples <= 0):
        raise ValueError("n_samples must be positive")
    if(args.n_features <= 0):
        raise ValueError("n_features must be positive")
    if(args.random_seed < 0):
        raise ValueError("random_seed must be non-negative")


    try:
        new_dataset = getSynthoDataset(args.n_samples, args.n_features, args.random_seed)
        exportToCsv(new_dataset, args.export_filename, separator=args.separator,
                      nan_input=args.nan_input, idxs=args.include_index)
        
    except(IOError, ValueError) as err:
        print(f"Got an Error: {err}")
        return 0
    
    
main()