import opendatasets as od
import pandas as pd
import json

# username : himanshubhenwal key : c729846b22a3daccd9c055a05a5dc263

od.download('https://www.kaggle.com/datasets/cid007/mental-disorder-classification')

df = pd.read_csv('./mental-disorder-classification/Dataset-Mental-Disorders.csv')

# separating features and labels
labels = df[['Expert Diagnose']]
features = df[['Sadness', 'Euphoric', 'Sleep dissorder', 'Suicidal thoughts', 'Anorxia', 'Aggressive Response', 'Ignore & Move-On', 'Nervous Break-down', 'Admit Mistakes', 'Overthinking', 'Sexual Activity', 'Concentration', 'Optimisim']]

# renaming some badly spelt names in the dataset
features.rename(columns = {'Sleep dissorder': 'Sleep Disorder', 'Anorxia' : 'Anorexia', 'Optimisim' : 'Optimism'}, inplace=True)


# definig the json template
json_template = {
    
        "instruction": "Given below is the values of certain features which are essential to predict the emotional state of a person. Read the feature values and try to predict the emotional status of the person.",
        "input": {
            "Sadness" : "",
            "Euphoric" : "",
            "Sleep Disorder": "",
            "Suicidal thoughts": "",
            "Anorexia" : "",
            "Aggresive Response" : "",
            "Ignore & Move-On": "",
            "Nervous Breakdown": "",
            "Admit Mistakes": "",
            "Overthinking": "",
            "Sexual Activity": "",
            "Concentration": "",
            "Optimism": "",
        },
        "output": {
            "Expert Diagnose" : ""
    }
}

feature_names = list(features.columns)

# iterating over the dataframe and populate the JSON template
json_output = []
for row in features.iterrows():
    json_object = json_template.copy()
    for i in feature_names:
      json_object['input'][str(i)] = row[1][str(i)]
for row in labels.iterrows():
    json_object['output'] = row[1]['Expert Diagnose']
    json_output.append(json_object)


# writing the JSON output to a file
with open('output_final.json', 'w') as f:
    json.dump(json_output, f)