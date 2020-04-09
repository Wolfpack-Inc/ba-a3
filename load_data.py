import os
import pandas as pd


def load_dataset(filename, folder='data'):
    """
    Returns the txt file as pandas dataframe
    """
    
    path = os.path.join(os.getcwd(), folder, filename)
    
    # Read data from text file
    data = pd.read_csv(path, sep=" ", header=None)

    # Drop extra columns
    data.drop([26,27], axis=1, inplace=True)

    # Define & assign column names
    columns = ['engine_id', 'cycle', 'setting1', 'setting2', 'setting3'] + ['s' + str(i) for i in range(1,22)]

    data.columns = columns

    # Set index
    data.set_index(['engine_id', 'cycle'], inplace=True)
    
    return data