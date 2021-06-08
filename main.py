import bs4
import requests
import re


def get_site_links(url):
    res = requests.get(url)
    if res.raise_for_status() is False:
        raise(Exception("invalid url"))

    soup = bs4.BeautifulSoup(res.text,  'html.parser')

    return [
        link.get('href')
        for link in soup.findAll('a', attrs={'href': re.compile("^https://")})
    ]
