import requests
from datetime import datetime
from bs4 import BeautifulSoup as BS
import re


def datatime():
    now = str(datetime.now().date()) + " " + str(datetime.now().hour) + ":" + str(datetime.now().minute)
    dataInfo = ""
    dataInfo = dataInfo + "\nАктуальная информация с сайта finance.yahoo.com на " + now + " по МСК "
    return dataInfo


def datatime_ru():
    now = str(datetime.now().date()) + " " + str(datetime.now().hour) + ":" + str(datetime.now().minute)
    dataInfo = ""
    dataInfo = dataInfo + "\nАктуальная информация с сайта smart-lab.ru на " + now + " по МСК "
    return dataInfo


def parse_usd_up():
    response = requests.get('https://finance.yahoo.com/screener/predefined/day_gainers')
    soup = BS(response.content, 'html.parser')
    dt_str = ""
    MainData = soup.find_all("tr", class_="simpTblRow Bgc($hoverBgColor):h BdB Bdbc($seperatorColor) Bdbc("
                                          "$tableBorderBlue):h H(32px) Bgc($lv2BgColor)")
    for i in range(5):
        sub_list = MainData[i]
        dt_str += "\n" + str(i + 1) + ")   💼 Полное название - " + sub_list.find('td', {'aria-label': 'Name'}).text
        dt_str += "\n🏷️Тикер $" + sub_list.find('a', {'data-test': 'quoteLink'}).text
        dt_str += "\n📈Рост в процентах " + sub_list.find('td', {'aria-label': '% Change'}).text
        dt_str += "\n💲Цена = " + sub_list.find('td', {'aria-label': 'Price (Intraday)'}).text + " $USD\n"
    dt_str += datatime()
    return dt_str


def parse_usd_dwn():
    response = requests.get('https://finance.yahoo.com/screener/predefined/day_losers')
    soup = BS(response.content, 'html.parser')
    dt_str = ""
    MainData = soup.find_all("tr", class_="simpTblRow Bgc($hoverBgColor):h BdB Bdbc($seperatorColor) Bdbc("
                                          "$tableBorderBlue):h H(32px) Bgc($lv2BgColor)")
    for i in range(5):
        sub_list = MainData[i]
        dt_str += "\n" + str(i + 1) + ")   💼 Полное название - " + sub_list.find('td', {'aria-label': 'Name'}).text
        dt_str += "\n🏷️Тикер $" + sub_list.find('a', {'data-test': 'quoteLink'}).text
        dt_str += "\n📈Падение в процентах " + sub_list.find('td', {'aria-label': '% Change'}).text
        dt_str += "\n💲Цена = " + sub_list.find('td', {'aria-label': 'Price (Intraday)'}).text + " $USD\n"
    dt_str += datatime()
    return dt_str


def parse_usd_top():
    response = requests.get('https://finance.yahoo.com/screener/predefined/most_actives')
    soup = BS(response.content, 'html.parser')
    dt_str = ""
    MainData = soup.find_all("tr", class_="simpTblRow Bgc($hoverBgColor):h BdB Bdbc($seperatorColor) Bdbc("
                                          "$tableBorderBlue):h H(32px) Bgc($lv2BgColor)")
    for i in range(10):
        sub_list = MainData[i]
        dt_str += "\n" + str(i + 1) + ")  💼 Полное название - " + sub_list.find('td', {'aria-label': 'Name'}).text
        dt_str += "\n🏷️ Тикер $" + sub_list.find('a', {'data-test': 'quoteLink'}).text
        dt_str += "\n📈 Изменение в процентах " + sub_list.find('td', {'aria-label': '% Change'}).text
        dt_str += "\n💲Цена = " + sub_list.find('td', {'aria-label': 'Price (Intraday)'}).text + " $USD\n"
    dt_str += datatime()
    return dt_str


def parse_rub_top():
    response = requests.get('https://smart-lab.ru/q/shares/')
    soup = BS(response.content, 'html.parser')
    dt_str = ""
    MainData = soup.find_all("tr")
    for i in range(11):
        sub_list = MainData[i + 1]
        dt_str += "\n" + str(i + 1) + ") 💼 Полное название - " + sub_list.find('a').text
        sub_list2 = sub_list.find_all("td")
        dt_str += "\n🏷️ Тикер $" + sub_list2[3].text
        dt_str += "\n📈 Изменение в процентах" + re.sub("^\s+|\n|\r|\s+$", '', sub_list2[8].text)
        dt_str += "\n💲Цена " + sub_list2[7].text + " ₽RUB\n"
    dt_str += datatime_ru()
    return dt_str


def parse_rub_up():
    response = requests.get('https://smart-lab.ru/q/shares/order_by_last_to_prev_price/desc/')
    soup = BS(response.content, 'html.parser')
    dt_str = ""
    MainData = soup.find_all("tr")
    for i in range(5):
        sub_list = MainData[i + 2]
        dt_str += "\n" + str(i + 1) + ") 💼 Полное название - " + sub_list.find('a').text
        sub_list2 = sub_list.find_all("td")
        dt_str += "\n🏷️ Тикер $" + sub_list2[3].text
        dt_str += "\n📈 Рост в процентах" + re.sub("^\s+|\n|\r|\s+$", '', sub_list2[8].text)
        dt_str += "\n💲Цена " + sub_list2[7].text + " ₽RUB\n"
    dt_str += datatime_ru()
    return dt_str


def parse_rub_down():
    response = requests.get('https://smart-lab.ru/q/shares/order_by_last_to_prev_price/asc/')
    soup = BS(response.content, 'html.parser')
    dt_str = ""
    MainData = soup.find_all("tr")
    for i in range(5):
        sub_list = MainData[i + 2]
        dt_str += "\n" + str(i + 1) + ") 💼 Полное название - " + sub_list.find('a').text
        sub_list2 = sub_list.find_all("td")
        dt_str += "\n🏷️ Тикер $" + sub_list2[3].text
        dt_str += "\n📈 Падение в процентах" + re.sub("^\s+|\n|\r|\s+$", '', sub_list2[8].text)
        dt_str += "\n💲Цена " + sub_list2[7].text + " ₽RUB\n"
    dt_str += datatime_ru()
    return dt_str


if __name__ == '__main__':
    print(parse_rub_up())
