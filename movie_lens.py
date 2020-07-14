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

    print(data.head(5))
    print('\n')

    #mean movie ratings for each film grouped by gender
    mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
    print(mean_ratings)
    print('\n')

    ratings_by_title = data.groupby('title').size()
    print(ratings_by_title[:10])
    print('\n')

    active_titles = ratings_by_title.index[ratings_by_title >= 250]
    print(active_titles)
    print('\n')

    mean_ratings = mean_ratings.loc[active_titles]
    print(mean_ratings)
    print('\n')

    #To see the top films among female viewers.
    top_female_ratings = mean_ratings.sort_values(by=['F'], ascending=False)
    print(top_female_ratings[:10])
    print('\n')

    #Calculate diferent in rating between F and M
    mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
    sorted_by_diff = mean_ratings.sort_values(by="diff", ascending=True)
    print(sorted_by_diff[:10])
    print('\n')

    #disgreement in the ratings in the viewers
    rating_std_by_title = data.groupby('title')['rating'].std()
    rating_std_by_title = rating_std_by_title.loc[active_titles]
    print(rating_std_by_title.sort_values(ascending=False)[:10])
    print('\n')

if __name__ == '__main__':
    users, ratings, movies = load_data()
    explore_data(users, ratings, movies)
