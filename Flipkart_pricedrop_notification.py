import requests
from bs4 import BeautifulSoup
import time
import smtplib
dic = {}
oldcost = 0
count = 1
olddict = {}
oldavail = {}
availdic = {}
lin = {}


def send_mail(subject, body):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("sendermail@gmail.com", "password")
    msg = f"Subject : {subject}\n\n{body}"
    server.sendmail(
        'sendermail@gmail.com', 'recivermail@gmail.com',
        msg
    )
    print("EMAIL HAS SENT")
    server.quit()


while True:

    try:
        links = ["https://www.flipkart.com/redmi-k20-pro-flame-red-128-gb/p/itmfg7uysw6gs55a", "https://www.flipkart.com/redmi-k20-pro-glacier-blue-128-gb/p/itmfgfjthe3dyjp3", "https://www.flipkart.com/realme-x2-pro-lunar-white-128-gb/p/itma3203d88190a3", "https://www.flipkart.com/iqoo-3-tornado-black-128-gb/p/itm7d075bc17be11", "https://www.flipkart.com/lg-g8x-black-128-gb/p/itme8a4f5f473aa4", "https://www.flipkart.com/realme-x3-arctic-white-128-gb/p/itm325a6e0c17b0a", "https://www.flipkart.com/realme-x3-glacier-blue-128-gb/p/itm325a6e0c17b0a",
                 "https://www.flipkart.com/realme-x2-pro-lunar-white-128-gb/p/itma3203d88190a3", "https://www.flipkart.com/realme-x2-pro-neptune-blue-128-gb/p/itma3203d88190a3", "https://www.flipkart.com/realme-x3-superzoom-arctic-white-128-gb/p/itm7e4d21f06e37e", "https://www.flipkart.com/realme-x3-superzoom-glacier-blue-128-gb/p/itm7e4d21f06e37e", "https://www.flipkart.com/realme-7-pro-sun-kissed-leather-128-gb/p/itm72f96fb9b13c3", "https://www.flipkart.com/nike-nk-sportswear-elemental-backpack-21-l-laptop/p/itm9a37689db11e1", "https://www.flipkart.com/skybags-komet-01-laptop-backpack-e-black-26-l/p/itmfggqfh4mzssan", "https://www.flipkart.com/tommy-hilfiger-biker-club-alaska-23-6-l-medium-laptop-backpack/p/itmf3um9rmj9fpdw", "https://www.flipkart.com/tommy-hilfiger-joshua-30-l-laptop-backpack/p/itmfdwhavhwt2bzf", "https://www.flipkart.com/tommy-hilfiger-connor-23-l-laptop-backpack/p/itmfegbctr3qxet3"]
        for url in links:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.text, "html.parser")
            avail = soup.find(class_="_16FRp0")
            if avail == None:
                avail = "available"
            else:
                avail = "NOT available"
            title = soup.find(class_="B_NuCI").text
            title = str(title)
            x = title.replace(" ", "")
            x = x.replace("\xa0", "")
            title = x+" fk"
            price = soup.find(class_="_30jeq3 _16Jk6d").text
            cost = price[1:]
            cost = int("".join(cost.split(",")))
            dic[title] = cost
            availdic[title] = avail
            if count == 1:
                olddict[title] = oldcost
                oldavail[title] = "NOT available"
                lin[title] = url

        count += 1
        print("checking for "+str(count)+"th time")

        for i in dic:
            if dic[i] > olddict[i]:
                olddict[i] = dic[i]
                bod = "price increased for "+i+"old price is " + \
                    str(olddict[i])+", new price is " + \
                    str(dic[i])+"\ncheck "+lin[i]
                sub = "price increased"
                print(bod)
                send_mail(sub, bod)

            elif dic[i] == olddict[i]:
                pass
            else:
                bod = "price dropped for "+i+"old price is " + \
                    str(olddict[i])+", new price is " + \
                    str(dic[i])+"\ncheck "+lin[i]
                olddict[i] = dic[i]
                sub = "price dropped"
                print(bod)
                send_mail(sub, bod)
        for i in availdic:
            if len(availdic[i]) < len(oldavail[i]):
                print(i+" available now ")
                oldavail[i] = availdic[i]
                sub = "item available"
                bod = i+" is available check once, with price:" + \
                    str(dic[i])+"\ncheck "+lin[i]
                print(bod)
                send_mail(sub, bod)
            elif len(availdic[i]) == len(oldavail[i]):
                pass
            else:
                print(i + " item is not available now")
                sub = "item not available"
                bod = i+" is not available check once, with price:" + \
                    str(dic[i])+"\ncheck "+lin[i]
                print(bod)
                send_mail(sub, bod)
                oldavail[i] = availdic[i]
        print("sleeping for 30 minutes")
        time.sleep(30*60)
    except:
        continue
