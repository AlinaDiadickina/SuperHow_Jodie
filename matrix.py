import sys
from sklearn.metrics import confusion_matrix


if sys.argv[1]:
    default_pre_dataset = sys.argv[1]
else:
    default_pre_dataset = "./jodie/data/lastfm.csv"
if sys.argv[2]:
    default_post_dataset = sys.argv[2]
else:
    default_post_dataset = "./jodie/data/lastfm_test.csv"

#PREPARE FIRST FILE
f = open(default_pre_dataset, 'r')
Lines = f.readlines()

skip_first_line = 0
pre_data = []
for line in Lines:
    if skip_first_line >= 1:
        string_list = line.replace('\n', '').split(",")
        pre_data.append(string_list)
    skip_first_line += 1
f.close()

pre_data_merged = []
for set in pre_data:
    for unit in set:
        pre_data_merged.append(unit)

#PREPARE SECOND FILE
f = open(default_post_dataset, 'r')
Lines = f.readlines()

skip_first_line = 0
post_data = []
for line in Lines:
    if skip_first_line >= 1:
        string_list = line.replace('\n', '').split(",")
        post_data.append(string_list)
    skip_first_line += 1
f.close()

post_data_merged = []
for set in post_data:
    for unit in set:
        post_data_merged.append(unit)

CM = confusion_matrix(pre_data_merged, post_data_merged)

TN = CM[0][0]
FN = CM[1][0]
TP = CM[1][1]
FP = CM[0][1]

print('TN','FN','TP','FP')
print(TN,FN,TP,FP)





