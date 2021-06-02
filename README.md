# pararius

Python library to get information about houses from [pararius.nl](https://www.pararius.nl/).

**DISCLAIMER**: this is not an official API and doesn't use one. The script is provided as is (see the LICENSE) and for personal usage only. Please, contact the pararius team (Real Estate Classifieds BV) if you need a stable API for extensive or commercial usage.

## Installation

```bash
python3 -m pip install pararius
```

## Usage

```python
import pararius
search_url = 'https://www.pararius.nl/koopwoningen/nederland/bestaande-bouw/huis'
urls = pararius.get_urls(search_url)
for url in urls:
    info = pararius.get_info(url)
    print(info)
```

Output example (anonymized, just in case):

```python
{'@context': 'http://schema.org/',
 '@id': 'https://www.pararius.nl/huis-te-koop/schiedam/.../...',
 '@type': ['House', 'Product'],
 'address': {
    '@type': 'PostalAddress',
    'addressLocality': 'Schiedam',
    'addressRegion': '...',
    'postalCode': '...',
    'streetAddress': '...'},
 'description': '...',
 'floorSize': {'@type': 'QuantitativeValue', 'unitText': 'MTK', 'value': 115},
 'image': 'https://casco-media-prod.global.ssl.fastly.net/...',
 'name': '...',
 'numberOfRooms': [{
    '@type': 'QuantitativeValue',
    'unitText': 'kamer',
    'value': 4,
  }],
 'offers': {
    '@type': 'Offer',
    'availability': 'http://schema.org/LimitedAvailability',
    'businessFunction': 'sell',
    'image': '...',
    'price': '290000.00',
    'priceCurrency': 'EUR',
    'url': 'https://www.pararius.nl/huis-te-koop/schiedam/...',
    'validFrom': '2021-06-02',
  },
}
```
