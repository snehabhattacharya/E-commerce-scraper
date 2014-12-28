from urlparse import urlparse
from bs4 import BeautifulSoup
import re
import urllib2,urllib
rating=[]
price=[]
t=[]
class Gadjets:

    def __init__(self,product):
        self.product=product
        self.flipkart()
        self.amazon()
        self.snapdeal()


    def parse_url(self,url):
        hdr = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}
        req = urllib2.Request(url,headers=hdr)
        res = urllib2.urlopen(req)

        data=res.read()
        soup=BeautifulSoup(data,"lxml")
        return soup


    def flipkart(self):
        
        k=self.product
        k=urllib.quote(k)
        url="http://www.flipkart.com/mobiles/pr?q=" + str(k) + "&as=on&as-show=on&otracker=start&sid=tyy%2C4io&as-pos=1_1_ic_" + str(k)
        soup=self.parse_url(url)
        
        print "Flipkart"
        print ""
        
        var1= soup.find_all('div', 'gd-col gu3')
        for e in var1:
            status= e.find('a','pu-status oos fk-uppercase fk-font-11')
            if not status:
                rating.append(e.find('div' , 'pu-rating'))
                price.append(e.find('div', 'pu-price'))
                t.append(e.find('a',"fk-display-block"))


        '''print "no"
        if not e.find('a', 'pu-status oos fk-uppercase fk-font-11'):
            print (e.find('div' , 'pu-rating').text).strip()
            print (e.find('div', 'pu-price').text).strip()
            print (e.find('a',"fk-display-block").text).strip()
        else:
            print "nj"
        '''

        
        self.display(t,rating,price)

    

    def amazon(self):
        
        k=self.product
        k=urllib.quote(k)
        url="http://www.amazon.in/s/ref=nb_sb_noss_1?url=node%3D1389432031&field-keywords="+str(k)+ "&rh=n%3A976419031%2Cn%3A1389401031%2Cn%3A1389432031%2Ck%3A" + str(k)
        soup=self.parse_url(url)
        print ""
        print "Amazon"
        print ""
        container=soup.find_all('div', {'class' : 's-item-container'})
        #print container
        for e in container:
            title=e.find('h2', {'class' : 'a-size-base s-inline s-access-title a-text-normal'})
            #print (title.text)
            if self.product in (title.text).strip():
                t.append(title)
                r=e.find('i', 'a-icon a-icon-star a-star-4-5')
                if r:
                    rating.append(r) 
                p=e.find('span', 'a-size-base a-color-price s-price a-text-bold')
                if p:


                    price.append(p)

            
        


        #rating=soup.find_all('i', {"class" : "a-icon a-icon-star a-star-4-5"})
        #price=soup.find_all('span' , {"class" : 'a-size-base a-color-price s-price a-text-bold'})
        self.display(t,rating,price)

    def snapdeal(self):
        
        k=self.product
        k=urllib.quote(k)
        url ="http://www.snapdeal.com/search?keyword="+str(k)+"&santizedKeyword=&catId=&categoryId=175&suggested=true&vertical=p&noOfResults=20&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&url=&utmContent=&catalogID=&dealDetail="
        soup=self.parse_url(url)
        print ""
        print "Snapdeal"
        print ""
        
        container = soup.find_all('div', 'product_grid_box')
        for e in container:
            title= e.find('div', 'product-title')
            if self.product in (title.text).strip():
                t.append(title)
                r=e.find('div', 'ratingStarsSmall')
                rating.append(r)
                p=e.find('div', 'product-price')
                price.append(p)
        #title=soup.find_all('div', {'class' : 'product-title'})
        #rating=soup.find_all('div', {'class' : 'ratingStarsSmall'})
        #price=soup.find_all('div', {'class' : 'product-price'})
        
        self.display(t,rating,price)

    def display(self,title,rating,price):
        for (i,j,k) in zip(title,rating,price):
            print (i.text).strip() + " " + (j.text).strip() + " " + (k.text).strip()

prod=raw_input("enter product")
Gadjets(prod)
