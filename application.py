import os,sys

import requests
import json
import sqlite3
from collections import namedtuple
from re import sub
from bs4 import BeautifulSoup
from flask import Flask, jsonify, render_template, request
from store_functions import *
from flask_cors import CORS



app = Flask(__name__,
            static_folder = "./dist",
            template_folder = ".")
CORS(app)

JUMIA_URL = os.getenv('JUMIA_URL', 'https://www.jumia.com.ng/catalog/?q=')
KONGA_URL = os.getenv('KONGA_URL', 'https://b9zcrrrvom-3.algolianet.com/1/indexes/*/queries')
KARA_URL = os.getenv('KARA_URL', 'http://www.kara.com.ng/catalogsearch/result?q=')
SLOT_URL = os.getenv('SLOT_URL', 'http://slot.ng/?post_type=product&s=')
JIJI_URL= os.getenv('JIJI_URL', 'https://jiji.ng/search?query=')
EMPTY_LIST = []

urls = [JUMIA_URL,KONGA_URL,KARA_URL,SLOT_URL,JIJI_URL]

@app.route('/search/<term>/', methods=['GET'])
def search_products(term=None):
    '''
    Searches online stores using the given term. If no term is given, defaults to recent.
    '''
    #sort_arg = sort_filters[request.args.get('sort')] if sort in sort_filters else ''

    jumiaurl = JUMIA_URL + sub(r"\s+", '+', str(term))
    #kongaurl = KONGA_URL + sub(r"\s+", '%20', str(term))
    karaurl = KARA_URL + str(term)
    sloturl = SLOT_URL + sub(r"\s+", '+', str(term))
    jijiurl= JIJI_URL + sub(r"\s+", '+', str(term)) 
    results = parse_jumia(jumiaurl) + parse_kara(karaurl) + parse_konga(KONGA_URL,term) + parse_slot(sloturl) + parse_jiji(jijiurl)

    return jsonify(results), 200

@app.route('/visitstore/', methods=['GET'])
def visit_store():
    store = request.args.get('store')
    url = request.args.get('url')
    conn = sqlite3.connect('database.db')
    visited_url = conn.execute("SELECT id, times_visited from visited_stores where url = ? LIMIT 1",(url,)).fetchall()
    if len(visited_url) == 0:
        conn.execute("INSERT INTO visited_stores (store,url,times_visited) VALUES (?,?,?)", (store,url,1))
        conn.commit()
    else:
        for row in visited_url:
            conn.execute('UPDATE visited_stores set times_visited = ? where ID = ?',(row[1]+1,row[0]))
            conn.commit()
    conn.close()

    return jsonify(url), 200

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home_page(path):
	return render_template('index.html'),200


#@app.route('/product', methods=['GET'])
#def show_product():
#    url = request.args.get('url')
#    store = request.args.get('store')
#    try:
#        data = requests.get(url).text
#    except requests.exceptions.RequestException as e:  # This is the correct syntax
#        print(e)
#        sys.exit(1)
#    soup = BeautifulSoup(data, 'lxml')
#    parsed_soup = create_local_page(soup,store)
#    with open("templates/product.html", "wb") as f_output:
#        f_output.write(parsed_soup.prettify("utf-8"))

#    return render_template('product.html'), 200


#def create_local_page(soup,STORE):
#    switcher = {
#        'jumia': parse_page_jumia,
#        'konga': parse_page_konga,
#        'kara': parse_page_kara,
#        'slot': parse_page_slot,
#        'jiji': parse_page_jiji
#    }
    # Get the function from switcher dictionary
#    func = switcher.get(STORE, lambda: "Store is not supported yet")
    # Execute the function
#    parsed_soup = func(soup)

#    return parsed_soup


def parse_all(soup,STORE):

    titles = parse_titles(soup,STORE)
    images = parse_images(soup,STORE)
    prices = parse_prices(soup,STORE)
    #ratings = parse_ratings(soup,STORE)
    product_urls = parse_product_urls(soup,STORE)
    source = STORE
    #price_drops = parse_price_drops(soup,STORE)
    search_results = []
    for search_result in zip(titles, images, prices, product_urls):
        search_results.append({
            'title': search_result[0],
            'image': search_result[1],
            'price': search_result[2],
            'url': search_result[3],
            'source': source,
        })
    return search_results


def parse_jumia(url, sort=None):
    '''
    This function parses the page and returns list of products
    '''
    #print(url)
    STORE = "jumia"
    try:
        data = requests.get(url).text
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        sys.exit(1)
    soup = BeautifulSoup(data, 'lxml')
    #print(soup)
    table_present = soup.find('section', {'class': 'products -mabaya'})
    if table_present is None:
        return EMPTY_LIST
    return parse_all(soup,STORE)

def parse_jiji(url, sort=None):
    '''
    This function parses the page and returns list of products
    '''
    #print(url)
    STORE = "jiji"
    try:
        data = requests.get(url).text
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        sys.exit(1)
    soup = BeautifulSoup(data, 'lxml')
    #print(soup)
    table_present = soup.find('div', {'class': 'b-adverts-list-title'})
    if table_present is None:
        return EMPTY_LIST
    return parse_all(soup,STORE)

def parse_kara(url, sort=None):
    '''
    This function parses the page and returns list of products
    '''
    #print(url)
    STORE = "kara"
    try:
        data = requests.get(url).text
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        sys.exit(1)
    soup = BeautifulSoup(data, 'lxml')
    #print(soup)
    table_present = soup.find('ul', {'class': 'searchindex-results'})
    if table_present is None:
        return EMPTY_LIST
    return parse_all(soup,STORE)

def parse_konga(url, term):
    '''
    This function parses the page and returns list of products
    '''
    #print(url)
    STORE = "konga"
    params = {"x-algolia-agent": "Algolia for vanilla JavaScript 3.30.0;react-instantsearch 5.3.2;JS Helper 2.26.1", "x-algolia-application-id": "B9ZCRRRVOM", "x-algolia-api-key": "cb605b0936b05ce1a62d96f53daa24f7"}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','accept': 'application/json','content-type': 'application/x-www-form-urlencoded','Origin': 'https://www.konga.com'}
    data = json.dumps({"requests" : [{"indexName":"catalog_store_konga_price_desc" ,"params":"query=" + sub(r"\s+", '%20', str(term))  }]})
    try:
        response = requests.post(url,headers=headers, params=params, data=data).json()
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        sys.exit(1)
    #n.loads(response['requests'][], object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    soup = response['results'][0]['hits']    
    #print(response)
    #table_present = soup.find('div', {'class': 'ais-InstantSearch__root'})
    return parse_all(soup,STORE)

def parse_slot(url, sort=None):
    '''
    This function parses the page and returns list of products
    '''
    #print(url)
    STORE = "slot"
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'lxml')
    #print(soup)
    table_present = soup.find('div', {'class': 'products-found'})
    if table_present is None:
        return EMPTY_LIST
    return parse_all(soup,STORE)

def parse_titles(soup,STORE):
    switcher = {
        'jumia': parse_title_jumia,
        'konga': parse_title_konga,
        'kara': parse_title_kara,
        'slot': parse_title_slot,
	    'jiji': parse_title_jiji
    }
    # Get the function from switcher dictionary
    func = switcher.get(STORE, lambda: "Store is not supported yet")
    # Execute the function
    titles = func(soup)
    return titles



def parse_images(soup,STORE):
    switcher = {
        'jumia': parse_image_jumia,
        'konga': parse_image_konga,
        'kara': parse_image_kara,
        'slot': parse_image_slot,
	    'jiji': parse_image_jiji
    }
    # Get the function from switcher dictionary
    func = switcher.get(STORE, lambda: "Store is not supported yet")
    # Execute the function
    images = func(soup)
    return images


def parse_prices(soup,STORE):
    switcher = {
        'jumia': parse_price_jumia,
        'konga': parse_price_konga,
        'kara': parse_price_kara,
        'slot': parse_price_slot,
	    'jiji': parse_price_jiji
    }
    # Get the function from switcher dictionary
    func = switcher.get(STORE, lambda: "Store is not supported yet")
    # Execute the function
    images = func(soup)
    return images

def parse_ratings(soup,STORE):

    return

def parse_product_urls(soup,STORE):
    switcher = {
        'jumia': parse_url_jumia,
        'konga': parse_url_konga,
        'kara': parse_url_kara,
        'slot': parse_url_slot,
	    'jiji': parse_url_jiji
    }
    # Get the function from switcher dictionary
    func = switcher.get(STORE, lambda: "Store is not supported yet")
    # Execute the function
    urls = func(soup)
    return urls


def parse_price_drops(soup,STORE):

    return 
@app.route('/latest/', methods=['GET'])
def latest_deals():
    jumiaurl = "https://www.jumia.com.ng/last-price/"
    karaurl = "http://www.kara.com.ng/index.php/deals"
    sloturl = "https://slot.ng"
    jijiurl= "https://jiji.ng"
    results = latest_kara(karaurl) + latest_jumia(jumiaurl) + latest_konga(KONGA_URL) + latest_jiji(jijiurl)

    return jsonify(results), 200

def latest_kara(url, sort=None):
    '''
    This function parses the page and returns list of products
    '''
    #print(url)
    STORE = "kara"
    try:
        data = requests.get(url).text
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        sys.exit(1)
    soup = BeautifulSoup(data, 'lxml')
    #print(soup)
    table_present = soup.find('ul', {'class': 'products-grid'})
    #print(table_present)
    if table_present is None:
        return EMPTY_LIST
    return parse_all(soup,STORE)

def latest_jumia(url, sort=None):
    '''
    This function parses the page and returns list of products
    '''
    #print(url)
    STORE = "jumia"
    try:
        data = requests.get(url).text
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        sys.exit(1)
    soup = BeautifulSoup(data, 'lxml')
    #print(soup)
    table_present = soup.find('section', {'class': 'products -mabaya'})
    #print(table_present)
    #print(soup)
    if table_present is None:
        return EMPTY_LIST
    return parse_all(soup,STORE)


def latest_konga(url, sort=None):
    '''
    This function parses the page and returns list of products
    '''
    #print(url)
    STORE = "konga"
    params = {"x-algolia-agent": "Algolia for vanilla JavaScript 3.30.0;react-instantsearch 5.3.2;JS Helper 2.26.1", "x-algolia-application-id": "B9ZCRRRVOM", "x-algolia-api-key": "cb605b0936b05ce1a62d96f53daa24f7"}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','accept': 'application/json','content-type': 'application/x-www-form-urlencoded','Origin': 'https://www.konga.com'}
    data = json.dumps({"requests" : [{"indexName":"catalog_store_konga" ,"params":"query=" }]})
    try:
        response = requests.post(url,headers=headers, params=params, data=data).json()
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        sys.exit(1)
    #n.loads(response['requests'][], object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    soup = response['results'][0]['hits']    
    #print(response)
    #table_present = soup.find('div', {'class': 'ais-InstantSearch__root'})
    return parse_all(soup,STORE)

def latest_slot(url, sort=None):
    '''
    This function parses the page and returns list of products
    '''
    #print(url)
    STORE = "slot"
    try:
        data = requests.get(url).text
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        sys.exit(1)
    soup = BeautifulSoup(data, 'lxml')
    print(soup)
    table_present = soup.find('div', {'id': 'container'})
    print(table_present)
    if table_present is None:
        return EMPTY_LIST
    return parse_all(soup,STORE)

def latest_jiji(url, sort=None):
    '''
    This function parses the page and returns list of products
    '''
    #print(url)
    STORE = "jiji"
    try:
        data = requests.get(url).text
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        sys.exit(1)
    soup = BeautifulSoup(data, 'lxml')
    #print(soup)
    table_present = soup.find('div', {'class': 'b-adverts-list-title'})
    #print(table_present)
    if table_present is None:
        return EMPTY_LIST
    return parse_all(soup,STORE)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
