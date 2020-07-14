import pandas as pd


def load_data():
    unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
    users = pd.read_table('datasets/movielens/users.dat', sep='::', header=None, names=unames,engine='python')
    rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
    ratings = pd.read_table('datasets/movielens/ratings.dat', sep='::', header=None, names=rnames, engine='python')
    mnames = ['movie_id', 'title', 'genres']
    movies = pd.read_table('datasets/movielens/movies.dat', sep='::', header=None, names=mnames, engine='python')

    return users, ratings, movies

def explore_data(users, ratings, movies):
    print(users[:5])
    print('\n')
    print(ratings[:5])
    print('\n')
    print(movies[:5])
    print('\n')

    print(ratings.info())
    print('\n')

    data = pd.merge(pd.merge(ratings, users), movies)
    print(data.info())
    print('\n')


if __name__ == '__main__':
    users, ratings, movies = load_data()
    explore_data(users, ratings, movies)
