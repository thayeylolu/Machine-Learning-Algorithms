# to try to implement the knn algorithm

import numpy as np
dataset = [
            [1 , 3],
            [2 , 2],
            [4 , 2],
            [3 , 1],
            [1 , 4]
          ]
# i have a datSET NOW!
#hurray!

#so the next thing is to have an label which is a scalar vector
label = ['high', 'moderate', 'high', 'moderate', 'high']

#the input vecor that I want to test
input_vector = [2 , 1]

# the function that I want to write to implemet KNN

def knn( dataset, label, input_vector, k):
    '''
        K is the number of vectors in the dataset that have a label 
        close which is closer to what the input vector's label should be
    '''
    # first verify that all the fields in the datasets are integer types or float type
    try:
        dataset.astype(float)

    except ValueError:
        # else if it is a str, or object type , it should return an error message
        print("Could not convert data type to an Float.")

    #-------------Euclidean Distance--------------

    #first we are going to calculate the Euclidean Distance 
    #for all the vectors (data points) in the sdataset, I will subtract 
    #each of  the rows from the input vectors
    #It should end up looking like this:

    #(2 - 3) , (3 - 4), etc
    matDiff = dataset - input_vector

    # square the difference
    squDiff = matDiff ** 2

    #get the sum of each row across the rows to create a new vector
    sumSq = np.sum( squDiff , axis = 1)
    rootMat = sumSq ** .5

    #sorting the array (vector) such that you get an array of indices of the sorted array
    #for example:
    # arr = [6, 29 , 11, 9, 32]; the indices  -> [0, 1, 2, 3, 4]
    # after sorting in ascending order:
    #sorted_arr = [6, 9, 11, 29, 32]  the order of the indices in the sorted array 
    # new_order_of_indices -> [0, 3 , 2, 1, 4 ]

    sortedmatIndices  = np.argsort(rootMat)




    #-------Checking the K datapoints that are closer to the input vector--------
