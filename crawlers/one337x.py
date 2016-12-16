import requests
from common import fetch_html
from bs4 import BeautifulSoup
from torrent import Torrent


class One337x(object):
    """Crawler for https://1337x.to"""
    def __init__(self):
        super(One337x, self).__init__()
        self.domain = 'https://1337x.to'

    def fetch_torrents(self, search_term):
        # NOTE: For now we are only dealing with page 1
        url = '%s/search/%s/1/' % (self.domain, search_term)
        torrents = self.extract_torrents(url)
        return torrents

    def extract_torrents(self, url):
        def extract_table_rows(html_doc):
            soup = BeautifulSoup(html_doc, 'html.parser')
            table_field = soup.find('table')
            table_body = table_field.findChild('tbody')
            table_rows = table_body.findChildren('tr')
            return table_rows

        def extract_magnet_link(url):
            html_doc = requests.get(url).text
            soup = BeautifulSoup(html_doc, 'html.parser')
            magnet_link = soup.find('ul', class_='download-links').findChild('a', class_='btn-magnet').attrs['href']
            return magnet_link

        def parse_td(row):
            name = row.find('td', class_='coll-1').find('b', class_='highlight').text
            page_url = row.find('td', class_='coll-1').findAll('a')[1].attrs['href']
            page_url = self.domain+page_url
            seeds = row.find('td', class_='coll-2 seeds').text
            leeches = row.find('td', class_='coll-3 leeches').text
            date = row.find('td', class_='coll-date').text
            size = row.find('td', class_='coll-4').contents[0]
            magnet_link = extract_magnet_link(page_url)
            return Torrent(
                name=name,
                seeds=seeds,
                leeches=leeches,
                date=date,
                size=size,
                url=page_url,
                magnet=magnet_link
            )

        html_doc = fetch_html(url)
        table_rows = extract_table_rows(html_doc)
        return map(parse_td, table_rows)
