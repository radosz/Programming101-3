from mutagen.mp3 import MP3
from datetime import timedelta
from random import randint
from tabulate import tabulate
from filetype_scannner import lst_filetype_scan
from mutagen.easyid3 import EasyID3
import curses
import time
import mutagen.id3
import player


class Song:

    def __init__(self, artist, song_name, album, length, path=" "):
        self.artist = artist
        self.song_name = song_name
        self.album = album
        self.length = int(length)
        self.path = path

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.song_name, self.album, self.length)

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash(self.__str__())

    def __repr__(self):
        return self.__str__()

    def length_rpr(self, seconds=False, minutes=False, hours=False):

        str_hours = "".join(str(timedelta(seconds=self.length))).split(":")[0]
        str_minutes = "".join(
            str(timedelta(seconds=self.length))).split(":")[1]
        str_seconds = "".join(
            str(timedelta(seconds=self.length))).split(":")[2]

        if not seconds and not minutes and not hours:
            # 86400 seconds = one day
            if int(self.length) >= 86400:
                return timedelta(seconds=self.length)
            # 3600 seconds  = 1 hour
            if int(self.length) >= 3600:
                hours = True
            elif int(self.length) > 60:
                minutes = True

        if seconds:
            return str_seconds
        if minutes:
            return "{}:{}".format(str_minutes, str_seconds)
        if hours:
            return "{}:{}:{}".format(str_hours, str_minutes, str_seconds)


class Playlist:

    def __init__(self, name, shuffle=False, repeat=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.song_lst = []
        self.__song_index = 0

    def __str__(self):
        return str(self.ppprint_playlist())

    def add_song(self, song):
        self.song_lst.append(song)

    def remove_song(self, song):
        try:
            self.song_lst.remove(song)
        except ValueError:
            pass

    def add_songs(self, songs):
        self.song_lst += songs

    def total_length(self):
        length = [x.length for x in self.song_lst]
        total = (sum(length))
        return timedelta(seconds=total)

    def artists(self):
        art = [x.artist for x in self.song_lst]
        result = {k: art.count(k) for k in set(art)}
        return result

    def current_song(self):
        try:
            return self.song_lst[self.__song_index]
        except IndexError:
            if self.repeat:
                self.__song_index = 0
                return self.song_lst[0]
            pass  # End  of  Playlist

    def next_song(self):
        if not self.shuffle:
            self.__song_index += 1
            return self.current_song()

        self.__song_index = randint(self.__song_index, len(self.song_lst) - 1)
        return self.current_song()

    def ppprint_playlist(self):
        head = ["Play", "Artist", "Song", "length"]
        songs = [x.song_name for x in self.song_lst]
        artists = [x.artist for x in self.song_lst]
        lengths = [x.length_rpr() for x in self.song_lst]
        play = [" " for x in self.song_lst]
        current_play = "".join(
            [str(x) for x in self.song_lst if self.current_song() == x])
        play[self.song_lst.index(current_play)] = ">" * 5
        table = [x for x in zip(play, artists, songs, lengths)]
        str_play_table = tabulate(table, headers=head, tablefmt="fancy_grid")
        total_l = "Total lenght:{} ".format(self.total_length())
        return str_play_table + "\n" + total_l + "\n"

    def save(self, filename="default_playlist.txt"):
        artists = [x.artist for x in self.song_lst]
        songs = [x.song_name for x in self.song_lst]
        albums = [x.album for x in self.song_lst]
        lengths = [x.length for x in self.song_lst]
        paths = [x.path for x in self.song_lst]
        str_save = "\n".join([str(x)
                              for x in zip(artists, songs, albums, lengths, paths)])
        str_save = "".join(
            [x for x in str_save if x != "(" and x != ")"and x != "'"])
        file = open(filename, "w")
        file.write(str_save)
        file.close()

    @staticmethod
    def load(filename="default_playlist.txt"):
        file = open(filename, "r")
        content = file.read()
        pls = [x.split(",") for x in content.split("\n")]
        playlist = Playlist("default")
        file.close()

        # artist = x[0]
        # song_name = x[1]
        # album = x[2]
        # length = x[3]
        # path = x[4]

        for x in pls:
            playlist.add_song(Song(x[0], x[1], x[2], x[3], x[4]))


class MusicCrawler(Playlist):

    def __init__(self, path, shuffle=False, repeat=False):
        self.path = path
        super().__init__("mutagen", shuffle, repeat)

    def generate_playlist(self):
        search_types = ["mp3", "ogg"]
        full_path = []
        # files is dict
        files = lst_filetype_scan(self.path, search_types)
        for st in search_types:
            full_path += [self.path + x for x in files[st]]

        for id3 in full_path:
            try:
                artist = EasyID3(id3)["artist"][0]
                title = EasyID3(id3)["title"][0]
                album = EasyID3(id3)["album"][0]
                length = MP3(id3).info.length
            except mutagen.id3._util.ID3NoHeaderError:
                continue

            super().add_song(
                Song(artist, title, album, length, id3))

# TODO : Make keyboard control


class MusicPlayer(MusicCrawler):

    def __init__(self, path, shuffle=False, repeat=False):
        super().__init__(path, shuffle, repeat)
        self.pls = super().generate_playlist()
        if not shuffle:
            self.song = super().current_song()
        self.song = super().next_song()
        self.playing = player.play(self.song.path)
        self.to_scr()

    def __repr__(self):
        return super().ppprint_playlist()

    def stop(self):
        player.stop(self.playing)

    def next(self):
        self.stop()
        self.playing = player.play(super().next_song().path)
        self.to_scr()

    def to_scr(self):
        curses.wrapper(self.auto_next)

    def auto_next(self, window):

        try:
            window.addstr(0, 0, "Welcome to R.A Player")
            window.addstr(2, 0, super().ppprint_playlist())
        except Exception:
            pass

        window.refresh()
        elapsed_time = 0
        while elapsed_time < self.song.length:
            elapsed_time += 1
            time.sleep(1)
            window.addstr(
                1, 0, "Elapsed Time :" + str(timedelta(seconds=elapsed_time)))
            window.refresh()
        self.next()
        return self.auto_next()
