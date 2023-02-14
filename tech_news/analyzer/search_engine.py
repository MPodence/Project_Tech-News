from tech_news.database import search_news
from datetime import datetime


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
    try:
        data = []
        formated_date = datetime.strptime(
            date, '%Y-%m-%d').strftime('%d/%m/%Y')
        # https://www.programiz.com/python-programming/datetime/strftime
        # ref do funcionamento do strftime para formatar a data
        news = search_news({"timestamp": formated_date})
        for new in news:
            data.append((new["title"], new["url"]))
        return data
    except Exception:
        raise ValueError('Data inválida')


# Requisito 9
def search_by_category(category: str):
    data = []
    news = search_news({"category": {"$regex": category, "$options": 'i'}})
    for new in news:
        data.append((new["title"], new["url"]))
    return data
