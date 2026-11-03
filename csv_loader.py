import csv

class CsvLoader:
    def __init__(self, file_name):
        self.file_name = file_name

    def load(self):
        stations = []
        with open(self.file_name, encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                line = row[0]
                number = int(row[1])
                name = row[2]
                stations.append([line, number, name])
                
        return stations