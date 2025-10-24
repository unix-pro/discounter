import requests
import re

resp = requests.get('https://www.lidl.de/c/online-prospekte/s10005610')
html = resp.text

pattern = r'prospekte/aktionsprospekt-([^/]+)'
match = re.search(pattern, html)

extracted = match.group(1)  # Returns: "13-10-2025-18-10-2025-e8f607"
print(extracted)

url = "https://endpoints.leaflets.schwarz/v4/flyer?flyer_identifier=aktionsprospekt-" + extracted

resp = requests.get(url)
resp = resp.json()
url = resp['flyer']['pdfUrl']
with open('/tmp/lidl.pdf', 'wb') as f:
    f.write(requests.get(url).content)
