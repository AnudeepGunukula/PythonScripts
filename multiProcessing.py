import requests
import multiprocessing


def proxy_leech():
    all_prox = []
    http_proxies = requests.get(
        "https://api.proxyscrape.com:443/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
    http = http_proxies.text
    all_prox.append([i.rstrip() for i in http.split("\n")])
    socks4_proxies = requests.get(
        "https://api.proxyscrape.com:443/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all")
    socks4 = socks4_proxies.text
    all_prox.append([i.rstrip() for i in socks4.split("\n")])
    socks5_proxies = requests.get(
        "https://api.proxyscrape.com:443/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all")
    socks5 = socks5_proxies.text
    all_prox.append([i.rstrip() for i in socks5.split("\n") if ":" in i])
    return all_prox


all_proxies = proxy_leech()
http = all_proxies[0]
socks4 = all_proxies[1]
socks5 = all_proxies[2]
li = []


def check(j):
    pro = {
        'http': 'socks4://'+j,
        'https': "socks4://"+j}
    print("testing "+str(j))
    r = requests.get("https://www.google.com", proxies=pro)
    if "lang=" in r.text:
        print(j+":          success")
        li.append(j)


tlist = []
a = 0
socks4 = socks4[:30]
while True:

    tlist = []
    for i in range(10):
        j = socks4[a]
        a += 1
        try:
            t = multiprocessing.Process(target=check(j))
            tlist.append(t)
        except:
            continue
    for k in tlist:
        k.start()
    for l in tlist:
        l.join()
    if a == 30:
        break

print(li)
