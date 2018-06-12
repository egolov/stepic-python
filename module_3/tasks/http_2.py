import re
import requests

link_pattern = r"<a.+?href\s?=\s?[\"'](.+?)[\"'].*?>"


def parse_hosts(text):
    links = re.findall(link_pattern, text)
    res = set()
    for link in links:
        if link.startswith(('..', '.')):
            continue
        if '://' in link:
            # skip protocol
            link = link.split('://')[1]
        host_port = link.split('/')[0]
        host = host_port.split(':')[0]
        res.add(host)
    return res

if __name__ == '__main__':
    url = input()
    url = url.rstrip().lstrip()
    res = requests.get(url)
    if res.status_code == 200:
        text = res.text
        hosts = parse_hosts(text)
        print("\n".join(sorted(hosts)))