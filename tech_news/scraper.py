import time
import requests
from parsel import Selector
from requests.exceptions import HTTPError, ConnectTimeout, Timeout


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        res = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
            )
        res.raise_for_status()
    except (HTTPError, ConnectTimeout, Timeout):
        return None
    return res.text


# Requisito 2
def scrape_updates(html_content):
    content = Selector(text=html_content)
    hrefs = content.css("a.cs-overlay-link ::attr(href)").getall()
    return hrefs


# Requisito 3
def scrape_next_page_link(html_content):
    content = Selector(text=html_content)
    next_page = content.css("a.next.page-numbers ::attr(href)").get()
    return next_page


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
