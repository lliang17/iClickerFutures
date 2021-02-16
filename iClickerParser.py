from bs4 import BeautifulSoup
import re
import pandas as pd

def recode(txt):
    return txt.encode('ascii', 'ignore').strip().decode('utf-8')

def parseprice(txt):
    pricetxts = re.findall("iclicker.*?\$[0-9]+", txt.lower())
    price = []
    if len(pricetxts) == 0: return None
    for i in range(len(pricetxts)):
        price.append(int(pricetxts[i].split("$")[1]))
    return [min(price), max(price)]

def parsedate(txt):
    return

def parse(filename = "source_data.txt"):

    posts = []
    dates = []
    prices = []
    classid = 'sjgh65i0'

    file = open(filename, "r", encoding="utf-8")
    page_source = file.read()
    file.close()

    soup = BeautifulSoup(page_source, 'html.parser')
    rawposts = soup.find_all(attrs = {'class':classid})[::2]

    for i in range(len(rawposts)):
        soupbase = rawposts[i].find(attrs = {'class':"d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 jq4qci2q a3bd9o3v knj5qynh m9osqain"})
        dates.append(recode(str(soupbase.get_text())))
        posts.append(recode(str(soupbase.next_sibling)))
        prices.append(parseprice(recode(str(soupbase.next_sibling))))

    df = pd.DataFrame({'Date':dates,'Price':prices}).dropna()

    df.to_csv("grossdata.csv")

