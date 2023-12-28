'''4.Develop a recommendation system using Flask that suggests content to users 
based on their preferences.'''
# Code



from flask import Flask, request, render_template




app = Flask(__name__)

# Sample user preferences data (you can replace this with a real database)
user_preferences = {
    'user1': {'action', 'comedy'},
    'user2': {'drama', 'romance'},
    # Add more users and their preferences
}

# Sample movie data (you can replace this with a real database)
movie_data = {
    'movie1': {'action', 'thriller'},
    'movie2': {'comedy', 'romance'},
    'movie3': {'drama', 'romance'},
    'movie4': {'action', 'comedy', 'drama'},
    # Add more movies and their genres
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user = request.form['user']

    if user in user_preferences:
        user_prefs = user_preferences[user]
        recommended_movies = get_recommendations(user_prefs)
        return render_template('recommendations.html', user=user, recommendations=recommended_movies)
    else:
        return render_template('error.html', message=f'User "{user}" not found.')

def get_recommendations(user_prefs):
    recommended_movies = set()

    for movie, genres in movie_data.items():
        if any(genre in user_prefs for genre in genres):
            recommended_movies.add(movie)

    return recommended_movies

if __name__=="__main__":
    app.run(host="0.0.0.0")