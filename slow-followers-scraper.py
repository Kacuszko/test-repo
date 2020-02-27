import requests
from bs4 import BeautifulSoup
import json

instagram_url = 'https://instagram.com'
# username = 'kacuszko'


def get_followers_count(profile_url: str):
    response = requests.get(f"{instagram_url}/{profile_url}")
    # print(response.status_code)
    if response.ok:
        html = response.text
        bs_html = BeautifulSoup(html, 'html.parser')
        scripts = bs_html.select('script[type="application/ld+json"]')
        scripts_content = json.loads(scripts[0].text.strip())
        # print(json.dumps(scripts_content, indent=4, sort_keys=True))

        main_entity_of_page = scripts_content['mainEntityofPage']
        interaction_statistics = main_entity_of_page['interactionStatistic']
        followers_count = interaction_statistics['userInteractionCount']
        return followers_count


profiles = ['kacuszko', 'mariamalgosia']
for profile in profiles:
    count = get_followers_count(profile)
    print(f"{profile} has {count} followers")
