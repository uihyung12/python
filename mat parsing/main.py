from scipy import io
import numpy as np

matTrain = io.loadmat('LabelTrainAll.mat')
label_train = matTrain['label_train']
imgName1 = label_train[0]['imageName']
label1 = label_train[0]['label']

for i in range(label_train.size):
    np.savetxt('./test/' + imgName1[i][0] +'.txt', label1[i], fmt = '%d', delimiter = ',')

matTest = io.loadmat('LabelTestAll.mat')
label_test  = matTest['LabelTest']
imgName2 = label_test[0]['name']
label2 = label_test[0]['label']

for i in range(label_test.size):
    np.savetxt('./test/' + imgName2[i][0] +'.txt', label2[i], fmt = '%d', delimiter = ',')
