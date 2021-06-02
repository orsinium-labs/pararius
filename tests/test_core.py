import pararius


def test_get_urls():
    search_url = 'https://www.pararius.nl/koopwoningen/nederland/bestaande-bouw/huis'
    urls = pararius.get_urls(search_url)
    assert len(urls) == 60
    for url in urls:
        assert url.startswith('https://www.pararius.nl/huis-te-koop/')


def test_get_info():
    search_url = 'https://www.pararius.nl/koopwoningen/nederland/bestaande-bouw/huis'
    urls = pararius.get_urls(search_url)
    info = pararius.get_info(urls[0])
    assert 'address' in info
    assert 'description' in info
    assert 'name' in info
