#!/usr/bin/env python

import bertCode
import json
import argparse
import csv

dummy_data = [
    """received from: efgrossm@eng.ucsd.edu Hi UCSD service desk,I am trying to access MyStudentChart, 
    but my phone broke yesterday. I cannot use DuoMobile to confirm login from my computer. 
    Can I get a bypass code while I wait for my new phone to come? -Esther
    """,
    """received from: rsotelo@ucsd.edu

    Hi Service desk,

    Can you please help me register my era commons username RYSOTELO and USCD affiliation to DUO.

    Thank you,

    Raquel
    """,
    "My account is compromised, I need to change my password",
    "Wifi at Sixth college is not working. All of my friends are reporting a problem",
    "My VPN is not working. It is stuck on trying to connect when I type in my password",
    "I am not receiving any emails in my Outlook exchange. The last email I got was 2 months ago. HELP!!!",
    "I just registered for Math 189 yesterday and it is not showing up as a course on my Canvas page. Please help",
    "My docking station is broken, the monitors connected to it does not work",
    "My health email is not receiving any emails, what is going on?",
    "I need Adobe Acrobat for work, how can I get that on my account?"
]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Predict the service offering based on the provided target description')
    parser.add_argument("-t", "--target")
    args = parser.parse_args()
    target_filepath = args.target
    
    if target_filepath is None:
        target = dummy_data
    else:
        with open(target_filepath, 'r') as f:
            target = f.readlines()
    
    with open('config.json', 'r') as config:
        params = json.load(config)

    labels, probs = bertCode.run_process(descriptions = target, param_dict=params)
    
    with open('../outputs/results.csv', 'w') as res:
        header = ['Predicted Service Offering', 'Probability']
        writer = csv.writer(res)
        writer.writerow(header)
        
        for label, prob in zip(labels, probs):
            print(label, prob)
            row = [label, prob]
            writer.writerow(row)