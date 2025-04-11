from typing import Optional
from methods import sim

# List of similarity metrics
LIST_METRICS = ['Cosine', 'Euclid', 'Jaccard', 'Minkowski', 'Pearson']
K_KNN = 50  # The number of the Nearest Neighbors for the KNN-Algorithm


def predict_rating_user_user_cf(df, user, item, sim_metric):
    """ returns predicted rating of user for the item i,
    neighbors: list of tuples (similarity: user and othe_user, rating of other_user for item) """
    # Check the correctness of user1, user2 and the given sim_metric
    if user not in df.columns or item not in df.index or sim_metric not in LIST_METRICS:
        print('Please enter valid user-name(s) and/or similarity metric!')
    else:
        # retrieve users having rated the 'item':
        neighbors = [(sim(df[user].tolist(), df[other_user].tolist(), sim_metric), df.loc[item, other_user]) for
                     other_user in df.columns if (other_user != user and df.loc[item, other_user] != 0)]
        # Sort them by similarity
        neighbors.sort(key=lambda tpl: tpl[0], reverse=True)
        # compute weighted average of the k-NN's ratings
        num = sum(similarity * rating for (similarity, rating) in neighbors[:K_KNN])
        denum = sum(abs(similarity) for (similarity, _) in neighbors[:K_KNN])
        return num / denum


def predict_rating_item_item_cf(df, user, item, sim_metric):
    """ returns predicted rating of user for the item i,
    neighbors: list of tuples (similarity: item and othe_item, rating of user for other_item) """
    # Check the correctness of user1, user2 and the given sim_metric
    if user not in df.columns or item not in df.index or sim_metric not in LIST_METRICS:
        print('Please enter valid user-name(s) and/or similarity metric!')
    else:
        # retrieve items have been rated by the 'user':
        neighbors = [(sim(df.loc[item].tolist(), df.loc[other_item].tolist(), sim_metric), df.loc[other_item, user]) for
                     other_item in df.index if (other_item != item and df.loc[other_item, user] != 0)]

        # Sort them by similarity
        neighbors.sort(key=lambda tpl: tpl[0], reverse=True)
        # compute weighted average of the k-NN's ratings
        num = sum(similarity * rating for (similarity, rating) in neighbors[:K_KNN])
        denum = sum(similarity for (similarity, _) in neighbors[:K_KNN])
        return num / denum


def recommend_to_user(df, user, sim_metric):
    """ returns a sorted dictionary containing the top 100 recommendable movies:
    {items not rated by user: predicted rating} """
    # check the correctness of user and sim_metric
    if user not in df.columns or sim_metric not in LIST_METRICS:
        print('Please enter valid user-name(s) and/or similarity metric!')
    else:
        dict_items = {}
        for item in df.index:
            if df.loc[item, user] == 0:
                dict_items.update({item: predict_rating_user_user_cf(df, user, item, sim_metric)})
        # Sort according to the predicted rating
        sorted_dict = {k: v for k, v in sorted(dict_items.items(), key=lambda itm: itm[1], reverse=True)}
        return {item: sorted_dict[item] for item in list(sorted_dict)[0:100]}
