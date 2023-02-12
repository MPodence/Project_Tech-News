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
    content = Selector(text=html_content)
    new = {
        "url": content.css("link[rel='canonical'] ::attr(href)").get(),
        #  https://stackoverflow.com/questions/52849274/getting-the-current-url-page-ref-scrapy
        "title": content.css(".entry-title ::text").get().strip(),
        "timestamp": content.css(
            ".cs-bg-dark > ul > li.meta-date ::text"
        ).get(),
        "writer": content.css("li.meta-author > span.author > a ::text").get(),
        "reading_time": int(content.css(
            "li.meta-reading-time ::text"
        ).get().split(" ")[0]),
        "summary": "".join(content.css(
            "div.entry-content > p:nth-of-type(1) *::text"
        ).getall()).strip(),
        #  https://developer.mozilla.org/pt-BR/docs/Web/CSS/:nth-of-type
        "category": content.css(
            ".cs-bg-dark > div > div > a > span.label ::text"
        ).get()
    }
    return new


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
