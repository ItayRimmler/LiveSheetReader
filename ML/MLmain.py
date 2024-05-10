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


def decoder(label):
    if label == 1:
        return 'Do'
    if label == 2:
        return 'Do#'
    if label == 3:
        return 'Re'
    if label == 4:
        return 'Re#'
    if label == 5:
        return 'Mi'
    if label == 6:
        return 'Fa'
    if label == 7:
        return 'Fa#'
    if label == 8:
        return 'Sol'
    if label == 9:
        return 'Sol#'
    if label == 10:
        return 'La'
    if label == 11:
        return 'La#'
    if label == 12:
        return 'Si'
    return 'nothing'

# Creating train data:
train = pd.read_csv("train_data.csv")
recorder = Sound(1.5)
wanna = input("Wanna add data? [Y/N]\n")

if wanna == 'y' or wanna == 'Y':
    times = input("How many recordings will you perform today?\n")
    for i in range(int(times)):
        recorder.record()
        recorder.send_to_cpp("../data/recording.bin")
        output = sp.check_output(["C:/Users/User/PycharmProjects/LiveSheetReader/ver2/src/app/all/main.exe"])
        result = list(map(float, output.strip().split()))
        actual = input("What did you play?\n")
        actual = encoder(actual)
        actual2 = input("And what's that other note you played?\n")
        actual2 = encoder(actual2)
        couple = int(actual2 > 0)
        row = []
        just_freqs = [result[i] for i in range(len(result)) if i%2 == 0]
        recorder.index_2_note(just_freqs)
        for i in range(min(24, int(len(result) * 0.5))):
            row.append(result[2*i])
            row.append(result[2*i+1])
            row.append(encoder(recorder.notes[i]))
        if len(row) < train.shape[1] - 4:
            count = 0
            for i in range(len(row), train.shape[1] - 4):
                row.append(-1)
                count += 1
            row.append(24 - count/3)
        else:
            row.append(24)
        row.append(actual)
        row.append(couple)
        row.append(actual2)
        train.loc[train.shape[0]] = row
        train.to_csv("train_data.csv", index=False)
labels = train.loc[:, ['actual', 'couple', 'actual2']]
train = train.drop(['actual', 'couple', 'actual2'], axis=1)

# Building the model:
model = RandomForestClassifier(n_estimators=c.EP)
model2 = RandomForestClassifier(n_estimators=c.EP)
model3 = RandomForestClassifier(n_estimators=c.EP)

# Fitting the model:
lab1 = labels.loc[:, 'actual']
lab2 = labels.loc[:, 'couple']
lab3 = labels.loc[:, 'actual2']
model.fit(train, lab1)
model2.fit(train, lab2)
model3.fit(train, lab3)

# Printing the train score:
print(f'Train accuracy: {model.score(train, lab1)} , {model.score(train, lab2)} , {model.score(train, lab3)}')

# Creating test data:
test_data = pd.DataFrame(columns=train.columns)
print("Recording again...")
recorder.record()
recorder.send_to_cpp("../data/recording.bin")
output = sp.check_output(["C:/Users/User/PycharmProjects/LiveSheetReader/ver2/src/app/all/main.exe"])
result = list(map(float, output.strip().split()))
actual = input("What did you play?\n")
actual = encoder(actual)
actual2 = input("And what's that other note you played?\n")
actual2 = encoder(actual2)
couple = int(actual2 > 0)
row = []
just_freqs = [result[i] for i in range(len(result)) if i%2 == 0]
recorder.index_2_note(just_freqs)
for i in range(min(24, int(len(result) * 0.5))):
    row.append(result[2*i])
    row.append(result[2*i+1])
    row.append(encoder(recorder.notes[i]))
if len(row) < train.shape[1] - 1:
    count = 0
    for i in range(len(row), train.shape[1] - 1):
        row.append(-1)
        count += 1
    row.append(24 - count/3)
else:
    row.append(24)
# row.append(actual)
# row.append(couple)
# row.append(actual2)
# row.append(temp/row[-2])
test_data.loc[test_data.shape[0]] = row
temp = model.predict(test_data)
temp2 = model2.predict(test_data)
temp3 = model3.predict(test_data)
print(decoder(temp), bool(temp2), decoder(temp3))
