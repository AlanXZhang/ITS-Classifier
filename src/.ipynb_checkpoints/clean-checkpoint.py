import pandas as pd
import numpy as np
import argparse
import os

def clean_csv(path="../data/cases_f.csv"):
    """
    Reads the CSV and return one without missing values and organizations that
    appear less than 10 times
    """
    df = read_csv(path)
    df = drop_na(df)
    df = fill_na(df)
    df = drop_orgs(df)
    return df

def read_csv(path="../data/cases_f.csv", q=True):
    """
    Reads the csv file and return it as a Pandas DataFrame
    
    keyword argument:
    path: String. filepath (absolute or relative path)
    q: Bool. Whether to run this function in quiet mode. If the value is true,
    nothing will be printed. Otherwise, print whether the function was
    successful or not.
    
    return:
    Returns a valid DataFrame if this function is succesful, 
    empty dataframe otherwise
    """
    try:
        df = pd.read_csv(
            path,
            encoding="utf-8",
            encoding_errors="ignore",
            engine="c",
            on_bad_lines="warn",
        )
        print("Successfuly loaded data into a DataFrame")
    except:
        df = None
        print("Read function failed. Please make sure that the filepath \
        is correct.")
    finally:
        return df
    
def drop_na(df):
    """
    Drops any row that is missing the service offering or organization
    
    keyword argument:
    df: a Pandas DataFrame
    
    return: a new DataFrame without these missing values
    """
    return df.dropna(axis=0, subset=["service_offering", "u_organization"])
    
def fill_na(df):
    """
    Replaces the missing values of the DataFrame with an empty string
    
    keyword argument:
    df: a Pandas DataFrame
    """
    return df.fillna("")

def drop_orgs(df):
    """
    Drops organizations that appeared less than 10 times in our data
    
    keyword argument:
    df: a Pandas DataFrame
    """
    val_cts = df.value_counts("u_organization")
    orgs_to_drop = [x for x,ct in val_cts.items() if ct < 10]
    df2 = df[~df["u_organization"].isin(orgs_to_drop)]
    return df2

def org_split(df, output_dir = "../data/"):
    """
    Splits the original data into datasets filtered by the organization
    
    keyword argument:
    df: a Pandas DataFrame
    
    return: None
    Saves the new dataframes in the data folder.
    """
    org_grps = df.groupby("u_organization")
    org_lst = org_grps.groups.keys()
    for org in org_lst:
        filename = f"{org}.csv"
        output_path = os.path.join(output_dir, filename)
        org_grps.get_group(org).to_csv(output_path)
    return 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Processes the raw data for use')
    parser.add_argument("-f", "--filepath", default = "../data/cases_f.csv")
    parser.add_argument("-o", "--output_dir", default="../data/")
    parser.add_argument("-s", "--split_df", action="store_false", default=False)
    args = parser.parse_args()
    filepath = args.filepath
    output_dir = args.output_dir
    split_df = args.split_df
#     print(args.filepath, args.output_dir, args.split_df)
    df = clean_csv(filepath)
    filename = filepath.split("/")[-1].split(".")[0]
    clean_filepath = os.path.join(output_dir, f"{filename}_cleaned.csv")
    df.to_csv(clean_filepath)
    if split_df:
        org_split(df, output_dir)