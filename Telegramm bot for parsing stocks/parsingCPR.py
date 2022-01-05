import requests
from datetime import datetime


def datatime():
    now = str(datetime.now().date()) + " "+str(datetime.now().hour) + ":"+str(datetime.now().minute)
    dataInfo = ""
    dataInfo = dataInfo + "\nАктуальная информация с сайта blockchain.com на " + now + " по МСК "
    return dataInfo


# Блокчейн.ком это Client side rendering
def parse_crypto_rub():
    r = requests.get('https://www.blockchain.com/prices/api/coin-list-page?limit=20&page=0&tsym=RUB')
    data = r.json()
    strInfo = ""
    for i in range(10):
        sub_list = data['Data'][i]
        strInfo = strInfo + "\n💼 Название - " + sub_list['CoinInfo']['FullName']
        strInfo = strInfo + "\n💸 Цена сейчас = " + sub_list['DISPLAY']['RUB']['PRICE']
        strInfo = strInfo + "\n💱 Дельта за день = " + sub_list['DISPLAY']['RUB']['CHANGEDAY'] + "\n"
    strInfo = strInfo + datatime()
    return strInfo


def parse_crypto_usd():
    r = requests.get('https://www.blockchain.com/prices/api/coin-list-page?limit=20&page=0&tsym=USD')
    data = r.json()
    strInfo = ""
    for i in range(10):
        sub_list = data['Data'][i]
        strInfo = strInfo + "\n💼 Название - " + sub_list['CoinInfo']['FullName']
        strInfo = strInfo + "\n💸 Цена сейчас = " + sub_list['DISPLAY']['USD']['PRICE']
        strInfo = strInfo + "\n💱 Дельта за день = " + sub_list['DISPLAY']['USD']['CHANGEDAY'] + "\n"
    strInfo = strInfo + datatime()
    return strInfo


def cr_best_up():
    r = requests.get('https://www.blockchain.com/prices/api/coin-list-page?limit=20&page=0&tsym=USD')
    data = r.json()
    strInfo = ""
    tiker = float(data['Data'][0]['DISPLAY']['USD']['CHANGEPCT24HOUR'])
    for i in range(10):
        sub_list = data['Data'][i]
        tiker2 = float(data['Data'][i]['DISPLAY']['USD']['CHANGEPCT24HOUR'])
        if tiker < tiker2:
            strInfo = "\n💼 Название - " + sub_list['CoinInfo']['FullName']
            strInfo = strInfo + "\n💸 Цена сейчас = " + sub_list['DISPLAY']['USD']['PRICE']
            strInfo = strInfo + "\n💱 Дельта за день = " + sub_list['DISPLAY']['USD']['CHANGEDAY']
            strInfo = strInfo + "\n📈 Рост за день= " + sub_list['DISPLAY']['USD']['CHANGEPCT24HOUR'] + "%\n"
            tiker = tiker2
    strInfo = strInfo + datatime()
    return strInfo


def cr_best_down():
    r = requests.get('https://www.blockchain.com/prices/api/coin-list-page?limit=20&page=0&tsym=USD')
    data = r.json()
    strInfo = ""
    tiker = float(data['Data'][0]['DISPLAY']['USD']['CHANGEPCT24HOUR'])
    for i in range(10):
        sub_list = data['Data'][i]
        tiker2 = float(data['Data'][i]['DISPLAY']['USD']['CHANGEPCT24HOUR'])
        if tiker > tiker2:
            strInfo = "\n💼 Название - " + sub_list['CoinInfo']['FullName']
            strInfo = strInfo + "\n💸 Цена сейчас = " + sub_list['DISPLAY']['USD']['PRICE']
            strInfo = strInfo + "\n💱 Дельта за день = " + sub_list['DISPLAY']['USD']['CHANGEDAY']
            strInfo = strInfo + "\n📉 Падение за день= " + sub_list['DISPLAY']['USD']['CHANGEPCT24HOUR'] + "%\n"
            tiker = tiker2
    strInfo = strInfo + datatime()
    return strInfo


#if __name__ == '__main__':
   # print(best_down())
