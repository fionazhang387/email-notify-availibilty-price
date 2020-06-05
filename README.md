# email-notify-availibilty-price
This repository helps to automate tracking and sending notification emails when an online product is available or prices has changed.

Python: Version 3.7

Virtual Environment:
$ pip install beautifulsoup4
$ pip install bs4
$ pip install lxml
$ pip install smtplib
$ pip install requests

## Files
### main_status.py
It shows abilitiesities status of the Bose SoundLink Bluetooth Speaker on Bestbuy website, and send out emails to notify when it is available.

### main_price.py
It shows the price of Disposable Surgical Mask on Amazon, and send out emails to notify when the price is falling.

### SendEmail.py
This file contains customized modules. The functions generate emails and send from a specific gmail user to a specific gmail user with notification contents.
