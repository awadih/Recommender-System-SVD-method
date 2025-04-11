# Recommender-System-SVD-method
Movies recommender system using the Singular Value Decomposition method

# Problem

Herby is an example of recommender system applied to a dataset of ratings for movies.

# Method

Content-based filtering using K-nearest neighbor (KNN) classifier / similarity methods.

# Dataset

The [movies matrix](/resources/movies.mat) contains 1682 movies produced from 1930 till 1998. It contains the variables Y and R:
> * R: a (num_movies x num_users)-matrix of size 1682 x 943 containing the ratings (from 1 to 5) given by 943 users for 1682 movies (of course not all the movies are rated)
> * Y: a (num_movies x num_users)-matrix of size 1682 x 943. This matrix has only values of 0 or 1.

> **NOTE:**  Each cell y_{ij} is 1 if the user i has rated the movie j. The cell y_{ij} is 0 if the user i did not rate the movie j.
movie_ids.text: contains the movie ids and the name of the movies.

> Credits for the dataset goes to Prof. Dr. Wolfgang Konen at TH-Cologne, Germany. 

# Use Case

As a use case the movies recommended for the User 12 in dataset has been listed.

# Sources:
1. 'Using Singular Value Decomposition to Build a Recommender System', Adrian Tam, October 29, 2021, [link](https://machinelearningmastery.com/using-singular-value-decomposition-to-build-a-recommender-system/)
