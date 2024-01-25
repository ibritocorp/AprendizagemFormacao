def pingSite(urlSite):
    import urllib.request
    try:
        urllib.request.urlopen(urlSite)
        print(f'\033[33mO site "{urlSite}" está acessível!\033[m')
    except urllib.error.URLError:
        print(f'\033[31mO site "{urlSite}" não está acessível.\033[m')
