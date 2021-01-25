# calculating Shannon's Entropy

import numpy as np 

def ShanEnt(dataset):
    '''
    This contains some codes to calculate Shannon Entropy 
    (The expected value of information )

    '''
    #number of rows in the dataset
    num_datapoints = np.shape(dataset)[0]

    #a dictionary : that counts the number of labels in the dataset
    label_count = {}

    for feature in dataset:
        #the label column is the last column or feature
        
        current_label = feature[-1]
        if current_label not in label_count.keys():
            label_count[current_label] = 0
        
            label_count[current_label] += 1


    shan_ent = 0.0

    for key in label_count:
        prob = float(label_count[key])/ num_datapoints
        shan_ent -= prob * np.log2(prob)

    return (shan_ent)

def createData ():
    dataset = np.array(
        [[1, 1, 3 ,'yes'],
        [1, 0, 4 ,'no' ],
        [0, 1, 1, 'no'],
        [0, 1, 9, 'no'],
        [1, 2, 1, 'yes'],
        [1, 1, 1, 'yes'],
        ]
    )

    label = np.array(['surfaces', 'nosurfaces'])
    return (dataset , label)

data, label = createData()


#print(ShanEnt(data))


def SplitDataSet ( data, axis, value):
    retDataset = np.array()
    
    