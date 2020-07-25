from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, session
)
import spotipy
from spotipy import oauth2

bp = Blueprint('spotify', __name__)

SCOPE = 'user-library-read user-top-read user-read-currently-playing'
CACHE = '.spotifycache'
sp_oauth = oauth2.SpotifyOAuth(scope=SCOPE,cache_path=CACHE )

@bp.route('/', methods=['GET'])
def login():
    token_info = sp_oauth.get_cached_token()
    if token_info and not sp_oauth.is_token_expired(token_info):
        access_token = token_info['access_token']
        session['access_token'] = access_token
        return redirect(url_for('spotify.last_played'))
    else:
        login_url = sp_oauth.get_authorize_url()
        return redirect(login_url)


@bp.route('/oauth/callback', methods=['GET'])
def set_token():
    code = request.args['code']
    token_info = sp_oauth.get_access_token(code)
    access_token = token_info['access_token']
    session['access_token'] = access_token
    return redirect(url_for('spotify.top_tracks'))


@bp.route('/top_tracks', methods=['GET'])
def top_tracks():
    access_token = session['access_token']
    sp_api = spotipy.Spotify(access_token)
    top_tracks_result = sp_api.current_user_top_tracks()
    
    all_top_tracks = []
    for t in top_tracks_result['items']:
        top_track = {}
        top_track['artist_name'] = t['artists'][0]['name']
        top_track['track_name'] = t['name']
        top_track['album_name'] = t['album']['name']
        top_track['album_image'] = t['album']['images'][0]['url']
        all_top_tracks.append(top_track)

    current_song_result = sp_api.current_user_playing_track()['item']
    current_playing = {}
    current_playing['song'] = current_song_result['name']
    current_playing['image'] = current_song_result['album']['images'][0]['url']
    current_playing['artist'] = current_song_result['artists'][0]['name']
    
    return render_template('top_tracks.html', top_tracks=all_top_tracks, 
    current_playing=current_playing)