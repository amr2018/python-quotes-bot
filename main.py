
# python quotes bot

import requests
import random
import pyttsx3
from time import sleep
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
quotes = []

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_quotes():
    res = requests.get(url)
    html = BeautifulSoup(res.content, 'html.parser')
    for q in html.findAll('span', {'class': 'text'}):
        quotes.append(q.text)

get_quotes()

def start_bot():
    sleep(5)
    
    q = random.choice(quotes)
    print(q)
    say(q)
    start_bot()

sleep(2)
start_bot()
