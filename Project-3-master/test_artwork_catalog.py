from unittest import TestCase
# need to swap out the regular database for a test database before anything else is imported
import config 
config.db = 'test.db'
from artist_artwork_database import Artwork, Artist, ArtworkArtistDB
from artist_artwork_database import ArtistError, ArtworkError
import ui
import os
import sqlite3

class TestArtwork(TestCase):

    # Checking if Artist info is saved in database
    def test_check_artist_in_data(self):


        with sqlite3.connect(config.db) as con:
            artist_rows = con.execute('delete from artist')  # delete all data from test db
        con.close()

        store = ArtworkArtistDB()

        # art_artist expects an Artist object so this is an error
        # database.add_artist('ArtworkArtistDB')
        example_artist = Artist('Boris', 'example@example.com')
        store.add_artist(example_artist)

        # TestArtist.add_artist is a function object so this checks if 
        # the text 'Test ArtworkArtistDB' is in a function definition
        # self.assertIn('Test ArtworkArtistDB', TestArtist.add_artist)

        # Check if the artist was added
        con = sqlite3.connect(config.db)
        artist_rows = con.execute('select * from artist where ArtistName = "Boris" and email = "example@example.com"').fetchall()

        con.close()

        self.assertEqual(1, len(artist_rows))  # one artist matches so add must have worked
        
        # TestArtist.add_artist('Another Artist Test')
        # self.assertIn('Test ArtworkArtistDB ', TestArtist.add_artist)
        # self.assertIn('Another Test Student', TestArtist.add_artist)



    # Checking if Artwork info is saved in database
    def test_check_artwork_in_data(self):
        TestArtwork = ArtworkArtistDB()
        TestArtwork.add_artwork('ArtworkArtistDB')
        self.assertIn('Test ArtworkArtistDB', TestArtwork.add_artist)

        TestArtwork.add_artist('Another Artist Test')
        self.assertIn('Test ArtworkArtistDB ', TestArtwork.add_artist)
        self.assertIn('Another Test Student', TestArtwork.add_artist)
    
    # Checking if Artist info is getting duplicate
    def test_artist_already_in_data(self):
        TestArtist = ArtworkArtistDB()
        TestArtist.add_artist('Test ArtworkArtistDB')
        with self.assertRaises(ArtistError):
            TestArtist.add_artist('Test ArtworkArtistDB')

    #Checking if artwor info is getting duplicate in the database
    def test_artwork_already_in_database(self):
        TestArtwork = ArtworkArtistDB()
        TestArtwork.add_artwork('Test ArtworkArtistDB')
        with self.assertRaises(ArtworkError):
            TestArtwork.add_artwork('Test ArtworkArtistDB')
    # Making sure the artist info is only Artist Name and Email
    def test_get_artist_info(self):
        Artist = ui.get_new_artist()
        self.assertEqual('name', 'email')

    def test_index_of_artists(self):
        TestArtist = ArtworkArtistDB()
        TestArtist.add_artist('Vick')
        TestArtist.add_artist('Vicky')
        TestArtist.add_artist('Victoria')

        self.assertIsNone(TestArtist.add_artist('Mike'))


