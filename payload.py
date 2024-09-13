import requests
from bs4 import BeautifulSoup

def get_payload_and_keyword():
    x = requests.get('https://www.google.com/recaptcha/api/fallback?k=6LewPtQSAAAAAIvk6kmw1mVSYVUvd2Ev5MpenlHk').text

    soup = BeautifulSoup(x, 'html.parser')

    image_src = soup.find('img', class_='fbc-imageselect-payload')['src']
    url = 'https://google.com' + image_src

    kword = soup.find('label', class_='fbc-imageselect-message-text')

    return url, kword.find('strong').text