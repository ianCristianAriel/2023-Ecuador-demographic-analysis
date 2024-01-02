import zipfile
import pandas as pd

def decompress_file(file_path, destination):
    """
    Decompresses a zip file at the specified location.

    Args:
        file_path (str): Path to the zip file.
        destination (str): Destination folder for decompression.
    """
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(destination)
        print("Files successfully decompressed to:", destination)
    except Exception as e:
        print(f"Error decompressing the file: {e}")

def load_csv_into_dataframe(file_path):
    """
    Reads a CSV file and loads the data into a DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame with the data from the CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        print('CSV file successfully load in DataFrame.')
        return df
    except:
        print(f"The file does not exist at the specified path: {file_path}")
        return None

def load_dataframe_to_csv(dataframe, destination_path):
    """
    Saves a DataFrame to CSV files at the specified paths.

    Args:
        dataframe (pd.DataFrame): DataFrame to be saved.
        destination_paths (list): List of paths where the CSV files will be saved.
    """
    try:
        dataframe.to_csv(destination_path, index=False)
        print(f"DataFrame successfully saved to: {destination_path}")

    except Exception as e:
        print(f"Error saving the DataFrame: {e}")