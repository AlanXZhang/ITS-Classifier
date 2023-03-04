# A classification model intended to predict the service offering of a ServiceNow support ticket based on the description provided.

# Usage
1. Please create a folder named data and download the raw data file there
2. From there, open a terminal of your choice and run clean.py <br>
You have a few options here. "clean.py filepath output_dir split_df"
- filepath is a string that leads to the data file
- output_dir specifies where you want to store the cleaned data
- split_df specifies whether you want to split the data by the organization it falls under
    - split_df will generate new csvs files in the output_dir specified
The output of this function will generate a new csv named "(old_csv)_cleaned.csv"