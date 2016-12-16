from .common import fetch_html
import re


class Tpb(object):
    """Crawler for the pirate bay"""
    def __init__(self):
        super(Tpb, self).__init__()
        self.domain = 'https://thepiratebay.org'

    def fetch_torrents(search_term):
        url = '%s/search/%s/0/99/0' % (self.domain, search_term)
        torrents = self.extract_torrents(url)
        return torrents

    def extract_torrents(self, url):
        def extract_table_rows(html_doc):
            soup = BeautifulSoup(html_doc, 'html.parser')
            table_field = soup.find('table', id='searchResult')
            table_rows = table_field.findChildren('tr')[1:]  # ignore the header
            return table_rows

        def parse_tr(row):
            name = row.findChild('a', class_='detLink').text
            page_url = row.findChild('a', class_='detLink').attrs['href']
            page_url = self.domain+page_url
            tds = row.findChildren('td')
            seeds = tds[-2]
            leeches = tds[-1]
            date = row.findChild('font', class_='detDesc')
            # pattern = re.compile('')
            size = None
            magnet_link = None

        html_doc = fetch_html(url)
        table_rows = extract_table_rows(html_doc)
        return map(parse_tr, table_rows)
