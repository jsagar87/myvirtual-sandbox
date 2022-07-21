# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

# / **
# A user plays random songs in his spotify account, maintain a live playlist of recently played 25 songs.

# a a b c c d
# a b c d e f g h a b c
import collections


class Song:
    def __init__(self, lastplayedTime):
        __time__ = lastPlayedTIme

    def __compare__(self, song):
        if self.__time__ < song.time:
            return 1



playList = [] * 25
playListCurr = dict()

# songPlayed is called whenever user played a song
def songPlayed(song):
    if playListCurr.get(song):
        if len(playList) > 25:
            delSong = playList[0]
            del (playList[0])
            del (playListCurr[delSong])
    elif not playListCurr.get(song):
        playListCurr[song] = 1
    if len(playList) > 25:
        delSong = playList[0]
        del (playList[0])
        del (playListCurr[delSong])
    id = collections.search(playList, song)
    playList[id] = song
    collections.sort(playList)

# Returns the current play list
def getPlaylist():
    return playList

print("Hello, world!")
songPlayed(a)