import requests
from bs4 import BeautifulSoup as BS
import re


def tt_bot(link):
    print(1)
    try:
        r = requests.get(link)
        soup = BS(r.content, 'html.parser')
        link_data = soup.find('div', class_='tiktok-yf3ohr-DivContainer e1yey0rl0')
        link = link_data.find('img').get("src")
        tt_download(link)
    except:
        link = 'Некорректная ссылка! (Ссылка с телефона)'
    return link

# def tt_bot_sound(link):
#
#     r = requests.get(link)
#     soup = BS(r.content, 'html.parser')
#     link_data = soup.find('h4',class_='tiktok-9y3z7x-H4Link e1wg6xq70')
#     name = link_data.find('a').text
#     link ="https://www.youtube.com/results?search_query="+name.replace(' ', '+').replace(',', '')
#     print(link)
#     ry=requests.get(link)
#     soupry = BS(ry.content, 'html.parser')
#     stname =soupry.find('a',class_='yt-simple-endpoint style-scope ytd-video-renderer')#.find('yt-formatted-string').text
#     print(stname)
#     # stname = 'Некорректная ссылка! (Ссылка с телефона)'
#     return stname


def tt_download(link):
    response = requests.get(link)
    if response.status_code == 200:
        with open('data/tiktok/ttimg.jpg', 'wb') as imgfile:
            imgfile.write(response.content)


# if __name__ == '__main__':
#     print(tt_bot_sound("https://www.tiktok.com/@hntgod/video/7047522586686803201?is_from_webapp=1&sender_device=pc&web_id7030831830690579970"))
