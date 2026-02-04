# Music Playlist


playlist = ["Sheet Lahar", "Villager", "Ranjhana"]

current_song = playlist[0]
print("this is current song : ", current_song)

next_song = playlist[1]
print("Next song is : ", next_song)
playlist.append("Dhurandhar")

popex = playlist.pop(2)
print("Removed song is : ", popex)

print("Updated Playlist:", playlist)