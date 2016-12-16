class Torrent(object):
    """The domain representation of a Torrent"""
    def __init__(self, name, seeds, leeches, date, size, url, magnet):
        self.name = name
        self.seeds = seeds
        self.leeches = leeches
        self.date = date
        self.size = size
        self.url = url
        self.magnet = magnet
