import json
import pandas as pd

# load json-file into a list
with open("./data/essay_corpus.json") as f:
    essays = json.load(f)

# convert csv-file into a DataFrame
split_info = pd.read_csv("./data/train-test-split.csv", ';')

# split essays into train_essays and test_essays the both lists
train_essays = []
test_essays = []
for i in range(len(essays)):
    essay_num = essays[i]['id']
    if(split_info['SET'][essay_num-1]=="TRAIN"):
        train_essays.append(essays[i])
    else:
        test_essays.append(essays[i])

# write train_essays into json file
json_train_essays = json.dumps(train_essays, indent=4)
with open("./data/train_essays.json", 'w') as f:
    f.write(json_train_essays)


# write test_essays into json file
json_test_essays = json.dumps(test_essays, indent=4)
with open("./data/test_essays.json", 'w') as f:
    f.write(json_test_essays)