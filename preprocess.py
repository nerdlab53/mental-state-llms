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


# defining the json template
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
            "Expert Diagnose" : ""
    }
}

def write_json(features, labels, json_template, filename):
  '''
  Takes a dataframe and the JSON template as inputs and generates dataset

  Args : 
  
  features : Pandas DataFrame Object Containing all the features

  labels : Pandas DataFrame Object Containing all the labels

  json_template : A JSON template

  Outputs : 

  Writes to a <name>.json
  '''
  feature_names = list(features.columns)

# iterating over the dataframe and populate the JSON template
  json_output = []
  for row in df.iterrows():
      json_object = json_template.copy()
      for i in feature_names:
        json_object['input'][str(i)] = row[1][str(i)]
      for row in labels.iterrows():
          json_object['output'] = row[1]['Expert Diagnose']
      json_output.append(json_object)


  # writing the JSON output to a file
  with open(f'{filename}.json', 'w') as f:
      json.dump(json_output, f, indent=4)

write_json(features, labels, json_template, filename)