import re
import requests
from bs4 import BeautifulSoup

def get_heroes():
    """
    :return list: List of all hero names, as pulled from the icyveins tier list page https://www.icy-veins.com/heroes/heroes-of-the-storm-general-tier-list
    """
    url = "https://www.icy-veins.com/heroes/heroes-of-the-storm-general-tier-list"

    # Headers to mimic a browser visit
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Returns a requests.models.Response object
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.text, 'html.parser')
    regex = re.compile('ranking-.*')
    all_hero_spans = soup.find_all('span', attrs={'id': regex})
    heroes = [ span['id'][len("ranking-"):] for span in all_hero_spans ]

    return heroes

def get_hero_synergies(hero):
    """
    :param hero: The name of a hero to pull synergies for
    :return list[strings]: Heros that the named hero has synergies with, as pulled from the hero build guide page, Ex. https://www.icy-veins.com/heroes/diablo-build-guide
    """

    url = f'https://www.icy-veins.com/heroes/{hero}-build-guide'

    # Headers to mimic a browser visit
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Returns a requests.models.Response object
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.text, 'html.parser')

    regex = re.compile('hero-.*')
    synergies_soup = soup.find_all('img', attrs={'class': 'hero_portrait hero_portrait_good', 'data-heroes-tooltip': regex})
    synergies = [ syn['data-heroes-tooltip'][len('hero-'):] for syn in synergies_soup ]

    return synergies

def get_hero_counters(hero):
    """
    :param hero: The name of a hero to pull counters for
    :return list[strings]: Heros that the named hero is countered by, as pulled from the hero build guide page, Ex. https://www.icy-veins.com/heroes/diablo-build-guide
    """

    url = f'https://www.icy-veins.com/heroes/{hero}-build-guide'

    # Headers to mimic a browser visit
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Returns a requests.models.Response object
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.text, 'html.parser')

    regex = re.compile('hero-.*')
    counters_soup = soup.find_all('img', attrs={'class': 'hero_portrait hero_portrait_bad', 'data-heroes-tooltip': regex})
    counters = [ syn['data-heroes-tooltip'][len('hero-'):] for syn in counters_soup ]

    return counters

if __name__ == '__main__':
    hero_list = get_heroes()
    for hero in hero_list:
        print(hero)

        synergies = get_hero_synergies(hero)
        print("    Synergies")
        for synergy in synergies:
            print(f'        {synergy}')

        counters = get_hero_counters(hero)
        print("    Counters")
        for counter in counters:
            print(f'        {counter}')

