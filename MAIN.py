from MusicLibrary import *
from Song import *
from Playlist import *

def main():
    details = MusicLibrary.process_file()
    print("Please Enter a Number!")
    Options = input("1:Song / 2:MusicLibrary / 3:Playlist"+"\n"+"Here: ")

    if Options == "1":
        print("Please Enter a Number!")
        Option = input("1:Add Song / 2:Remove Song"+"\n"+"Here: ")
        if Option == "1":
            title = input("Enter Song Title: ")
            artist = input("Enter Artist Name: ")
            album = input("Enter Album Name: ")
            genre = input("Enter Genre of Music: ")
            length = input("Enter Length of the Song: ")
            Song.add_song(title, artist, album, genre, length, details)
        elif Option == "2":
            title = input("Enter Song Title: ")
            Song.remove_song(title, details)
        else:
            print("Invalid")

    elif Options == "2":
        print("Please Enter a Number!")
        print("1:Get Title / 2:Get Artist")
        Option = input("3:Get Album / 4:Get Genre"+"\n"+"Here: ")
        if Option == "1":
            artist = input("Enter Artist Name: ")
            MusicLibrary.get_title(artist, details)
        elif Option == "2":
            title = input("Enter Song Title: ")
            MusicLibrary.get_artist(title, details)
        elif Option == "3":
            title = input("Enter Song Title: ")
            artist = input("Enter Artist Name: ")
            MusicLibrary.get_album(title, artist, details)
        elif Option == "4":
            title = input("Enter Song Title: ")
            MusicLibrary.get_genre(title, details)
        else:
            print("Invalid")

    elif Options == "3":
        print("Please Enter a Number!")
        print("1:Create Playlist / 2:Add Song / 3:Remove Song")
        Option = input("4:Reorder Songs / 5:Display Playlist"+"\n"+"Here: ")
        if Option == "1":
            name = input("Enter the Name of thhe Playlist: ")
            Playlist.create_playlist(name)
        elif Option == "2":
            name = input("Enter the Name: ")
            title = input("Enter the Title: ")
            Playlist.add_song(name, title, details)
        elif Option == "3":
            name = input("Enter the Name: ")
            title = input("Enter the Title: ")
            Playlist.remove_song(name, title, details)
        elif Option == "4":
            name = input("Enter the Name: ")
            Playlist.reorder_songs(name, details)
        elif Option == "5":
            name = input("Enter the Name of the Playlist: ")
            Playlist.display_playlist(name)
        else:
            print("Invalid")

main()
