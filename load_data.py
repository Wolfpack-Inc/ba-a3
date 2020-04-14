import os
import pandas as pd


def load_dataset(location_filename):
    """
    Returns the txt file as pandas dataframe
    """   
    # Read data from text file
    data = pd.read_csv(location_filename, header=None, sep=' ')

    # Drop extra columns
    data.drop([26,27], axis=1, inplace=True)

    # Define & assign column names
    columns = ['engine_id', 'cycle', 'setting1', 'setting2', 'setting3'] + ['s' + str(i) for i in range(1,22)]

    data.columns = columns

    return data

def load_RUL_predictions(location_filename):
    """
    Returns the RUL predictions as pandas dataframe
    """    
    df = pd.read_csv(location_filename, sep=';')
    
    df.set_index('id', inplace=True)
    
    return df
    
    

