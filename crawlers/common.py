import requests


def fetch_html(url):
    html_doc = requests.get(url).text
    return html_doc
