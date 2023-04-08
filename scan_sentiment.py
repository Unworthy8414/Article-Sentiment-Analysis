import sys
import requests
import json
from textblob import TextBlob
from tqdm import tqdm
import os

api_key = sys.argv[1]
search_query = sys.argv[2]
search_url = f'https://newsapi.org/v2/everything?q={search_query}&apiKey={api_key}'

try:
    response = requests.get(search_url)
    response.raise_for_status()
    data = response.json()
    articles = [(article['url'], article['title'], article['publishedAt']) for article in data['articles']]
except requests.exceptions.RequestException as e:
    print("Error fetching articles:", e)
    sys.exit(1)

if os.path.exists('articles_data.json'):
    with open('articles_data.json', 'r') as json_file:
        existing_data = json.load(json_file)
else:
    existing_data = []

if not existing_data:
    existing_data = [{'url': '', 'headline': '', 'date': '', 'polarity': 0, 'subjectivity': 0}]

article_data = []
for url, headline, date in tqdm(articles, desc="Analyzing articles"):
    response = requests.get(url)
    content = response.text
    blob = TextBlob(content)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if not any(item['headline'] == headline for item in existing_data):
        entry = {'url': url, 'headline': headline, 'date': date, 'polarity': polarity, 'subjectivity': subjectivity}
        article_data.append(entry)
        existing_data.append(entry)

with open('articles_data.json', 'w') as json_file:
    json.dump(existing_data, json_file)
