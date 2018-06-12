import re
import requests

pattern=r"<a href\s?=\s?[\"'](https?://.+?\.html)[\"']>"

def extract_urls(url):
    urls = list()
    res = requests.get(url)
    if res.status_code == 200:
        urls.extend(re.findall(pattern, res.text))
    return urls

def can_be_reached_in_2_steps(src, dest):
    first_step_urls = extract_urls(src)
    for first_step_url in first_step_urls:
        if dest in extract_urls(first_step_url):
            return True
    return False

src = input()
dest = input()
if can_be_reached_in_2_steps(src, dest):
    print('Yes')
else:
    print('No')