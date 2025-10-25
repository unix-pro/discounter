from datetime import date
import requests

kw = date.today().isocalendar()[1] + 1
year = date.today().isocalendar()[0]

url = f'https://www.rossmann.de/de/kataloge/aktion/catalogs/{year}_kw{kw}_aktion/pdf/complete.pdf'

try:
    resp = requests.get(url)
    with open('/tmp/rossmann.pdf', 'wb') as f:
        f.write(resp.content)
except Exception as e:
    print(str(e))
