import requests
from bs4 import BeautifulSoup

URL = 'https://www.sahibinden.com/kiralik-is-yeri?hasMap=true&sorting=address_asc&address_quarter=51408&address_quarter=51421&address_quarter=23001&address_quarter=23003&address_quarter=23004&address_quarter=23005&address_quarter=22995&address_quarter=22996&address_town=440&address_city=34'
url_2 = 'https://eksisozluk.com/'
page = requests.get(url_2)

soup = BeautifulSoup(page.content, 'html.parser')

# <div id="ResultsContainer">
#     <!-- all the job listings -->
# </div>

results = soup.find(id='ResultsContainer')
