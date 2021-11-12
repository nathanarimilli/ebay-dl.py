import argparse
import requests
from bs4 import BeautifulSoup
import json

def parse_itemssold(text):
    '''
    Takes as input a string and returns number of items sold from string
    >>> parse_itemssold('38 sold')
    38
    >>> parse_itemssold('14 watchers')
    0
    >>> parse_itemssold('Almost gone')
    0
    '''
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in text:
        return int(numbers)
    else:
        return 0

def parse_price(text):
    '''
    Takes an input string and returns price in cents as an int value
    >>> parse_price('$14.19')
    1419
    >>> parse_price('$0.99')
    99
    >>> parse_price('$24.36 to $141.04')
    2436
    >>> parse_price('$121.42')
    12142
    >>> parse_price('Free Shipping')
    0
    '''
    #for 'free shipping' etc:
    if '$' not in text:
        return 0
    #extract numbers
    symbol = text.find('$')
    end = text.find(' ')
    text_relevant = text[symbol:end] if end != -1 else text[symbol:]
    numbers = ''
    for char in text_relevant:
        if char in '1234567890':
            numbers += char
    return int(numbers)
    
        





if __name__ == '__main__':
    #get command line arguments
    parser = argparse.ArgumentParser(description='Download information from ebay and convert to JSON.')
    parser.add_argument('search_term')
    parser.add_argument('--num_pages', default = 10)
    args = parser.parse_args()
    print('args.search_term=', args.search_term)

    # empty variable for list of items found on all web pages
    items = []

    #loop over ebay pages
    for page_number in range(1, int(args.num_pages)+1):
        #url building
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw='
        url += args.search_term 
        url += '&_sacat=0&rt=nc&_pgn=' 
        url += str(page_number)
        print('url=', url)

        #downloading html
        r = requests.get(url)
        status = r.status_code
        print('status=', status)
        html = r.text

        # html bs4 processing
        # needed info: --
        soup = BeautifulSoup(html, "html.parser")
        #loop over all items in page
        tags_items = soup.select('.s-item')
        for tag_item in tags_items:

            name = None
            tags_name = tag_item.select('.s-item__title')
            for tag in tags_name:
                name = tag.text

            freereturns = False
            tags_returns = tag_item.select('.s-item__free-returns')
            for tag in tags_returns:
                freereturns = True


            
            price = None
            tags_price = tag_item.select('.s-item__price')
            for tag in tags_price:
                price = parse_price(tag.text)

            
            condition = None
            tags_status = tag_item.select('.SECONDARY_INFO')
            for tag in tags_status:
                condition = tag.text

            
            shipping = 0
            tags_shipping = tag_item.select('.s-item__shipping')
            for tag in tags_shipping:
                shipping = parse_price(tag.text)


            items_sold = None
            tags_itemssold = tag_item.select('.s-item__hotness')
            for tag in tags_itemssold:
                items_sold = parse_itemssold(tag.text)

            #make library
            item = {
                'name': name,
                'free_returns': freereturns,
                'items_sold': items_sold,
                'status': condition,
                'price': price,
                'shipping': shipping
            }
            items.append(item)

          
        #status-monitoring print statements
        print('len(tag_items)=', len(tags_items))
        print('len(items)=', len(items))
        #for item in items:
        #    print('item=', item)



    #write the json file
    filename = args.search_term+'.json'
    with open(filename, 'w', encoding='ascii') as f:
        f.write(json.dumps(items))