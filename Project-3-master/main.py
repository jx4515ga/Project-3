from artist_artwork_database import Artist, ArtworkArtistDB
import ui


store = ArtworkArtistDB()

#Creating Menu
def create_menu():
    print('''
    1. Add new Artist
    2. Add new Artwork
    3. Search Artwork
    4. Display all Artwork
    5. Availability
    6. Delete Artwork
    Q. Quit
    ''')
    print('Enter a choice: ')
    return(input())

#Add new artist 
def add_new_artist():
    add_new_artist = ui.get_new_artist()
    try:
        add_new_artist.save()
    except:
        ui.message('\n Artist already in the database. \n')


#Add new Artowork 
def add_new_artwork():
    add_new_artwork = ui.get_new_artwork()
    add_new_artwork.save()
    ui.message('\nArtwork already in the database. \n')

# Search for artwork
def searh_artwork():
    search_artwork = ui.ask_question('Enter artwork name: ')
    art = store.get_artwork_by_name(search_artwork)
    ui.show_all_artwork(art)
    
# Display all the artwork in the database
def display_all_Art():
    artworks = store.get_all_artwork()
    ui.show_all_artwork(artworks)

def change_availability():

    pass

# Delete a artwork from the database 
def delete_artwork():
    try:
        artwork_name = ui.get_artwork_by_name()
        artworks = store.get_artwork_by_name(artwork_name)
        artworks.artname.delete()
        print('Artwork deleted succesfully')
    except:
        print('Artwork not found')
    
#Quit the application

def quit_program():
    ui.message('Thanks! Adios. See you Soon. ')


def main():
    while True:
        select = ''
        select = create_menu()
        if select == '1':
            add_new_artist()
        elif select == '2':
            add_new_artwork()
        elif select == '3':
            searh_artwork()
        elif select == '4':
            display_all_Art()
        elif select == '5':
            change_availability()
        elif select == '6':
            delete_artwork()
        elif select == 'q':
            quit_program()
       
            break 
        else:
            print('please enter a valid choice! ')

if __name__ == "__main__":
    main()