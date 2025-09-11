from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re

#Set up client Credentials
sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(
    client_id = "f630ad3f2a8f4ed2a2ac610b5121f50b",
    client_secret = "aedbdbe0ec224b26b440c906344503b4"
))


#Full Track URL

track_url = "3h4T9Bg8OVSUYa6danHeH5"

#Extract Track Id Directly from URL using Regex


track = sp.track(track_url)
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
df = pd.DataFrame([track_data])
print("\n Print data as DataFrame")
print(df)

#Save metadata to csv
df.to_csv("Spotify_track_data.csv", index=False)

#Visualize Track Data

features = ["Popularity", "Durations(minutes)"]
values = [track_data["Popularity"], track_data["Duration (minutes)"]]

plt.figure(figsize=(8,5))
plt.bar(features, values, color = "skyblue", edgecolor = 'black')
plt.title(f"Track Metadata for '{track_data['Track Name']}'")
plt.ylabel('value')
plt.show()





