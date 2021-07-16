import lyricsgenius as lg
file = open("C:/Users/ankita upadhyay/Documents/Python/Python codes/2021/Lyrics Extractor/lyrics_text.txt", "w")

#we created this text file to store lyrics of the songs extracted
#songs lyrics were extracted with the help of api

#genius = lg.Genius('Client_Access_Token_Goes_Here', skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

#you will gwt client access token after setting up a new api cleint
#i did mine using https://genius.com
#reference: https://towardsdatascience.com/song-lyrics-genius-api-dcc2819c29

genius = lg.Genius('WQMOj3Gii193wxHpYGrLeRgwpjjqztOZph2byk33Zy-nxynv6q1UPxUvZa-VWHDU', skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

artists = ['Chainsmokers', 'Ariana Grande-Butera', 'Selena Gomez']
#artists = ['Logic', 'Rihanna', 'Frank Sinatra']

#Enter the name of artists you want to extract songs of

def get_lyrics(arr, k):
    c=0
    for name in arr:
        try:
            songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
            #get top popular songs of the following artist
            s = [song.lyrics for song in songs]
            file.write("\n\n <|endoftext|> \n \n".join(s))
            #write song lyrics in text file
            c += 1
            print(f"Songs grabbed: {len(s)}")
            #if song is found
        except :
            print(f"some exceptions at {name}: {c}")
            #if song is not found

get_lyrics(artists, 5) #here 5 is the amount of songs you want from 1 artist 