import requests as req
import sys
import warnings
import time
import threading
from bs4 import BeautifulSoup

# TODO://导出到表格
import csv

logo = '''

 ____ ___        .__  _________ .__                   __                 
|    |   \_______|  | \_   ___ \|  |__   ____   ____ |  | __ ___________ 
|    |   /\_  __ \  | /    \  \/|  |  \_/ __ \_/ ___\|  |/ // __ \_  __ 
|    |  /  |  | \/  |_\     \___|   Y  \  ___/\  \___|    <\  ___/|  | \/
|______/   |__|  |____/\______  /___|  /\___  >\___  >__|_ \___  >__|   
                              \/     \/     \/     \/     \/    \/       

'''

print(logo + "author: m0nk3y")
print("Usage: python3 UrlCheck.py  url_file.txt out_file.txt")
warnings.filterwarnings('ignore')
start = time.time()
headers = {
    'Accept': '*/*',
    'Accept-Language': '*/*',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Connection': 'keep-alive',
    'Referer': 'http://www.baidu.com/'
}

def UrlCheck(url):
    try:
        res = req.get(url, timeout=5, headers=headers, verify=False)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'lxml')
        title = soup.title.string
        if res.status_code == 200:
            print("[+] " + str(res.status_code) + "  " + url + "  " + title)
        if res.status_code == 404:
            print("[-] " + str(res.status_code) + "  " + url + "  " + title)
        if res.status_code == 500:
            print("[-] " + str(res.status_code) + " " + url + "  " + title)
        if res.status_code == 403:
            print("[-] " + str(res.status_code) + " " + url + "  " + title)
        if res.status_code == 405:
            print("[-] " + str(res.status_code) + " " + url + "  " + title)
    except Exception:
        pass



if __name__ == "__main__":
    # main()
    s = sys.argv[1]
    # output = sys.argv[2]
    threads = []
    with open(s, 'r+') as f:
        urls = f.readlines()
        for url in urls:
            if 'http' not in url:
                url = 'https://' + url
            t = threading.Thread(target=UrlCheck, args=(url.strip('\n'),))
            threads.append(t)
        f.close()
    for i in range(0, len(threads)):
        threads[i].start()
    for i in range(0, len(threads)):
        threads[i].join()

    end = time.time()
    print("[+] URL 存活探测完毕，共有" + " 探测总时间 " + str(end - start))
