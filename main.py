# TODO: Add some tests so I'll know if this ever breaks
import re
import requests
import urllib.parse
from bs4 import BeautifulSoup

def get_heroes():
    """
    :return list: List of all hero names, as pulled from the heroesprofile page https://www.heroesprofile.com/Global/Hero/
    """
    url = "https://www.heroesprofile.com/Global/Hero/"

    # Headers to mimic a browser visit
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Returns a requests.models.Response object
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.text, 'html.parser')
    regex = re.compile('.*')
    all_tr = soup.find_all('tr', attrs={'data-hero': regex})
    heroes = [ tr['data-hero'] for tr in all_tr ]
    return heroes

def get_hero_top_5_matchups(hero, matchup_type):
    """
    :param hero: The name of a hero to pull a top 5 allies or threats for
    :param matchup_type: "allies" or "threats" # TODO: add validation to guarantee one of these two strings is passed
    :return list: List of hero names, either top 5 allies or top 5 threats depending on what was passed for matchup_type
    """

    url = f'https://www.heroesprofile.com/Global/Matchups/?hero={urllib.parse.quote(hero)}'

    # Headers to mimic a browser visit
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Returns a requests.models.Response object
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.text, 'html.parser')

    top_5_sections = soup.find_all('div', class_='rectangular-box hero-category')

    for section in top_5_sections:
        if matchup_type.lower() not in section.h3.text.lower():
            continue
        top_5 = section.find_all('div', class_='popup-trigger')
        names = [ hero.find('div', class_='popup').h4.text for hero in top_5 ]

    return names

if __name__ == '__main__':
    hero_list = get_heroes()
    for hero in hero_list:
        print(hero)

        allies = get_hero_top_5_matchups(hero, "allies")
        print("    Allies")
        for ally in allies:
            print(f'        {ally}')

        threats = get_hero_top_5_matchups(hero, "threats")
        print("    Threats")
        for enemy in threats:
            print(f'        {enemy}')

