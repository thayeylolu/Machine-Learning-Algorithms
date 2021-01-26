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