import csv, dictionary, collections

class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length
    
    def add_song(title, artist, album, genre, length, details):
        try:
            newsong = {'Title': title, 'Artist': artist, 'Album': album, 'Genre': genre, 'Length': length}
            details.append(newsong)
            with open("DataSample.csv","w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=details[0].keys())
                writer.writeheader()
                for row in details:
                    writer.writerow(row)
            print("Song is Successfully Added!")
        except TypeError:
            print("Please fill in all details!")

    def remove_song(title, details):
        try:
            for i in range(len(details)):
                if details[i]['Title'] == title:
                    artist = details[i]['Artist']
                    album = details[i]['Album']
                    genre = details[i]['Genre']
                    length = details[i]['Length']
            remsong = {'Title': title, 'Artist': artist, 'Album': album, 'Genre': genre, 'Length': length}
            details.remove(remsong)
            with open("DataSample.csv","w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=details[0].keys())
                writer.writeheader()
                for row in details:
                    writer.writerow(row)
            print("Song is Successfully Removed!")
        except TypeError:
            print("Please fill in all details!")
