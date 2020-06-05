from bs4 import BeautifulSoup
import requests
import SendEmail


def check_price():
    """
    Input:
    URL of product website
    Headers - search 'my user agent' on Google, and copy paste user agent

    Return:
    Price of products and send gmail to user if price's condition has met
    """
    page = requests.get(url, headers=headers)
    html = page.content
    soup = BeautifulSoup(html, 'lxml')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[1:])

    if converted_price < 35:
        SendEmail.sent_price_email()

    print(converted_price)
    print(title.strip())


# Amazon products
url = 'https://www.amazon.com/Disposable-Breathable-Comfortable-Pollution-Protection/dp/B0875S5TWF/ref=sr_1_4?dchild=1&keywords=surgical+mask&qid=1591309055&sr=8-4'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

check_price()
