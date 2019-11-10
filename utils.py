import os
import pandas as pd 

def confirm_dir(dir_name='output'):
    dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), dir_name))
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    return dir_path

def export_df(df, output_name):
    data_dir = confirm_dir(dir_name='output')
    export_path = os.path.abspath(os.path.join(data_dir, output_name))
    df.to_csv(export_path, index=False)
