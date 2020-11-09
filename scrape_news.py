import pandas as pd
import time
from splinter import Browser
from bs4 import BeautifulSoup as bs


def init_browser():
    executable_path = {"executable_path": "/Users/stuhu/.wdm/drivers/chromedriver/win32/86.0.4240.22/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()
    
# Fox News
    url = "https://www.foxnews.com/us"
    url1 = "https://www.foxnews.com"
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    results1 = soup.find_all('article', class_='article story-1')
    results2 = soup.find_all('article', class_='article story-2')
    title_find1 = results1[0].find('h2', class_='title').a.text
    title_find2 = results1[1].find('h2', class_='title').a.text
    title_find3 = results2[0].find('h2', class_='title').a.text
    content_find1 = results1[0].find('p', class_='dek').a.text
    content_find2 = results1[1].find('p', class_='dek').a.text
    content_find3 = results2[0].find('p', class_='dek').a.text
    img_find1 = results1[0].find('img')['src']
    img_find2 = results1[1].find('img')['src']
    img_find3 = results2[0].find('img')['src']
    link_find1 = results1[0].find('a')['href']
    link_1 = url1 + link_find1
    link_find2 = results1[1].find('a')['href']
    link_2 = url1 + link_find2
    link_find3 = results2[0].find('a')['href']
    link_3 = url1 + link_find3

# OANN
    url = "https://www.oann.com/"
    url1 = "https://www.oann.com/"
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    results = soup.find_all('article')
    oann_img1 = results[0].a.img['src']
    oann_link1 = results[0].find('h3').a['href']
    oann_title1 = results[0].find('h3').a.text
    oann_img2 = results[1].a.img['src']
    oann_link2 = results[1].find('h3').a['href']
    oann_title2 = results[1].find('h3').a.text
    oann_img3 = results[2].a.img['src']
    oann_link3 = results[2].find('h3').a['href']
    oann_title3 = results[2].find('h3').a.text
    oann_img4 = results[3].a.img['src']
    oann_link4 = results[3].find('h3').a['href']
    oann_title4 = results[3].find('h3').a.text
    oann_img5 = results[4].a.img['src']
    oann_link5 = results[4].find('h3').a['href']
    oann_title5 = results[4].find('h3').a.text

# NewsMax
    url = "https://www.newsmax.com"
    url1 = "https://www.newsmax.com/us/"
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    results = soup.find('center')
    newsmax_link = url + results.find('a')['href']
    newsmax_img = url + results.find('a').img['src']
    newsmax_title = results.find('a').img['alt']
    browser.visit(url1)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    results = soup.find_all('li', class_="article_link")
    nmusa_link1 = url + results[0].a['href']
    nmusa_img1 = url + results[0].img['src']
    nmusa_title1 = results[0].a.text
    nmusa_link2 = url + results[1].a['href']
    nmusa_img2 = url + results[1].img['src']
    nmusa_title2 = results[1].a.text
    nmusa_link3 = url + results[2].a['href']
    nmusa_img3 = url + results[2].img['src']
    nmusa_title3 = results[2].a.text
    nmusa_link4 = url + results[3].a['href']
    nmusa_img4 = url + results[3].img['src']
    nmusa_title4 = results[3].a.text

# Brietbart
    url = "https://www.breitbart.com"
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    results = soup.find('section', class_="top_article_main")
    br_title = results.find('h2').a.text
    br_img = results.find('img')['src']
    br_link = url + results.find('h2').a['href']
    br_excerpt = results.find('div', class_="excerpt").p.text
    results = soup.find('section', class_='featured_side')
    articles = results.find_all('article')
    br_title1 = articles[0].h2.a.text
    br_link1 = url + articles[0].h2.a['href']
    br_title2 = articles[1].h2.a.text
    br_link2 = url + articles[1].h2.a['href']
    br_title3 = articles[2].h2.a.text
    br_link3 = url + articles[2].h2.a['href']
    br_title4 = articles[3].h2.a.text
    br_link4 = url + articles[3].h2.a['href']

    # store data in a dictionary
    listings = {
        "title_find1": title_find1,
        "content_find1": content_find1,
        "img_find1": img_find1,
        "link_1": link_1,
        "title_find2": title_find2,
        "content_find2": content_find2,
        "img_find2": img_find2,
        "link_2": link_2,
        "title_find3": title_find3,
        "content_find3": content_find3,
        "img_find3": img_find3,
        "link_3": link_3,
        "oann_img1": oann_img1,
        "oann_link1": oann_link1,
        "oann_title1": oann_title1,
        "oann_img2": oann_img2,
        "oann_link2": oann_link2,
        "oann_title2": oann_title2,
        "oann_img3": oann_img3,
        "oann_link3": oann_link3,
        "oann_title3": oann_title3,
        "oann_img4": oann_img4,
        "oann_link4": oann_link4,
        "oann_title4": oann_title4,
        "oann_img5": oann_img5,
        "oann_link5": oann_link5,
        "oann_title5": oann_title5,
        "newsmax_title": newsmax_title,
        "newsmax_img": newsmax_img,
        "newsmax_link": newsmax_link,
        "nmusa_title1": nmusa_title1,
        "nmusa_img1": nmusa_img1,
        "nmusa_link1": nmusa_link1,
        "nmusa_title2": nmusa_title2,
        "nmusa_img2": nmusa_img2,
        "nmusa_link2": nmusa_link2,
        "nmusa_title3": nmusa_title3,
        "nmusa_img3": nmusa_img3,
        "nmusa_link3": nmusa_link3,
        "nmusa_title4": nmusa_title4,
        "nmusa_img4": nmusa_img4,
        "nmusa_link4": nmusa_link4,
        "br_title": br_title,
        "br_img": br_img,
        "br_link": br_link,
        "br_excerpt": br_excerpt,
        "br_title1": br_title1,
        "br_link1": br_link1,
        "br_title2": br_title2,
        "br_link2": br_link2,
        "br_title3": br_title3,
        "br_link3": br_link3,
        "br_title4": br_title4,
        "br_link4": br_link4
    }

    # quit the browser after scraping
    browser.quit()

    # return results
    return listings