import csv, collections, dictionary

class MusicLibrary:
    def __init__(self, details):
        self.details = []

    def process_file():
        details = []
        with open("DataSample.csv","r") as csvfile:
            reader= csv.DictReader(csvfile)
            for row in reader:
                details.append(dict(row))
            return details

    def get_title(artist, details):
        songs = []
        try:
            for i in range(len(details)):
                if details[i]["Artist"] == artist:
                    songs.append(details[i]["Title"])
            return songs
        except KeyError:
            print("Artist Do not exist!")

    def get_artist(title, details):
        try:
            for i in range(len(details)):
                if details[i]["Title"] == title:
                    return details[i]["Artist"]
        except KeyError:
            print("Unknown Artist!")

    def get_album(title, artist, details):
        if title is None:
            for i in range(len(details)):
                if details[i]["Artist"] == artist:
                    return details[i]["Album"]
        elif artist is None:
            for i in range(len(details)):
                if details[i]["Title"] == title:
                    return details[i]["Album"]
        else: 
            print("Album Not Found!")

    def get_genre(title, details):
        try:
            for i in range(len(details)):
                if details[i]["Title"] == title:
                    return details[i]["Genre"]
        except KeyError:
            print("Unknown Song Title!")

    # def get_length(title, details):
        try:
            for i in range(len(details)):
                if details[i]["Title"] == title:
                    return details[i]["Length"]
        except KeyError:
            print("Unknown Song Title!")
