import opendatasets as od
import pandas as pd
import json
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-fn", "--filename", help='name of the output json file')

args = parser.parse_args()

filename = args.filename

# username : himanshubhenwal key : c729846b22a3daccd9c055a05a5dc263

od.download('https://www.kaggle.com/datasets/cid007/mental-disorder-classification')

df = pd.read_csv('./mental-disorder-classification/Dataset-Mental-Disorders.csv')

df.rename(columns = {'Sleep dissorder': 'Sleep Disorder', 'Anorxia' : 'Anorexia', 'Optimisim' : 'Optimism'}, inplace=True)

# separating features and labels
labels = df[['Expert Diagnose']]
features = df[['Sadness', 'Euphoric', 'Sleep Disorder', 'Suicidal thoughts', 'Anorexia', 'Aggressive Response', 'Ignore & Move-On', 'Nervous Break-down', 'Admit Mistakes', 'Overthinking', 'Sexual Activity', 'Concentration', 'Optimism']]


# definig the json template
json_template = {
    
        "instruction": "Given below is the values of certain features which are essential to predict the emotional state of a person. Read the feature values and try to predict the emotional status of the person.",
        "input": {
            "Sadness" : "",
            "Euphoric" : "",
            "Sleep Disorder": "",
            "Suicidal thoughts": "",
            "Anorexia" : "",
            "Aggressive Response" : "",
            "Ignore & Move-On": "",
            "Nervous Break-down": "",
            "Admit Mistakes": "",
            "Overthinking": "",
            "Sexual Activity": "",
            "Concentration": "",
            "Optimism": "",
        },
        "output": {
    }
}

import json
import copy

def populate_json_template(df, json_template):
    '''
    Takes the dataframe as input and outputs the final JSON data

    Args : 
    df : Pandas DataFrame Containing all the values
    json_template : JSON template for data

    Output :
    Outputs the JSON data generated
    '''
    final_data = []
    for _, row in df.iterrows():
        current_data = copy.deepcopy(json_template)  # Create a deep copy of the template
        for key in json_template['input']:
            if key != 'Expert Diagnose':
                current_data['input'][key] = str(row[key]) 
        current_data['output']['Expert\'s Diagnosis'] = str(row['Expert Diagnose'])
        final_data.append(current_data)
    return final_data

# Example usage
populated_data = populate_json_template(df, json_template)
with open(f'{filename}.json', 'w') as f:
    json.dump(populated_data, f, indent=4)