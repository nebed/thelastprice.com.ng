from re import sub
from re import compile as recompile
from urllib.parse import urljoin
import os


JUMIA_BASE_URL = os.getenv('JUMIA_BASE_URL', 'https://www.jumia.com.ng')
KONGA_BASE_URL = os.getenv('KONGA_BASE_URL', 'https://konga.com')
KARA_BASE_URL = os.getenv('KARA_BASE_URL', 'http://www.kara.com.ng')
SLOT_BASE_URL = os.getenv('SLOT_BASE_URL', 'https://slot.ng')
JIJI_BASE_URL = os.getenv('JIJI_BASE_URL', 'https://jiji.ng')

def parse_title_jumia(soup):
    '''
    Returns list of titles of products from store
    '''
    titles = soup.find_all("span", class_="name")
    titles[:] = [title.get_text() for title in titles]

    return titles

def latest_title_jumia(soup):
    '''
    Returns list of titles of products from store
    '''
    titles = soup.find_all("span", class_="name")
    titles[:] = [title.get_text() for title in titles]

    return titles

def parse_title_konga(soup):
    '''
    Returns list of titles of products from store
    '''
    titles = []
    titles[:] = [product['name'] for product in soup]

    return titles


def parse_title_kara(soup):
    '''
    Returns list of titles of products from store
    '''
    titles = soup.find_all("h2", class_="product-name")
    titles[:] = [title.a.get('title') for title in titles]

    return titles

def parse_title_slot(soup):
    '''
    Returns list of titles of products from store
    '''
    titles = soup.find_all(class_="mf-product-details-hover")
    titles[:] = [title.h2.get_text() for title in titles]

    return titles

def parse_title_jiji(soup):
    '''
    Returns list of titles of products from store
    '''
    titles=soup.find_all("h4", class_="qa-advert-title b-list-advert__item-title")
    titles[:]=[title.get_text().replace('\n', '').strip() for title in titles]
    
    return titles

def parse_image_jumia(soup):
    '''
    Returns list of images of products from store
    '''
    images = soup.find_all("div", class_="image-wrapper")
    images[:] = [image.img.get('data-src') for image in images]

    return images

def parse_image_konga(soup):
    '''
    Returns list of images of products from store
    '''
    images = []
    images[:] = ["https://www-konga-com-res.cloudinary.com/w_auto,f_auto,fl_lossy,dpr_auto,q_auto/media/catalog/product" + product['image_thumbnail_path'] for product in soup]

    return images

def parse_image_kara(soup):
    '''
    Returns list of images of products from store
    '''
    images = soup.find_all("a", class_="product-image")
    images[:] = [image.img.get('src') for image in images]

    return images

def parse_image_slot(soup):
    '''
    Returns list of images of products from store
    '''
    images = soup.find_all(class_="mf-product-thumbnail")
    images[:] = [image.a.img.get('data-original') for image in images]

    return images

def parse_image_jiji(soup):
    '''
    Returns list of images urls of products from store
    '''
    images=soup.find_all("a", class_="b-list-advert__item-image js-handle-click-ctr")
    images[:]=[image.img.get("data-src") for image in images]
    
    return images

def parse_price_jumia(soup):
    '''
    Returns list of images of products from store
    '''
    prices = soup.find_all("span", class_="price-box ri")
    prices[:] = [price.span.find("span", dir="ltr").get('data-price') for price in prices]

    return prices

def parse_price_konga(soup):
    '''
    Returns list of prices of products from store
    '''
    prices = []
    prices[:] = [product['special_price'] for product in soup]

    return prices

def parse_price_kara(soup):
    '''
    Returns list of prices of products from store
    '''
    prices = soup.select(".regular-price,.special-price")
    #prices = soup.find_all("span", class_="price")
    prices[:] = [ sub(r'[^\d.]', '', price.get_text())  for price in prices]

    return prices

def parse_price_slot(soup):
    '''
    Returns list of prices of products from store
    '''
    prices = soup.find_all('span', class_="woocommerce-Price-amount amount")
    prices[:] = [sub(r'[^\d.]', '', price.get_text()) for price in prices]

    return prices

def parse_price_jiji(soup):
    '''
    Returns list of prices of products from store
    '''
    prices=soup.find_all(class_="b-list-advert__item-price")
    prices[:] = [sub(r'[^\d.]', '', price.get_text()) for price in prices]
    
    return prices

def parse_url_jumia(soup):
    '''
    Returns list of images of products from store
    '''
    urls = soup.find_all("div", class_="sku -gallery")
    urls[:] = [url.a.get('href') for url in urls]

    return urls

def parse_url_konga(soup):
    '''
    Returns list of urls of products from store
    '''
    urls = []
    urls[:] = ["https://www.konga.com/product/" + product['url_key'] for product in soup]

    return urls

def parse_url_kara(soup):
    '''
    Returns list of urls of products from store
    '''
    urls = soup.find_all("h2", class_="product-name")
    urls[:] = [ url.a.get('href')  for url in urls]

    return urls

def parse_url_slot(soup):
    '''
    Returns list of urls of products from store
    '''
    urls = soup.find_all('div', class_="mf-product-thumbnail")
    urls[:] = [url.a.get('href') for url in urls]

    return urls

def parse_url_jiji(soup):
    '''
    Returns list of urls of products from store
    '''
    urls=soup.find_all('a',class_="b-list-advert__item-textblock js-handle-click-ctr")
    urls[:]=[url.get("href") for url in urls]
    
    return urls

#def parse_page_jumia(soup):
    '''
    Returns jumia page with absolute urls for styles and images
    '''
#    return soup

#def parse_page_konga(soup):
    '''
    Returns konga page with absolute urls for styles and images
    '''
#    links = soup.find_all('link')
#   scripts = soup.find_all('script')
#    for div in soup.find_all("div", {'class':'newsletter-popup-container js-newsletter-subscription-popup'}): 
#        div.decompose()
#    for link in links:
#        link['href'] = urljoin(KONGA_BASE_URL,link.get('href'))
#    for script in scripts:
#        script['src'] = urljoin(KONGA_BASE_URL,script.get('src'))



#    return soup

#def parse_page_kara(soup):
    '''
    Returns kara page with absolute urls for styles and images
    '''

#    return soup

#def parse_page_slot(soup):
    '''
    Returns kara page with absolute urls for styles and images
    '''

#    return soup

#def parse_page_jiji(soup):
    '''
    Returns jiji page with absolute urls for styles and images
    '''

#    return soup