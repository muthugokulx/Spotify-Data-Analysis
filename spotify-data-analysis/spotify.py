from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re

#Set up client Credentials
sp = spotipy.spotify(auth_manager = SpotifyClientCredentials(
    client_id = "f630ad3f2a8f4ed2a2ac610b5121f50b",
    client_secret = "*****************************"
))


#Full Track URL

track_url = "https://open.spotify.com/track/7qiZfU4dY1lWllzX7mPBI"

#Extract Track Id Directly from URL using Regex

track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

track = sp.track(track_id)
print(track)

#Extract Metadata

track_data = {
    'Track Name' : track['name'],
    'Artist' : track['artists'][0]['name'],
    'Album' : track['album']['name'],
    'Popularity' : track['popularity'],
    'Duration (minutes)' : track['duration_ms'] / 60000

}

#Convert Metadata to Dataframe
df = pd.DataFrame(track_data)
print("\n Print data as DataFrame")
print(df)

#Save metadata to csv
df.to_csv("Spotify_track_data.csv", index=False)



