# import re
# import os
# import numpy as np
# import spotipy
# from spotipy import oauth2
# from collections import OrderedDict
# from datetime import datetime
#
# from . import db
#
# scopes = 'playlist-modify-public'
# sp_oauth = oauth2.SpotifyOAuth(client_id=os.environ['CLIENT_ID'],
#                                client_secret=os.environ['CLIENT_SECRET'],
#                                redirect_uri=os.environ['REDIRECT_URI'],
#                                scope=scopes)
#
#
# def get_auth_url():
# 	auth_url = sp_oauth.get_authorize_url(show_dialog=False)
# 	return auth_url
#
#
# def get_access_and_refresh(code):
# 	return sp_oauth.get_access_token(code)
#
#
# def refresh_access_token(refresh_token, user_id):
# 	token_info = sp_oauth.refresh_access_token(refresh_token)
# 	token = token_info['access_token']
# 	user_spot_info = SpotifyToken.query.filter_by(user_id=user_id).first()
# 	user_spot_info.access_token = token
# 	db.session.commit()
# 	sp = spotipy.Spotify(auth=token)
# 	return sp
#
#
# def get_playlist_genre(artist_list, sp):
# 	artist_list = np.array_split(artist_list, 5)
# 	artists = []
# 	for artist in artist_list:
# 		artists += sp.artists(artist)['artists']
# 	artist_genres = [artist['genres'] for artist in artists if artist is not None]
# 	artist_genres = [genre for sublist in artist_genres for genre in sublist]
# 	genre_dict = {}
# 	for genre in artist_genres:
# 		if genre in genre_dict:
# 			genre_dict[genre] += 1
# 		else:
# 			genre_dict[genre] = 1
# 	return max(genre_dict, key=genre_dict.get)
#
#
# def get_curr_artist_tracks(user_id):
# 	tracks = ArtistTracks.query.filter_by(artist_id=user_id).all()
# 	final_list_of_tracks = []
# 	for track in tracks:
# 		track_dict = OrderedDict()
# 		track_dict['track_uri'] = track.track_uri
# 		track_dict['track_name'] = track.track_name
# 		track_dict['track_link'] = track.track_link
# 		track_dict['track_summary'] = track.track_summary
# 		placed_playlists = PlaylistToPlacedSong.query.filter_by(song_id=track.id, placed=1).all()
# 		track_dict['placed_playlists'] = []
# 		if len(placed_playlists) != 0:
# 			for playlist in placed_playlists:
# 				playlist_name = PlaylistDetails.query.filter_by(id=playlist.playlist_id).first().name
# 				track_dict['placed_playlists'].append(playlist_name)
# 		final_list_of_tracks.append(track_dict)
# 	return final_list_of_tracks
#
#
# def refresh_playlist_deets(p_uri, sp):
# 	sp_playlist_deets = sp.playlist(playlist_id=p_uri, fields='name,followers,tracks')
#
# 	stored_playlist = PlaylistDetails.query.filter_by(playlist_uri=p_uri).first()
#
# 	overall_genre = get_playlist_genre(
# 		[track['track']['artists'][0]['uri'] for track in sp_playlist_deets['tracks']['items']
# 		 if track['track'] is not None], sp)
# 	stored_playlist.num_followers = sp_playlist_deets['followers']['total']
# 	stored_playlist.num_tracks = sp_playlist_deets['tracks']['total']
# 	stored_playlist.overall_genre = overall_genre
# 	stored_playlist.last_updated = datetime.now()
#
# 	# Delete all songs on the playlist so that we can make sure we have the newest ones
# 	all_artists = ArtistsInPlaylist.query.filter_by(playlist_id=stored_playlist.id).all()
# 	print([x.id for x in all_artists])
#
# 	all_plist_artists = []
# 	for sp_artist in sp_playlist_deets['tracks']['items']:
# 		if sp_artist['track'] is not None:
# 			artist_name = re.sub('[^A-Za-z0-9]+', ' ', sp_artist['track']['artists'][0]['name'])
# 			artist_uri = sp_artist['track']['artists'][0]['uri']
# 			artist_in_playlist = ArtistsInPlaylist(stored_playlist.id, artist_name=artist_name, artist_uri=artist_uri)
# 			all_plist_artists.append(artist_in_playlist)
# 	db.session.add_all(all_plist_artists)
# 	db.session.commit()
