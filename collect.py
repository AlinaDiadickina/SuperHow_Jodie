import os
from os import walk

# JODIE
jodieFiles = []
jodieData = {}
for root, dirs, files in os.walk("./git/jodie/data_results/"):
    for filename in files:
        jodieFiles.append(filename)

for fileName in jodieFiles:
    f = open("./git/jodie/data_results/" + fileName, "r")
    jodieData[fileName] = f.read()

# DGCF
dgcfFiles = []
dgcfData = {}
for root, dirs, files in os.walk("./git/DGCF/data_results/"):
    for filename in files:
        dgcfFiles.append(filename)

for fileName in dgcfFiles:
    f = open("./git/DGCF/data_results/" + fileName, "r")
    dgcfData[fileName] = f.read()

# TIGECMN
tigeFiles = []
tigeData = {}
for root, dirs, files in os.walk("./git/TigeCMN/data_results/"):
    for filename in files:
        tigeFiles.append(filename)

for fileName in tigeFiles:
    f = open("./git/TigeCMN/data_results/" + fileName, "r")
    tigeData[fileName] = f.read()

# DEEPRED
deepredFiles = []
deepredData = {}
for root, dirs, files in os.walk("./git/deepred_v2/deepred/data_results/"):
    for filename in files:
        deepredFiles.append(filename)

for fileName in deepredFiles:
    f = open("./git/deepred_v2/deepred/data_results/" + fileName, "r")
    deepredData[fileName] = f.read()

# PRINT DATA
print("JODIE")
for jodie in jodieData:
    print(jodie)
    print(jodieData[jodie])
print('------------------------------')

print("DGCF")
for dgcf in dgcfData:
    print(dgcf)
    print(dgcfData[dgcf])
print('------------------------------')

print("TigeCMN")
for tige in tigeData:
    print(tige)
    print(tigeData[tige])
print('------------------------------')

print("DeepRed")
for red in deepredData:
    print(red)
    print(deepredData[red])