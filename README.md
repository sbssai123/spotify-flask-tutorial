# spotify-flask-tutorial

Prerequisites:

1. Make sure you have Python 3.7, Flask installed (make sure you are using pip version 3 >)
```
pip install Flask
pip install spotipy --upgrade
```

2. Get a client and secret key from Spotify and export them: 
```
export SPOTIPY_CLIENT_ID='YOUR CLIENT'
export SPOTIPY_CLIENT_SECRET='YOUR SECRET'
export SPOTIPY_REDIRECT_URI='http://127.0.0.1:5000/oauth/callback'
```

3. Add the redirect URI (http://127.0.0.1:5000/oauth/callback) to your Spotify app in the developer console.

How to run this app locally:

1. Navigate to your terminal
2. `git clone https://github.com/sbssai123/spotify-flask-tutorial.git`
3. `cd spotify-flask-tutorial`
4. `export FLASK_APP=spotify-app`
5. `export FLASK_ENV=development`
6. `flask run`

[Slide Deck from HobbyHacks Workshop](https://docs.google.com/presentation/d/1XlORVOcAcJ5ss-PisHV9_OBYfTTgolQpxj1-DJQ0kcI/edit?usp=sharing)

[Slide Deck from DA Hacks Intro To APIs Workshop](https://docs.google.com/presentation/d/1sbem0WdkuQO2RYt58yqXdbDd8LXfZl666mcU4o1yTgk/edit#slide=id.g8ca514999e_0_234)