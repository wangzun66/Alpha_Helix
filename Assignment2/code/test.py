from itertools import chain
import pandas as pd
import numpy as np

essay = []  # store all token_tuples of a essay
essay_list = []  # store all essays
counter = 0;
with open("./data/train_essays_BIO.txt", 'r') as f:  # later
    for line in f.readlines():
        token = line.split('\t')
        if (len(token) == 1):
            essay_list.append(essay)
            essay = []
        else:
            token_tuple = (token[0].strip(), token[1].strip())
            essay.append(token_tuple)

# 2 dimensional list: 1.dim: essay,  2.dim: tokens of corresponding essay
essay_tokens_list = []

# 2 dimensional list: 1.dim: essay, 2.dim: annotations of corresponding essay
essay_anns_list = []

for i in range(len(essay_list)):
    array = np.asarray(essay_list[i])
    essay_tokens_list.append(array[:, 0])
    essay_anns_list.append(array[:, 1])

'''
Build 4 dictionaries
1. token2id: index is token, through index get token_id
2. id2token: index is token_id, through index get token
3. ann2id: index is annotation, through index get ann_id
4. id2ann: index is ann_id, through index get annotation
'''
# extract the set of tokens
tokens = list(chain(*essay_tokens_list))
tokens_series = pd.Series(tokens)
tokens_set = tokens_series.drop_duplicates().tolist()
tokens_set.insert(0, "NONE")
token_ids = range(0, len(tokens_set))

# build token dicts
token2id = pd.Series(token_ids, tokens_set)
id2token = pd.Series(tokens_set, token_ids)

# extract the set of annotations
anns_series = pd.Series(essay_anns_list[0])
ann_set = anns_series.drop_duplicates().tolist()
ann_id = range(0, 7)

# build annotation dicts
ann2id = pd.Series(ann_id, ann_set)
id2ann = pd.Series(ann_set, ann_id)

'''
essay vector embedding
1. get the maximum length of essays, define it as vector length
2. each entry of vector is token_id
3. token size of essay is less than vector length, pad 0, namely token_id of "NONE"
'''
# get vector length
max_length_of_vector = 0
for i in range(len(essay_tokens_list)):
    if max_length_of_vector < len(essay_tokens_list[i]):
        max_length_of_vector = len(essay_tokens_list[i])


# input vector x embedding
def x_embedding(tokens: list) -> list:
    x = list(token2id[tokens])
    x.extend([0] * (max_length_of_vector - len(x)))
    return x

# output vector y embedding
def y_embedding(anns: list) -> list:
    y = list(ann2id[anns])
    y.extend([0] * (max_length_of_vector - len(y)))
    return y


data_x = []
for i in range(len(essay_tokens_list)):
    data_x.append(x_embedding(essay_tokens_list[i]))

data_y = []
for i in range(len(essay_anns_list)):
    data_y.append(y_embedding(essay_anns_list[i]))

data_x = np.asarray(data_x)
data_y = np.asarray(data_y)
