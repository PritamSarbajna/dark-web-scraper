
![Black Minimal Business Personal Profile Linkedin Banner](https://github.com/PritamSarbajna/dark-web-scraper/assets/90236635/676a6e65-5be3-4bda-a04c-47162ad14f51)

<div align="center" >
  
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Kali](https://img.shields.io/badge/Kali-268BEE?style=for-the-badge&logo=kalilinux&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Debian](https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white)
![TOR](https://img.shields.io/badge/tor-%237E4798.svg?style=for-the-badge&logo=tor-project&logoColor=white)

</div>


<div align="center">
<a href="https://pypi.org/project/dark-web-scraper" target="_blank">
    <img src="https://img.shields.io/pypi/v/dark-web-scraper?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/dark-web-scraper" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/dark-web-scraper.svg?color=%2334D058" alt="Supported Python versions">
</a>
<a href="http://badges.mit-license.org" target="_blank">
    <img src="http://img.shields.io/:license-mit-blue.svg?style=flat-square)" alt="Supported Python versions">
</a>
  
</div>

## :dart: Usage :

Currently this is only designed to
- Scrape dark web for onion links
- Scrape images from dark web
**Without tor browser**

## :wrench: Current Dependencies:
- Linux [ used debian based distro ]

# :gear: Prerequisite :

#### Enable socks

- Update package lists
```
$ sudo apt update
```

- Install tor package
```
$ sudo apt install tor
```

- Start Tor service
```
$ sudo service tor start
```

- Verify installation status
```
$ sudo service tor status
```
# :books: Tutorial :

### Install using pip

```
$ pip install dark-web-scraper
```

#### 1. Find onion urls from a dark web link

- Request : ```find_onion_links( str )```
- Response: links will be saved in `result.txt`
- Example :
```Python
# Main.py

from dark_web_scraper import find_onion_links
find_onion_links('http://random_url.onion')
```

#### 2. Scrape images on a dark web link

- Request : ```find_images_from_onion_link( str )```
- Response: links will be saved in `result.txt`
- Example :
```Python
# Main.py

from dark_web_scraper import find_images_from_onion_link
find_images_from_onion_link('http://random_url.onion')
```

## :rocket: Features to be added :
- [ ] Scraping videos from dark web sites
- [ ] Object detection in images
- [ ] Sentiment aAnalysis on the webpage contents


## :warning: Disclaimer:

- I don't promote illegality.
- This project is just for educational purposes only/


