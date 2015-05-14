import unittest
from music_library import Song, Playlist


class Tests(unittest.TestCase):

    def setUp(self):
        self.song1 = Song(
            artist="Metalica", album="metalica", length=385, song_name="nothing else matters")

    def testlength(self):
        self.assertTrue(self.song1.length_rpr(minutes=True) == "06:25")
        self.assertTrue(self.song1.length_rpr(seconds=True) == "25")
        self.assertTrue(self.song1.length_rpr(hours=True) == "0:06:25")

    def test_class_Playlist_method_artist(self):
        song2 = Song(artist="Metalica", album="metalica",
                     length=385, song_name="Nothing else matters")
        song3 = Song(
            artist="Metalica", album="metalica", length=385, song_name="The Unforgiven")
        song4 = Song(artist="Iron Maiden", album="Power Slave",
                     length=385, song_name="Fear of the dark")
        song5 = Song(
            artist="Iron Maiden", album="Power Slave", length=385, song_name="Acces High")
        song6 = Song(artist="Qvkata DLG", album="Човека  който се смее",
                     length=385, song_name="Екстра а ти ?")

        songs = [song2, song3, song4, song5, song6]

        pl = Playlist("rado")
        pl.add_songs(songs)

        self.assertTrue(pl.artists()["Metalica"] == 2)
        self.assertTrue(pl.artists()["Iron Maiden"] == 2)
        self.assertTrue(pl.artists()["Qvkata DLG"] == 1)

    def test_class_Playlist_method_add_song(self):
        song2 = Song(artist="Metalica", album="metalica",
                     length=385, song_name="Nothing else matters")
        pl = Playlist("rado")
        pl.add_song(song2)
        self.assertTrue(song2 in pl.song_lst)

    def test_class_Playlist_method_remove_song(self):
        song2 = Song(artist="Metalica", album="metalica",
                     length=385, song_name="Nothing else matters")
        pl = Playlist("rado")
        pl.add_song(song2)
        pl.remove_song(song2)
        self.assertTrue(len(pl.song_lst) == 0)

    def test_class_Playlist_method_total_length(self):
        # 86400 seconds  =  1 day
        song2 = Song(artist="Metalica", album="metalica",
                     length=86400, song_name="Nothing else matters")
        song3 = Song(
            artist="Metalica", album="metalica", length=385, song_name="The Unforgiven")
        song4 = Song(artist="Iron Maiden", album="Power Slave",
                     length=385, song_name="Fear of the dark")
        song5 = Song(
            artist="Iron Maiden", album="Power Slave", length=385, song_name="Acces High")
        song6 = Song(artist="Qvkata DLG", album="Човекът  който се смее",
                     length=385, song_name="Екстра а ти ?")

        songs = [song2, song3, song4, song5, song6]

        pl = Playlist("rado")
        pl.add_songs(songs)
        self.assertTrue(str(pl.total_length()) == "1 day, 0:25:40")
        pl.remove_song(song2)
        self.assertTrue(str(pl.total_length()) == "0:25:40")

    def test_class_Playlist_method_current_song(self):
        song2 = Song(artist="Metalica", album="metalica",
                     length=385, song_name="Nothing else matters")
        song3 = Song(
            artist="Metalica", album="metalica", length=385, song_name="The Unforgiven")
        song4 = Song(artist="Iron Maiden", album="Power Slave",
                     length=385, song_name="Fear of the dark")
        song5 = Song(
            artist="Iron Maiden", album="Power Slave", length=385, song_name="Acces High")
        song6 = Song(artist="Qvkata DLG", album="Човекът  който се смее",
                     length=385, song_name="Екстра а ти ?")
        songs = [song2, song3, song4, song5, song6]

        pl = Playlist("rado", repeat=True)
        pl.add_songs(songs)
        self.assertTrue(str(pl.current_song(10)) ==
                        "Metalica - Nothing else matters from metalica - 385")
        self.assertTrue(str(pl.current_song(2)) ==
                        "Iron Maiden - Fear of the dark from Power Slave - 385")

        pl2 = Playlist("rado")  # repeat  is  False
        pl2.add_songs(songs)

        self.assertTrue(str(pl2.current_song(
            10)) == "Qvkata DLG - Екстра а ти ? from Човекът  който се смее - 385")

    def test_class_Playlist_method_current_song(self):
        song2 = Song(artist="Metalica", album="metalica",
                     length=385, song_name="Nothing else matters")
        song3 = Song(
            artist="Metalica", album="metalica", length=385, song_name="The Unforgiven")
        song4 = Song(artist="Iron Maiden", album="Power Slave",
                     length=385, song_name="Fear of the dark")
        song5 = Song(
            artist="Iron Maiden", album="Power Slave", length=385, song_name="Acces High")
        song6 = Song(artist="Qvkata DLG", album="Човекът  който се смее",
                     length=385, song_name="Екстра а ти ?")

        songs = [song2, song3, song4, song5, song6]

        pl = Playlist("rado", repeat=True)
        pl.add_songs(songs)

        self.assertTrue(
            str(pl.next_song()) == "Metalica - The Unforgiven from metalica - 385")
        self.assertTrue(
            str(pl.next_song()) == "Iron Maiden - Fear of the dark from Power Slave - 385")
        self.assertTrue(
            str(pl.next_song()) == "Iron Maiden - Acces High from Power Slave - 385")

        pl2 = Playlist("rado2", shuffle=True)
        pl2.add_songs(songs)
        #print("Shuffle test :" , pl2.next_song())
        # print(pl.ppprint_playlist())

    def test_class_Playlist_method_ppprint(self):
        song2 = Song(artist="Metalica", album="metalica",
                     length=385, song_name="Nothing else matters")
        song3 = Song(
            artist="Metalica", album="metalica", length=7200, song_name="The Unforgiven")
        song4 = Song(artist="Iron Maiden", album="Power Slave",
                     length=385, song_name="Fear of the dark")
        song5 = Song(
            artist="Iron Maiden", album="Power Slave", length=86400, song_name="Acces High")
        song6 = Song(artist="Qvkata DLG", album="Човекът  който се смее",
                     length=896385, song_name="Екстра а ти ?")
        songs = [song2, song3, song4, song5, song6]

        pl = Playlist("rado", shuffle=True)
        pl.add_songs(songs)
        pl.next_song()
        # pl.ppprint_playlist()

    def test_class_Playlist_method_save_and_load(self):
        song2 = Song(artist="Metalica", album="metalica",
                     length=385, song_name="Nothing else matters")
        song3 = Song(
            artist="Metalica", album="metalica", length=7200, song_name="The Unforgiven")

        pl = Playlist("default")
        pl.add_song(song2)
        pl.add_song(song3)
        pl.save()
        pl.load()
        # pl.ppprint_playlist()


if __name__ == '__main__':
    unittest.main()
