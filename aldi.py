import requests
import re

resp = requests.get('https://www.aldi-sued.de/de/homepage.html').text

pattern = r'href="(https://prospekt\.aldi-sued\.de/kw[^"]*)"'
match = re.search(pattern, resp)
url = match.group(1)  #
resp = requests.get(url).text

pattern = r'"downloadPdfUrl":\s*"([^"]*)"'
match = re.search(pattern, resp)
url = match.group(1)
print(url)
with open('/tmp/aldi.pdf', 'wb') as f:
    f.write(requests.get(url).content)
