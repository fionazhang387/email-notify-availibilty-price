from datetime import datetime
import bs4
from bs4 import BeautifulSoup
import time
import requests
import SendEmail



def status(url, headers):
    """
    Input:
    URL of product website
    Headers - search 'my user agent' on Google, and copy paste user agent

    Returns:
    Availability status of products
    """
    respond = requests.get(url, headers=headers)
    print('HTTP', respond.status_code)
    html = respond.content
    soup = BeautifulSoup(html, 'lxml')
    match = soup.find('div', class_='fulfillment-add-to-cart-button')
    status = match.text
    return status

# Start in 2 hours
# time.sleep(7200)

## valid URL
url0 = 'https://www.bestbuy.com/site/bose-soundlink-revolve-portable-bluetooth-speaker-triple-black/5722719.p?skuId=5722719'
url1 = 'https://www.bestbuy.com/site/bose-soundlink-revolve-portable-bluetooth-speaker-lux-gray/5722717.p?skuId=5722717'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
counter = 0
status_list = []

# Send emails to user if products are available
while True:
    counter += 1
    status_list = [status(url0, headers), status(url1, headers)]  #[Sold out, Sold out, Add to Cart] could be one of the examples
    time.sleep(1)
    print(datetime.now())

    body = "Triple Black is {0}, Lux Gray is {1}".format(status_list[0], status_list[1]) # Sold Out, Add to Cart, Check Stores
    print(body)

    print('Number of visit: {0}\n'.format(counter))

    if 'Add to Cart' in status_list:
        SendEmail.sent_status_email()

    # re-check after 2 hours
    time.sleep(7200)
