import requests

apikey = '4aa36aaf5092402780e7cf1b7230a562'
query = input("Enter the topic you want news about: ")


url = f'https://newsapi.org/v2/everything?q={query}&from=2025-12-29&sortBy=publishedAt&apiKey={apikey}'

r = requests.get(url)

data = r.json()
articles = data['articles']

for index, article in enumerate(articles):
    title = article['title']
    description = article['description']
    url = article['url']
    print(f'Article {index + 1}:\nTitle: {title}\nDescription: {description}\nURL: {url}\n')


# NewAPI link - https://newsapi.org/