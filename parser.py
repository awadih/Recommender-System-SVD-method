import pandas as pd
from scipy.io import loadmat


def create_dataframe(metadata_file, list_of_movies_file):
    """ create a dataframe representing the appropriate rating matrix """
    mat = loadmat(metadata_file)
    # 'Y': variable in mat file as mentioned in README file
    data = mat['Y']
    num_users = len(data[0])
    list_movies = []
    with open(list_of_movies_file, "r", encoding='utf-8') as f:
        lines = f.readlines()  # list of lines with '\n'
        for line in lines:
            line = line.strip('\n')
            line = line.replace(';', '. ')
            list_movies.append(line)
    df = pd.DataFrame(data, index=list_movies, columns=['User ' + str(i + 1) for i in range(num_users)])
    return df
