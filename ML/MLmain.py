# Starting with importing the General functions and the libraries
from ver2.src.lib.all import g
from ver2.src.lib.all import constants as c

# Imports specific to this script:
import pandas as pd
import subprocess as sp
from sklearn.ensemble import RandomForestClassifier
# Audio Process imports:
from ver2.src.lib.audio_process.audio_process import process_tempo
from ver2.src.lib.audio_process.Sound import Sound

def encoder(label):
    if label == 'Do':
        return 1
    if label == 'Do#':
        return 2
    if label == 'Re':
        return 3
    if label == 'Re#':
        return 4
    if label == 'Mi':
        return 5
    if label == 'Fa':
        return 6
    if label == 'Fa#':
        return 7
    if label == 'Sol':
        return 8
    if label == 'Sol#':
        return 9
    if label == 'La':
        return 10
    if label == 'La#':
        return 11
    if label == 'Si':
        return 12
    return 0

# Creating train data:
train = pd.read_csv("train_data.csv")
times = input("How many recordings will you perform today?\n")
recorder = Sound(1.5)

for i in range(int(times)):
    recorder.record()
    recorder.send_to_cpp("../data/recording.bin")
    output = sp.check_output(["C:/Users/User/PycharmProjects/LiveSheetReader/ver2/src/app/all/main.exe"])
    result = list(map(float, output.strip().split()))
    actual = input("What did you play?\n")
    actual = encoder(actual)
    temp = 0
    flag = True
    row = []
    just_freqs = [result[i] for i in range(len(result)) if i%2 == 0]
    recorder.index_2_note(just_freqs)
    for i in range(min(24, int(len(result) * 0.5))):
        row.append(result[2*i])
        row.append(result[2*i+1])
        row.append(encoder(recorder.notes[i]))
        if flag:
            if actual == encoder(recorder.notes[i]):
                flag = False
                temp = 1
    if len(row) < train.shape[1] - 3:
        count = 0
        for i in range(len(row), train.shape[1] - 3):
            row.append(-1)
            count += 1
        row.append(24 - count/3)
    else:
        row.append(24)
    row.append(actual)
    row.append(temp/row[-2])
    train.loc[train.shape[0]] = row
    train.to_csv("train_data.csv", index=False)
labels = train.loc[:, 'actual']
train = train.drop(['score', 'actual'], axis=1)

# Building the model:
model = RandomForestClassifier(n_estimators=c.EP)

# Fitting the model:
model.fit(train, labels)

# Printing the train score:
print(f'Train accuracy: {model.score(train, labels)}')

# Creating test data:
test_data = pd.DataFrame(columns=train.columns)
print("Recording again...")
recorder.record()
recorder.send_to_cpp("../data/recording.bin")
output = sp.check_output(["C:/Users/User/PycharmProjects/LiveSheetReader/ver2/src/app/all/main.exe"])
result = list(map(float, output.strip().split()))
actual = input("What did you play?\n")
actual = encoder(actual)
temp = 0
flag = True
row = []
just_freqs = [result[i] for i in range(len(result)) if i%2 == 0]
recorder.index_2_note(just_freqs)
for i in range(min(24, int(len(result) * 0.5))):
    row.append(result[2*i])
    row.append(result[2*i+1])
    row.append(encoder(recorder.notes[i]))
    if flag:
        if actual == encoder(recorder.notes[i]):
            flag = False
            temp = 1
if len(row) < train.shape[1] - 3:
    count = 0
    for i in range(len(row), train.shape[1] - 3):
        row.append(-1)
        count += 1
    row.append(24 - count/3)
else:
    row.append(24)
# row.append(actual)
# row.append(temp/row[-2])
test_data.loc[test_data.shape[0]] = row
temp = model.predict(test_data)
print(temp)
print(temp == actual)
