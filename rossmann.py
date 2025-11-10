from datetime import date
import requests

# 1. Calculate the year and *next* week
kw = date.today().isocalendar()[1] + 1
year = date.today().isocalendar()[0]

# 2. Create a list of all URLs to try
urls_to_try = [
    f'https://www.rossmann.de/de/kataloge/angebote/catalogs/{year}_kw{kw}_beilage/pdf/complete.pdf', # lowercase 'kw'
    f'https://www.rossmann.de/de/kataloge/angebote/catalogs/{year}_KW{kw}_beilage/pdf/complete.pdf'  # uppercase 'KW'
]

success = False

# 3. Loop through the list and stop after the first success
for url in urls_to_try:
    try:
        print(f"Attempting to download from: {url}")
        resp = requests.get(url)
        
        # This is the key: it raises an error if the status code is 4xx or 5xx (e.g., 404 Not Found)
        resp.raise_for_status()

        # If we get here, the download was successful
        with open('/tmp/rossmann.pdf', 'wb') as f:
            f.write(resp.content)
        
        print(f"Successfully downloaded file.")
        success = True
        break # Exit the loop since we found a working URL

    except requests.exceptions.RequestException as e:
        # This catches connection errors OR the HTTPError from raise_for_status()
        print(f"Failed attempt: {e}")

if not success:
    print("Failed to download the PDF from all attempted URLs.")
