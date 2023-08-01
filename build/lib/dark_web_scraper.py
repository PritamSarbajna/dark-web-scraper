import os
import re 
import time
import secrets
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib.parse import urljoin, unquote
from langdetect import detect
from langcodes import Language


proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
}

headers = { 'User-Agent': UserAgent().random }



def find_onion_links(url):
    response = requests.get(url, headers=headers, proxies=proxies)

    soup = BeautifulSoup(response.text, 'html.parser')

    text_content = soup.get_text()

    # Regular expression to match words with the last string as ".onion"
    pattern = r"\b\w+\.onion\b"

    # Find matches in the HTML response
    matches = re.findall(pattern, text_content)

    with open('result.txt', 'w') as file:
        # Write each match to the file
        for match in matches:
            file.write(match + '\n')
            
            
            
            
def find_images_from_onion_link(url):
    response = requests.get(url, headers=headers, proxies=proxies)

    soup = BeautifulSoup(response.text, 'html.parser')

    image_tags = soup.find_all('img')

    # Directory to save the images
    if not os.path.exists('static/images'):
        os.makedirs('static/images')


    for image_tag in image_tags:
        try:
            img_url = image_tag['src']

            # Skip the image if it's a SVG
            if img_url.startswith('data:image/svg+xml'):
                continue

            if not img_url.startswith('http'):
                img_url = urljoin(url, img_url)
            img_url = unquote(img_url.split("url=")[-1].split("&")[0])

            # Get a random filename in hexadecimal format
            filename = secrets.token_hex(8) + '.jpg'

            # Download the image
            res = requests.get(img_url, proxies=proxies, headers=headers)
            res.raise_for_status()
            
            # Save the file
            with open(os.path.join('static/images', filename), 'wb') as f:
                f.write(res.content)

            time.sleep(1)

        except Exception as e:
            print('Error downloading image:', str(e))



def detect_onion_link_language(url):
    response = requests.get(url, headers=headers, proxies=proxies)
    # Detect the language code
    lang_code = detect(response.text)
    # Convert the language code to readable format
    return Language(lang_code).display_name()


def is_onion_site_valid(url):
    response = requests.get(url, headers=headers, proxies=proxies)
    
    # Checking if the site is working properly
    if response.status_code == 200:
        return True
    else:
        return False
