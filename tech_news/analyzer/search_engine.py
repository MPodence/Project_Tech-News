from tech_news.database import search_news


# Requisito 7
def search_by_title(title: str):
    data = []
    # https://kb.objectrocket.com/mongo-db/how-to-query-mongodb-documents-with-regex-in-python-362
    # ref para case-insensitive como opção de regex
    news = search_news({"title": {"$regex": title, "$options": 'i'}})
    for new in news:
        data.append((new["title"], new["url"]))
    return data


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category: str):
    data = []
    news = search_news({"category": {"$regex": category, "$options": 'i'}})
    for new in news:
        data.append((new["title"], new["url"]))
    return data
