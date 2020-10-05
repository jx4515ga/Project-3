from unittest import TestCase
from artist_artwork_database import Artwork, Artist, ArtworkArtistDB
from artist_artwork_database import ArtistError, ArtworkError
import ui
import os

class TestArtwork(TestCase):

    # Checking if Artist info is saved in database
    def test_check_artist_in_data(self):
        TestArtist = ArtworkArtistDB()
        TestArtist.add_artist('ArtworkArtistDB')
        self.assertIn('Test ArtworkArtistDB', TestArtist.add_artist)

        TestArtist.add_artist('Another Artist Test')
        self.assertIn('Test ArtworkArtistDB ', TestArtist.add_artist)
        self.assertIn('Another Test Student', TestArtist.add_artist)
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


