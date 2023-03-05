from project.album import Album
from project.band import Band
from project.song import Song

band = Band("Death")
album = Album("The Sound of Perseverance")
band.add_album(album)
message = band.remove_album("The Sound of Perseverance")
expected = "Album The Sound of Perseverance has been removed."
print(message)