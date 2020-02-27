import requests
from bs4 import BeautifulSoup
import json
import asyncio
from concurrent.futures import ThreadPoolExecutor
import time

instagram_url = 'https://instagram.com'
# username = 'kacuszko'


def get_followers_count(profile_url: str, session):
    response = session.get(f"{instagram_url}/{profile_url}")
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
        return float(followers_count)


async def get_followers_async(profiles: list) -> list:
    res = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        with requests.Session() as session:
            loop = asyncio.get_event_loop()
            tasks = [
                loop.run_in_executor(executor, get_followers_count, *(profile, session)) for profile in profiles
            ]
            for response in await asyncio.gather(*tasks):
                res.append(response)
    return res

# SYNCH
start = time.time()
profiles = ['kacuszko', 'mariamalgosia']
for profile in profiles:
    count = get_followers_count(profile, requests)
    print(f"{profile} has {count} followers")
end = time.time()
elapsed = end - start
print(f"SYNCHRONOUSLY took {elapsed} seconds")

# ASYNC
start = time.time()
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(get_followers_async(profiles))
res = loop.run_until_complete(future)
print(res)
end = time.time()
elapsed = end - start
print(f"ASYNC MULTI-THREADING took {elapsed} seconds")
