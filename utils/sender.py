import sys

import requests

token = '6816947635:AAHWpTXDNNSzoysOCgRr5kvJoAUB1Y_T8CI'

request = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={sys.argv[1]}&text={sys.argv[2]}"
requests.get(request)
