import numpy as np
import knn

#dataset
df = np.array([
            [1 , 1, 1, 4],
            [2 , 2, 32, 2.1 ],
            [1 , 4, 31, 0],
            [4 , 2, 10.3, 11],
            [3 , 1, 13.2, 23.9],
            [201 , 24, 31, 19]
          ])

#label
output = ['cat B', 'cat B', 'cat B', 'cat C', 'cat C', 'cat C']

#input vector
vector = [390 , 81 , 17 , 29 ]

result = knn.KNN(df, output, vector, 5)
print(result)

