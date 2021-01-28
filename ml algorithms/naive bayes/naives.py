import numpy as np

def conditional_probability (a, b, n):
    """
    conditional probability of an Event A given that an event B occurs
    """
    prob_a = np.count(a)/ n
    prob_b = np.count(b)/n
    cond_prob = prob_a * prob_b

    return cond_prob
    pass 

def naives_bayes():
    """
    This algorithm for Naives Bayes
    """

    pass

#https://github.com/thayeylolu/Machine-Learning-Algorithms

# Split the dataset by class values, returns a dictionary
def separate_by_class(dataset):
	separated = dict()
	for i in range(len(dataset)):
		vector = dataset[i]
		class_value = vector[-1]
		if (class_value not in separated):
			separated[class_value] = list()
		separated[class_value].append(vector)
	return separated