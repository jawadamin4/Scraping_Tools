import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError


response =requests.get('https://api.github.com')
print(response.status_code)
print(response.json())
print(response.text)
print(response.url)

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
        print('Success!')


url = 'https://www.dawn.com/'
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extracting specific elements from the page
    title = soup.title.text
    paragraphs = soup.find_all('p')

    # Printing the extracted data
    print(f"Title: {title}")
    for paragraph in paragraphs:
        print(paragraph.text)


import grequests

urls = ['https://www.dawn.com/', 'https://urdu.geo.tv/', 'https://urdu.arynews.tv/']
requests = [grequests.get(url) for url in urls]
responses = grequests.map(requests)

for response in responses:
    if response is not None and response.status_code == 200:
        html_content = response.text
        # Process the HTML content of the response
    else:
        print("Error occurred during the request or response is None")

