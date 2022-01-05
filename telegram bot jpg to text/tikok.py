import requests
from bs4 import BeautifulSoup as BS
import re


def tt_download(link):
    r = requests.get(link)
    soup = BS(r.content, 'html.parser')
    Main_data=soup.find('div', class_='tiktok-19fglm-DivBodyContainer e1mw2lkl0')
    link_data=Main_data.find('div', class_='tiktok-1h63bmc-DivBasicPlayerWrapper e1yey0rl2')
    # link=link_data.find('video').get("src")
    return link_data
if __name__ == '__main__':
    print(tt_download("https://www.tiktok.com/foryou?is_copy_url=1&is_from_webapp=v1&item_id=7049011224549379333"
                      "#/@f1fanpost/video/7049011224549379333"))
