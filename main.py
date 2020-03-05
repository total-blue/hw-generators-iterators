import requests, json, hashlib

#1
class Searcher():
    def __init__(self, path):
        self.jsonfile = json.load(open(path))
        self.resfile = open('res.txt', 'a')
        self.shift = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.shift += 1
        if self.shift == len(self.jsonfile):
            raise StopIteration
        name = self.jsonfile[self.shift]['name']['common']
        response = requests.get('https://en.wikipedia.org/w/api.php', {'action': 'opensearch',
                  'search': name,
                  'format': 'json'})
        return self.resfile.write(f'{name}: {response.json()[-1][0]}\n')

#2
def generator(path):
    f = open(path)
    while True:
        line = f.readline()
        if len(line) == 0: break
        hashline = hashlib.md5(line.encode())
        yield hashline.digest()
