import json
import tqdm
import re

splits = {'train': 'train', 'validation': 'validation', 'test': 'test'}
dataset_type = 'test'

# set the response JSON file name
model_name = "Llama-3.1-8B-Instruct"
prompt_type = "CoT"
file_name = f'{prompt_type}response_{splits[dataset_type]}'

# record the number of correctly labelled tags or how they are wrongly labelled
tags_count = {
    "0": [0, 0, 0, 0],
    "1": [0, 0, 0, 0],
    "2": [0, 0, 0, 0],
    "3": [0, 0, 0, 0]
}

labels_to_ids = {
    "O": "0",
    "PER_B": "1",
    "PER_I": "2",
    "LOC_B": "3",
    "LOC_I": "4",
    "ORG_B": "5",
    "ORG_I": "6"
}

with open(f'./{model_name}/'+file_name+'.json', 'r') as jsonfile:
    dataset_json = json.load(jsonfile)

sentences = dataset_json['sentences']
tags = dataset_json['tags']
answer_tags = dataset_json['answer_tags']

# count the number of correct tags and mislabeled tags
i = 0
while i < len(answer_tags):
    tag = tags[i]
    ans_tag = answer_tags[i]["tags"]

    # we do not consider whether the word is the beginning of the entity or not 
    for ind in range(len(ans_tag)):
        if tag[ind] == "1" or tag[ind] == "2":
            tag[ind] = "1"
        elif tag[ind] == "3" or tag[ind] == "4":
            tag[ind] = "2"
        elif tag[ind] == "5" or tag[ind] == "6":
            tag[ind] = "3"

        if ans_tag[ind] == "1" or ans_tag[ind] == "2":
            ans_tag[ind] = "1"
        elif ans_tag[ind] == "3" or ans_tag[ind] == "4":
            ans_tag[ind] = "2"
        elif ans_tag[ind] == "5" or ans_tag[ind] == "6":
            ans_tag[ind] = "3"

        label = tag[ind]
        ans = ans_tag[ind]

        tags_count[label][int(ans)] = tags_count[label][int(ans)] + 1

    i += 1

# calculate entity level presion, recall, and F1 score

o_precision = tags_count["0"][0] / (tags_count["0"][0] +
                                    tags_count["1"][0] + tags_count["2"][0] + tags_count["3"][0])
o_recall = tags_count["0"][0] / (tags_count["0"][0] +
                                 tags_count["0"][1] + tags_count["0"][2] + tags_count["0"][3])
o_F1 = 2*o_precision*o_recall/(o_precision+o_recall)

per_precision = tags_count["1"][1] / (tags_count["0"][1] +
                                      tags_count["1"][1] + tags_count["2"][1] + tags_count["3"][1])
per_recall = tags_count["1"][1] / (tags_count["1"][0] +
                                   tags_count["1"][1] + tags_count["1"][2] + tags_count["1"][3])
per_F1 = 2*per_precision*per_recall/(per_precision + per_recall)

loc_precision = tags_count["2"][2] / (tags_count["0"][2] +
                                      tags_count["1"][2] + tags_count["2"][2] + tags_count["3"][2])
loc_recall = tags_count["2"][2] / (tags_count["2"][0] +
                                   tags_count["2"][1] + tags_count["2"][2] + tags_count["2"][3])
loc_F1 = 2*loc_precision*loc_recall/(loc_precision+loc_recall)

org_precision = tags_count["3"][3] / (tags_count["0"][3] +
                                      tags_count["1"][3] + tags_count["2"][3] + tags_count["3"][3])
org_recall = tags_count["3"][3] / (tags_count["3"][0] +
                                   tags_count["3"][1] + tags_count["3"][2] + tags_count["3"][3])
org_F1 = 2*org_precision*org_recall/(org_precision+org_recall)

print(f'{model_name}, {prompt_type}')
print(f'Person F1 score:        {per_F1}')
print(f'Location F1 score:      {loc_F1}')
print(f'Organization F1 score:  {org_F1}')
print(f'Wieghted F1 score:      {(per_F1*sum(tags_count["1"]) + loc_F1*sum(tags_count["2"]) + org_F1*sum(tags_count["3"])) / (sum(tags_count["1"]) + sum(tags_count["2"]) + sum(tags_count["3"]))}')

