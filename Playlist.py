import random

class Playlist:
    def __init__(self, playlist):
        self.playlist = playlist

    def create_playlist(name):
        try:
            playlistname = name
            with open(playlistname,"w") as txtfile:
                txtfile.write(playlistname+":,")
            print("Playlist is Successfully Created!")
        except TypeError:
            print("Enter a Valid Name!")

    def add_song(name, title, details):
        for i in range(len(details)):
            if details[i]['Title'] == title:
                with open(name, "r") as txtfile:
                    info = txtfile.read()
                    if info.count(title) <1:
                        with open(name,"a") as oldfile:
                            oldfile.write(title+",")
                        print("Song is Successfully Added!")
                    else:
                        print("Song is already added!")

    def remove_song(name, title, details):
        for i in range(len(details)):
            if details[i]['Title'] == title:
                with open(name, "r") as txtfile:
                    info = txtfile.read()
                    print(info.count(title))
                    if info.count(title) ==1:
                        newplaylist = info.strip(title+",")
                        with open(name, "w") as oldfile:
                            oldfile.write(newplaylist)
                        print("Song is Successfully Removed!")
                    else:
                        print("Song is not found!")

    def reorder_songs(name, details):
        neworder = []
        with open(name, "r") as txtfile:
            order = (txtfile.read().strip(name+":,")).split(",")
            orderr = order *2
            for i in range(len(order)):
                neworder.append(orderr[(i+1)])
        print("The new playlist is: ")
        print(neworder)

    def display_playlist(name):
        try: 
            with open(name, "r") as txtfile:
                print(txtfile.read())
        except FileNotFoundError:
            print("Playlist Not found!")
