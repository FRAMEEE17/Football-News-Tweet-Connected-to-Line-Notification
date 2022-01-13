#twitter.py
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time

#check system
import sys
print(sys.version)

#webTester
driverpath = r'C:\Users\User\Desktop\TWITTER\DRIVER\chromedriver.exe'

#hide gg chrome
opt = webdriver.ChromeOptions()
opt.add_argument('headless')
driver = webdriver.Chrome(driverpath,options=opt)

def Tweet(twitter_name):
    url = 'https://twitter.com/{}'.format(twitter_name)
    driver.get(url)
    time.sleep(3)
    '''
    #scrolling
    pixel = 0
    for i in range(3):
        driver.execute_script("window.scrollTo(0,{})".format(pixel))
        time.sleep(3)
        pixel = pixel + 1000
    '''
    page_html = driver.page_source
    data = soup(page_html, 'html.parser')
    posts = data.find_all('span',{'class':'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})

    #showonlytext
    dot = False
    allpost = []
    for p in posts:
        txt = p.text
        if dot == True:
            allpost.append(txt)
            #print(txt)
            #print('-----------------')
            dot = False
        if txt == '·':
            dot = True
    return allpost

from songline import Sendline
token = 'put my token here'
messenger = Sendline(token)

#checktwitter = ['FabrizioRomano','Transferzone00','NizaarKinsella','MarcelloChirico','ActualiteBarca','DiMarzio','sistoney67','SamLee','TheAthleticUK','TeleFootball','AbsoluteChelsea','Matt_Law_DT','SJohnsonSport','samuelluckhurst']
checktwitter = ['FabrizioRomano','NizaarKinsella','Matt_Law_DT']
for ct in checktwitter:
    texttoline = ''
    post = Tweet(ct)
    #print(post)
    print('---------------{}-------------'.format(ct))
    texttoline += '---------------{}----------------\n'.format(ct)
    for p in post:
        print(p)
        texttoline += p + '\n\n'
        print('=====')
        
    messenger.sendtext(texttoline)
driver.close()
