import json
import re
from typing import Any, Dict, List

import requests


rex_url = re.compile(r'href="/(?:huis|appartement)-te-(?:koop|huur)/[^"]+')
rex_json = re.compile(
    re.escape('<script type="application/ld+json">') + '(.+)' + re.escape('</script>'),
    re.DOTALL,
)
ROOT_URL = 'https://www.pararius.nl'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',  # noqa
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'cache-control': 'max-age=0',
    'referer': ROOT_URL,
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',  # noqa
}


def get_urls(url: str) -> List[str]:
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    return [f'{ROOT_URL}{u[6:]}' for u in rex_url.findall(r.text)]


def get_info(url: str) -> Dict[str, Any]:
    if not url.startswith(ROOT_URL):
        raise ValueError('invalid URL')
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    match = rex_json.search(r.text)
    if not match:
        raise ValueError('cannot find JSON data on page')
    raw = match.group(1)
    return json.loads(raw.splitlines()[1].strip())
