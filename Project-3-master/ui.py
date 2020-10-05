from artist_artwork_database import Artist, Artwork


def message(msg):
    print(msg)

# Get a new artist asking user for Name and email
def get_new_artist():
    new_artist_name = input('Enter new artist name: ').title()
    new_artist_email = input('Enter new artist email: ')
    print('New artist sucefully added. ')
    return Artist(new_artist_name, new_artist_email)

# getting new artost asking ArtistName, ArtworkName, Price, and Availability
def get_new_artwork():
    artist_name = input('Enter artist name: ').title()
    artwork_name = input ('Enter artwork name: ').title()
    price = float(input('Enter price (EX: 100000): '))
    available = str(input('Enter availability: '))
    print('New artwork successfully added. ')
    return Artwork(artist_name, artwork_name, price, available)
# Show all the artwork 
def show_all_artwork(Artwork):

    if Artwork:
        for artwork in Artwork:
            print(artwork)
        else:
            print('No artwork found. ')
        print()

#Getting artwork using the name of artwork 
def get_artwork_by_name():
    artwork_name = input('Enter artwork name: ').title()
    return artwork_name


def ask_question(question):
    return input(question)







