import requests
import json

#will return 40 items after the search
def search(item):
    url = f'https://stockx.com/api/browse?_search={item}'

    headers ={
        'accept': 'application/json',
        'accept-encoding' : 'utf-8',
        'accept-language' : 'en-GB, en; q=0.9',
        'app-platform': 'Iron',
        'referer': 'https://stockx.com/en-gb',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest' : 'empty', 
        'sec-fetch-mode' : 'cors',
        'sec-fetch-site' : 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    file = requests.get(url, headers=headers)
    result = json.loads(file.text)
    return result['Products'] #['Products'][0] will return the first return of the search

