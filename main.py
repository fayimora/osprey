from crawlers.one337x import One337x


if __name__ == '__main__':
    crawler = One337x()
    torrents = list(crawler.fetch_torrents('arrow'))
