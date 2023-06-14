# A classification model that predicts the service offering of ServiceNow support ticket(s) based on the description provided.

# Running the pre-trained model
1. Open a terminal from the main folder and type 'cd src'
2. Type in 'python run.py' to launch the model and predict the service offering along with their predicted probability
3. Compare the results generated in your terminal or the 'results.csv' in the main_dir/outputs folder with the 'sample_results.csv'
4. Run 'python run.py <filepath to your description .txt>'

Note: If you want to run the model on a list of description, store them as a file and each description should be on a new line <br>
E.g. <br>
My account is compromised, I need to change my password <br>
Wifi at Sixth college is not working. All of my friends are reporting a problem <br>
...<br>
My VPN is not working. It is stuck on trying to connect when I type in my password<br>


# To clean the raw data
1. Create a folder named data and download the raw data file there
2. From there, open a terminal of your choice and run clean.py <br>
You have a few options here. "clean.py filepath output_dir split_df"
- filepath is a string that leads to the data file
- output_dir specifies where you want to store the cleaned data
- split_df specifies whether you want to split the data by the organization it falls under
    - split_df will generate new csvs files in the output_dir specified
The output of this function will generate a new csv named "(old_csv)_cleaned.csv"
