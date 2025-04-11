from typing import Optional
from scipy.spatial import distance
from scipy.stats import pearsonr


def sim(vector1, vector2, sim_metric, order_minkowski: Optional[int] = 5):
    """ returns the similarity value between two vectors using a given similarity metric
    * order_minkowski: The order of the Minkowski distance"""
    if sim_metric == 'Cosine':
        return distance.cosine(vector1, vector2)
    elif sim_metric == 'Euclid':
        return distance.euclidean(vector1, vector2)
    elif sim_metric == 'Jaccard':
        return distance.jaccard(vector1, vector2)
    elif sim_metric == 'Pearson':
        return pearsonr(vector1, vector2)[0]
    elif sim_metric == 'Minkowski':
        return distance.minkowski(vector1, vector2, order_minkowski)
    print('Please enter a valid similarity metric!')
