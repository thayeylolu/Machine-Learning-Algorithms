# to try to implement the knn algorithm
# to solve classificiation problems

import numpy as np
import operator as op

# Module implemet KNN


def KNN( dataset, label, input_vector, k):
    
    '''
        1. dataset: a numpy array of type float
        2. label: the 
        3. input_vector : a list of values (can be integer, string)
        4. k : the number of vectors in the dataset that have a label 
        close which is closer to what the input vector's label should be
    '''


    # first verify that all the fields in the datasets are integer types or float type
    try:
        dataset = dataset.astype(float)
        input_vector = np.array(input_vector)
        k = int(k)

    except ValueError:
        # else if it is a str, or object type , it should return an error message
        print("Could not convert data type to an Float.")

    #-------------Euclidean Distance--------------

    #first we are going to calculate the Euclidean Distance 
    #for all the vectors (data points) in the sdataset, I will subtract 
    #each of  the rows from the input vectors
    #It should end up looking like this:

    #(2 - 3) , (3 - 4), etc
    if  (dataset.shape[1] == input_vector.shape[0]):
        matDiff = dataset - input_vector

        # square the difference
        squDistance = matDiff ** 2

        #get the sum of each row across the rows to create a new vector
        distance = np.sum( squDistance , axis = 1)
        distanceMat = distance ** .5

        #sorting the array (vector) such that you get an array of indices of the sorted array
        #for example:
        # arr = [6, 29 , 11, 9, 32]; the indices  -> [0, 1, 2, 3, 4]
        # after sorting in ascending order:
        # sorted_arr = [6, 9, 11, 29, 32]  the order of the indices in the sorted array 
        # new_order_of_indices -> [0, 3 , 2, 1, 4 ]

        sortedmatIndices  = np.argsort(distanceMat)

        #-------Checking the K datapoints that are closer to the input vector--------

        # create a dictionary containing the labels as keys and the number of times they appear as values
        countLabel = {}
    
        # loop through the number of nearest neighbours you want
        for i in range (k):

            # the choosen Label
            choosenLabel = label[sortedmatIndices[i]]

            # count the number of times the label appears, and store it in a dictionary countLabel
            countLabel[choosenLabel] = label.count(choosenLabel)
    
        # sort the items in the dictionary by the values and arrange them in descending order
        
        sorted_labels = sorted(countLabel.items(), key=op.itemgetter(1), reverse = True)

    return sorted_labels[0] [0]
    

