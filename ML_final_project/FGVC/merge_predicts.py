import csv
import pandas as pd
def read_csv_to_dict(file_path):
    result_dict = {}
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            key = row.pop('id')
            result_dict[key] = row
    return result_dict

file_path1 = 'submission_model.csv'
data_dict1 = read_csv_to_dict(file_path1)

file_path2 = 'submission_normal.csv'
data_dict2 = read_csv_to_dict(file_path2)

file_path3 = 'submission_amp.csv'
data_dict3 = read_csv_to_dict(file_path3)

result = []
for entry in data_dict1:
    print(data_dict1[entry])
    if (float(data_dict2[entry]['win2'])+0.5 > float(data_dict1[entry]['win2'])):
        data_dict1[entry]['label'] = data_dict2[entry]['label']
        data_dict1[entry]['win2'] = float(data_dict2[entry]['win2'])+0.5
    if (float(data_dict3[entry]['win2']) > float(data_dict1[entry]['win2'])):
        data_dict1[entry]['label'] = data_dict3[entry]['label']
        data_dict1[entry]['win2'] = data_dict3[entry]['win2']
    tempdict = {}
    tempdict['label'] = data_dict1[entry]['label']
    tempdict['id'] = entry
    result.append(tempdict)


fieldnames = ['id', 'label']
csv_file = "submission.csv"
# Open the CSV file in write mode
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    # Write the header using the keys of the first dictionary
    writer.writeheader()

    # Write the data from the list of dictionaries to the CSV file
    writer.writerows(result)
