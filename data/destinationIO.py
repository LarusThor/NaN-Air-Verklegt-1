import csv

class DestinationIO():
    def __init__(self):
        pass

    def read_destination(self):
        dest_list = []
        with open('files\destinations.csv', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dest_list.append(row)
        return dest_list

