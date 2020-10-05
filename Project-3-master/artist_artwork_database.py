import sqlite3
import os 


db = os.path.join('artworkStore.db')

# Creating Artist Class to collect data
class Artist:

    def __init__(self, name, email, id = None):
        self.name = name
        self.email = email
        self.id = id

        self.artworkStore = ArtworkArtistDB()

    def save(self):
        self.artworkStore.add_artist(self)


    def __str__(self):
        return f'ID: {self.id}, Name{self.name}, Email{self.name}'

    def __repr__(self):
        return f'ID: {self.id}, Name{self.name}, Email{self.name}'


# Creating an Artwork Class to collect artwork data

class Artwork:

    def __init__(self, artistname, artname, price, availability, id = None):
        self.artistname = artistname
        self.artname = artname
        self.price = price
        self.availability = availability
        self.id = id

        self.artworkStore = ArtworkArtistDB()

    # Collenting the data from the fuction add_artwork 
    def save(self):
        self.artworkStore.add_artwork(self)

    def delete(self):
        self.artworkStore._delete_art(self)


    def __str__(self):
        return f'ID: {self.id}, Name {self.artistname}, Artwork Name:{self.artname}, Price{self.price}, Available{self.availability}'

    def __repr__(self):
        return f'ID: {self.id}, Name {self.artistname}, Artwork Name{self.artname}, Price{self.price}, Available{self.availability}'

    
# Creating database and tables tp store en values mentined above
class ArtworkArtistDB:

#Creating two tables one called Artist and Artwork 
    def __init__(self):
        with sqlite3.connect(db) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS Artist(ArtistName TEXT UNIQUE, Email TEXT)')
        with sqlite3.connect(db) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS Artwork(ArtistName TEXT UNIQUE, ArtworkName TEXT UNIQUE, Price REAL, Available TEXT)')
            

            

    # Adding new artist(name and email) into the Artist table and then storing into the database

    def add_artist(self, artist):

        insert_sql = 'INSERT INTO Artist(ArtistName , Email) VALUES(?,?)'
        
        

        try:
            with sqlite3.connect(db) as conn:
                rows_modified = conn.execute(insert_sql,(artist.name, artist.email))
           
            return rows_modified
        except sqlite3.IntegrityError as e:
            raise ArtistError(f'Error adding {artist.name}') from e
        finally:
        
            conn.commit()

    #Adding new artwork (Artist name, Artwork name, Price, Availability) into the Artwork table and storing into the database 
    def add_artwork(self, artworks):
        
        insert_sql = 'INSERT INTO Artwork(ArtistName, ArtworkName, Price, Available ) VALUES (?,?,?,?)'
        

        try:
            with sqlite3.connect(db) as conn:
                rows_modified = conn.execute(insert_sql, (artworks.artistname, artworks.artname, artworks.price, artworks.availability))
                
            return rows_modified
        except sqlite3.IntegrityError as e:
            raise ArtworkError(f'Error - this artwork is already in the database. {artworks.artistname2}') from e
        finally:
            
            
            conn.close()

    #Displaying all the artwork available in the database 

    def get_all_artwork(self):
        get_all_artwork_sql = 'SELECT rowid, * FROM Artwork'
        conn = sqlite3.connect(db)
        conn.row_factory = sqlite3.Row
        rows = conn.execute(get_all_artwork_sql)

        artworks = []

        for r in rows:
            artwork = Artwork(r['ArtistName'], r['ArtworkName'], r['Price'], r['Available'])
            artworks.append(artwork)
        conn.close()
        return artworks

    
    # Displaying artwork searching by artist name.
    def get_artwork_by_name(self, name):
        search_sql = 'SELECT rowid, * FROM Artwork WHERE rowid = ?' 
        #UPPER(ArtworkName) like UPPER(?)'
        conn = sqlite3.connect(db)
        conn.row_factory = sqlite3.Row
        rows = conn.execute(search_sql, (name,))
        artwork_data = rows.fetchone()
        if artwork_data:
            artwork_data = Artwork(artwork_data ['id'], artwork_data [' ArtistName '], artwork_data [' ArtworkName '], artwork_data [' Price '], artwork_data [' Available: '])
        conn.close()
        return artwork_data
    

    #Deleting an artowork from the database looking by artist name
    def _delete_art(self, artworks):
        if not artworks.artname:
            raise ArtworkError('Artwork does not have that name')


        delete_sql = 'DELETE FROM Artwork WHERE rowid = ?'
        
        with sqlite3.connect(db) as conn:
            deleted  = conn.execute(delete_sql,(artworks.artname,))
            deleted.count = deleted.rowcount
        
        conn.close()

        if deleted.count == " ":
            raise ArtworkError('Artwork with that name not ')

        


class ArtistError(Exception):
    pass

class ArtworkError(Exception):
    pass

